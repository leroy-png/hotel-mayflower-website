<?php
// Hotel Mayflower — contact form handler (runs on the cPanel server).
// The site JS posts FormData here and expects a 2xx on success.
// GET /contact.php?ping=1 answers without sending mail (deploy check).

declare(strict_types=1);
header('Content-Type: application/json; charset=utf-8');

function respond(int $code, bool $ok, string $note = ''): void {
    http_response_code($code);
    echo json_encode(['ok' => $ok, 'note' => $note]);
    exit;
}

if (isset($_GET['ping'])) {
    respond(200, true, 'alive');
}
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    respond(405, false, 'method');
}

// Honeypot: bots fill every field; pretend success so they move on
if (!empty($_POST['website'])) {
    respond(200, true);
}

$name    = trim((string)($_POST['name'] ?? ''));
$email   = trim((string)($_POST['email'] ?? ''));
$arrival = trim((string)($_POST['arrival'] ?? ''));
$nights  = trim((string)($_POST['nights'] ?? ''));
$message = trim((string)($_POST['message'] ?? ''));

if ($name === '' || $message === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    respond(422, false, 'validation');
}
if (mb_strlen($name) > 200 || mb_strlen($message) > 5000 || preg_match('/[\r\n]/', $name . $email)) {
    respond(422, false, 'invalid');
}

$to = 'info@hotelmayflower.nl';

// From must be a domain hosted on this server for SPF/deliverability.
// Works for hotel.themayflower.nl now and hotelmayflower.nl after the move.
$host = strtolower(preg_replace('/[^a-z0-9.-]/i', '', $_SERVER['HTTP_HOST'] ?? 'themayflower.nl'));
$host = preg_replace('/^(www|hotel)\./', '', $host);

$subject = 'Bericht via de website - ' . preg_replace('/[^\PC ]/u', '', $name);

$body = "Nieuw bericht via het contactformulier van de website\n"
      . "-----------------------------------------------------\n"
      . "Naam:     $name\n"
      . "E-mail:   $email\n";
if ($arrival !== '') { $body .= "Aankomst: $arrival\n"; }
if ($nights !== '')  { $body .= "Nachten:  $nights\n"; }
$body .= "\nBericht:\n$message\n";

$headers = "From: Hotel Mayflower website <noreply@$host>\r\n"
         . "Reply-To: $email\r\n"
         . "X-Mailer: hotelmayflower-site\r\n"
         . "Content-Type: text/plain; charset=UTF-8";

if (@mail($to, $subject, $body, $headers)) {
    respond(200, true, 'sent');
}
respond(500, false, 'mail');
