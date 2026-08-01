<?php
// Hotel Mayflower — contact form handler.
//
// Design goal: a submission is never lost.
//   1. every message is written to disk first (outside the web root)
//   2. then delivery is attempted over authenticated SMTP
//   3. if SMTP is not configured, it falls back to PHP mail()
// Even if mail delivery breaks, the message is safely on the server.
//
// Configuration lives OUTSIDE this repository so deploys never overwrite it:
//   /home/<user>/mayflower-mail-config.php   (see mail-config.sample.php)
//
// Endpoints:
//   POST /contact.php            submit the form
//   GET  /contact.php?ping=1     liveness check
//   GET  /contact.php?selftest=<token>   send a test mail, report the exact error

declare(strict_types=1);
header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

const MAX_NAME = 200;
const MAX_MESSAGE = 5000;
const RATE_LIMIT_PER_HOUR = 12;

function respond(int $code, bool $ok, string $note = '', array $extra = []): void {
    http_response_code($code);
    echo json_encode(['ok' => $ok, 'note' => $note] + $extra, JSON_UNESCAPED_UNICODE);
    exit;
}

/** Where the config may live. PHP is often restricted (open_basedir) to the
 *  document root, so a location inside it is offered as a fallback. */
function config_candidates(): array {
    $doc = rtrim((string)($_SERVER['DOCUMENT_ROOT'] ?? ''), '/');
    return array_filter([
        home_dir() . '/mayflower-mail-config.php',
        $doc !== '' ? dirname($doc) . '/mayflower-mail-config.php' : '',
        $doc !== '' ? $doc . '/.data/mail-config.php' : '',
    ]);
}

/** First writable storage directory, preferring one outside the web root. */
function storage_dir(): string {
    $doc = rtrim((string)($_SERVER['DOCUMENT_ROOT'] ?? ''), '/');
    $candidates = array_filter([
        home_dir() . '/contact-messages',
        $doc !== '' ? $doc . '/.data/contact-messages' : '',
        sys_get_temp_dir() . '/mayflower-contact',
    ]);
    foreach ($candidates as $dir) {
        if (@is_dir($dir) ? @is_writable($dir) : @mkdir($dir, 0700, true)) {
            // Belt and braces: if it ended up under the web root, deny access.
            $guard = dirname($dir) . '/.htaccess';
            if ($doc !== '' && strpos($dir, $doc) === 0 && !file_exists($guard)) {
                @file_put_contents($guard, "Require all denied\nDeny from all\n");
            }
            return $dir;
        }
    }
    return '';
}

function home_dir(): string {
    $h = getenv('HOME');
    if ($h && is_dir($h)) return rtrim($h, '/');
    if (function_exists('posix_getpwuid') && function_exists('posix_geteuid')) {
        $pw = @posix_getpwuid(posix_geteuid());
        if (!empty($pw['dir']) && is_dir($pw['dir'])) return rtrim($pw['dir'], '/');
    }
    // Last resort: two levels above the document root (public_html/hotel -> home)
    $guess = dirname((string)($_SERVER['DOCUMENT_ROOT'] ?? ''), 2);
    return is_dir($guess) ? $guess : sys_get_temp_dir();
}

function load_config(): array {
    $defaults = [
        'to'            => ['info@hotelmayflower.nl'],
        'from_email'    => '',      // must be a sender the SMTP account may use
        'from_name'     => 'Hotel Mayflower website',
        'smtp_host'     => '',      // e.g. mail.smtp2go.com
        'smtp_port'     => 587,
        'smtp_secure'   => 'tls',   // 'tls' (587) or 'ssl' (465)
        'smtp_user'     => '',
        'smtp_pass'     => '',
        'selftest_token' => '',
    ];
    foreach (config_candidates() as $path) {
        if (@is_readable($path)) {
            $cfg = @include $path;
            if (is_array($cfg)) return array_merge($defaults, $cfg, ['_config_path_found' => true]);
        }
    }
    return $defaults + ['_config_path_found' => false];
}

/** Append one record to ~/contact-messages/YYYY-MM.jsonl. Returns the file path or ''. */
function store_message(array $record): string {
    $dir = storage_dir();
    if ($dir === '') return '';
    $file = $dir . '/' . gmdate('Y-m') . '.jsonl';
    $line = json_encode($record, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n";
    return @file_put_contents($file, $line, FILE_APPEND | LOCK_EX) === false ? '' : $file;
}

/** Crude per-IP rate limit based on the stored log. */
function rate_limited(string $ip): bool {
    $dir = storage_dir();
    if ($dir === '') return false;
    $file = $dir . '/' . gmdate('Y-m') . '.jsonl';
    if (!is_readable($file)) return false;
    $cut = time() - 3600;
    $hits = 0;
    $fh = @fopen($file, 'r');
    if (!$fh) return false;
    // Only the tail matters; read the last 64 KB.
    $size = filesize($file) ?: 0;
    if ($size > 65536) fseek($fh, -65536, SEEK_END);
    while (($line = fgets($fh)) !== false) {
        $row = json_decode($line, true);
        if (!is_array($row) || ($row['ip'] ?? '') !== $ip) continue;
        if (strtotime((string)($row['at'] ?? '')) >= $cut) $hits++;
    }
    fclose($fh);
    return $hits >= RATE_LIMIT_PER_HOUR;
}

function mime_header(string $text): string {
    return preg_match('/[^\x20-\x7E]/', $text)
        ? '=?UTF-8?B?' . base64_encode($text) . '?='
        : $text;
}

/**
 * Minimal authenticated SMTP client (STARTTLS or implicit TLS).
 * Returns [true, ''] on success or [false, 'reason'].
 */
function smtp_send(array $cfg, string $to, string $subject, string $body, string $replyTo): array {
    $host = (string)$cfg['smtp_host'];
    $port = (int)$cfg['smtp_port'];
    $secure = strtolower((string)$cfg['smtp_secure']);
    $from = (string)$cfg['from_email'];
    if ($host === '' || $from === '') return [false, 'smtp not configured'];

    $target = ($secure === 'ssl' ? 'ssl://' : 'tcp://') . $host . ':' . $port;
    $ctx = stream_context_create(['ssl' => [
        'verify_peer' => true, 'verify_peer_name' => true, 'SNI_enabled' => true,
    ]]);
    $fp = @stream_socket_client($target, $errno, $errstr, 15, STREAM_CLIENT_CONNECT, $ctx);
    if (!$fp) return [false, "connect failed: $errstr ($errno)"];
    stream_set_timeout($fp, 15);

    $read = function () use ($fp): string {
        $out = '';
        while (($line = fgets($fp, 515)) !== false) {
            $out .= $line;
            if (strlen($line) < 4 || $line[3] !== '-') break;
        }
        return $out;
    };
    $cmd = function (string $line) use ($fp, $read): string {
        fwrite($fp, $line . "\r\n");
        return $read();
    };
    $ok = fn(string $r, string $codes): bool => in_array(substr($r, 0, 3), explode(',', $codes), true);

    $greet = $read();
    if (!$ok($greet, '220')) { fclose($fp); return [false, 'bad greeting: ' . trim($greet)]; }

    $ehloName = $_SERVER['SERVER_NAME'] ?? 'localhost';
    $r = $cmd('EHLO ' . $ehloName);
    if (!$ok($r, '250')) { fclose($fp); return [false, 'EHLO refused: ' . trim($r)]; }

    if ($secure === 'tls') {
        $r = $cmd('STARTTLS');
        if (!$ok($r, '220')) { fclose($fp); return [false, 'STARTTLS refused: ' . trim($r)]; }
        if (!@stream_socket_enable_crypto($fp, true, STREAM_CRYPTO_METHOD_TLS_CLIENT)) {
            fclose($fp); return [false, 'TLS handshake failed'];
        }
        $r = $cmd('EHLO ' . $ehloName);
        if (!$ok($r, '250')) { fclose($fp); return [false, 'EHLO after TLS refused: ' . trim($r)]; }
    }

    if ((string)$cfg['smtp_user'] !== '') {
        $r = $cmd('AUTH LOGIN');
        if (!$ok($r, '334')) { fclose($fp); return [false, 'AUTH not accepted: ' . trim($r)]; }
        $r = $cmd(base64_encode((string)$cfg['smtp_user']));
        if (!$ok($r, '334')) { fclose($fp); return [false, 'username rejected: ' . trim($r)]; }
        $r = $cmd(base64_encode((string)$cfg['smtp_pass']));
        if (!$ok($r, '235')) { fclose($fp); return [false, 'login failed: ' . trim($r)]; }
    }

    $r = $cmd('MAIL FROM:<' . $from . '>');
    if (!$ok($r, '250')) { fclose($fp); return [false, 'MAIL FROM rejected: ' . trim($r)]; }
    $r = $cmd('RCPT TO:<' . $to . '>');
    if (!$ok($r, '250,251')) { fclose($fp); return [false, 'RCPT TO rejected: ' . trim($r)]; }
    $r = $cmd('DATA');
    if (!$ok($r, '354')) { fclose($fp); return [false, 'DATA refused: ' . trim($r)]; }

    $headers = [
        'Date: ' . date('r'),
        'From: ' . mime_header((string)$cfg['from_name']) . ' <' . $from . '>',
        'To: <' . $to . '>',
        'Subject: ' . mime_header($subject),
        'Message-ID: <' . bin2hex(random_bytes(8)) . '@hotelmayflower.nl>',
        'MIME-Version: 1.0',
        'Content-Type: text/plain; charset=UTF-8',
        'Content-Transfer-Encoding: 8bit',
        'X-Mailer: hotelmayflower-site',
    ];
    if ($replyTo !== '') $headers[] = 'Reply-To: <' . $replyTo . '>';

    // Dot-stuffing: a line consisting of "." would end the message early.
    $data = implode("\r\n", $headers) . "\r\n\r\n"
          . preg_replace('/^\./m', '..', str_replace("\n", "\r\n", $body));
    fwrite($fp, $data . "\r\n.\r\n");
    $r = $read();
    $cmd('QUIT');
    fclose($fp);

    return $ok($r, '250') ? [true, ''] : [false, 'message rejected: ' . trim($r)];
}

// ---------------------------------------------------------------- routing

$cfg = load_config();

if (isset($_GET['ping'])) {
    $store = storage_dir();
    respond(200, true, 'alive', [
        'smtp'    => $cfg['smtp_host'] !== '' ? 'configured' : 'not configured',
        'config'  => !empty($cfg['_config_path_found']) ? 'found' : 'not found',
        'storage' => $store !== '' ? 'writable' : 'NOT writable',
        'looked_in' => array_map(fn($p) => str_replace(home_dir(), '~', $p), config_candidates()),
    ]);
}

if (isset($_GET['selftest'])) {
    $token = (string)$cfg['selftest_token'];
    if ($token === '' || !hash_equals($token, (string)$_GET['selftest'])) respond(403, false, 'bad token');
    $to = $cfg['to'][0];
    [$sent, $err] = smtp_send($cfg, $to, 'Testbericht van de website',
        "Dit is een test vanaf het contactformulier van hotelmayflower.nl.\nAls u dit ziet, werkt de verzending.\n", '');
    if (!$sent && $cfg['smtp_host'] === '') {
        $sent = @mail($to, 'Testbericht van de website', "Test via PHP mail().\n",
            'From: ' . $cfg['from_name'] . ' <' . ($cfg['from_email'] ?: 'noreply@hotelmayflower.nl') . ">\r\n");
        $err = $sent ? '' : 'mail() returned false';
    }
    respond($sent ? 200 : 500, $sent, $sent ? 'test sent to ' . $to : $err,
        ['transport' => $cfg['smtp_host'] !== '' ? 'smtp' : 'mail()']);
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') respond(405, false, 'method');

// Honeypot: bots fill every field. Pretend success so they stop retrying.
if (!empty($_POST['website'])) respond(200, true);

$name    = trim((string)($_POST['name'] ?? ''));
$email   = trim((string)($_POST['email'] ?? ''));
$arrival = trim((string)($_POST['arrival'] ?? ''));
$nights  = trim((string)($_POST['nights'] ?? ''));
$message = trim((string)($_POST['message'] ?? ''));
$ip      = (string)($_SERVER['REMOTE_ADDR'] ?? '');

if ($name === '' || $message === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    respond(422, false, 'validation');
}
if (mb_strlen($name) > MAX_NAME || mb_strlen($message) > MAX_MESSAGE
    || preg_match('/[\r\n]/', $name . $email)) {
    respond(422, false, 'invalid');
}
if (rate_limited($ip)) respond(429, false, 'too many messages');

// 1. Store first — this is what makes the form reliable.
$record = [
    'at' => gmdate('c'), 'name' => $name, 'email' => $email,
    'arrival' => $arrival, 'nights' => $nights, 'message' => $message,
    'ip' => $ip, 'lang' => (string)($_POST['lang'] ?? ''),
    'ua' => substr((string)($_SERVER['HTTP_USER_AGENT'] ?? ''), 0, 200),
];
$stored = store_message($record);

// 2. Then deliver.
$subject = 'Bericht via de website - ' . $name;
$body = "Nieuw bericht via het contactformulier van hotelmayflower.nl\n"
      . "----------------------------------------------------------\n"
      . "Naam:     $name\n"
      . "E-mail:   $email\n";
if ($arrival !== '') $body .= "Aankomst: $arrival\n";
if ($nights !== '')  $body .= "Nachten:  $nights\n";
$body .= "\nBericht:\n$message\n\n"
       . "----------------------------------------------------------\n"
       . "Beantwoord deze e-mail om de gast rechtstreeks te antwoorden.\n";

$sent = false; $error = '';
foreach ((array)$cfg['to'] as $recipient) {
    [$ok1, $err1] = smtp_send($cfg, $recipient, $subject, $body, $email);
    if ($ok1) { $sent = true; continue; }
    $error = $err1;
    // Fallback: local mail() — only useful if the server may send for this domain.
    $from = $cfg['from_email'] ?: 'noreply@' . preg_replace('/^www\./', '', (string)($_SERVER['HTTP_HOST'] ?? 'hotelmayflower.nl'));
    $hdr = 'From: ' . mime_header((string)$cfg['from_name']) . ' <' . $from . ">\r\n"
         . 'Reply-To: <' . $email . ">\r\n"
         . "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8";
    if (@mail($recipient, $subject, $body, $hdr)) $sent = true;
}

if ($sent) respond(200, true, 'sent');
// Not delivered, but safely stored: the guest should not be asked to retype.
if ($stored !== '') respond(200, true, 'stored', ['delivery' => 'deferred']);
respond(500, false, $error !== '' ? $error : 'delivery failed');
