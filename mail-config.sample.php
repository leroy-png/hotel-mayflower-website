<?php
// Hotel Mayflower — mail configuration SAMPLE.
//
// Copy this file to your home directory (NOT into the website folder):
//     /home/themayflower/mayflower-mail-config.php
// then fill in the SMTP credentials. It is read by contact.php.
// Keeping it outside the repository means deploys never overwrite or expose it.
//
// In cPanel File Manager: go to /home/themayflower, "+ File",
// name it mayflower-mail-config.php, then Edit and paste the contents below.

return [
    // Where enquiries should arrive. More than one address is allowed.
    'to' => ['info@hotelmayflower.nl'],

    // The sender address. Must be one the SMTP account is allowed to use.
    // With SMTP2GO: any address on a verified sender domain, e.g.:
    'from_email' => 'website@hotelmayflower.nl',
    'from_name'  => 'Hotel Mayflower website',

    // --- SMTP credentials -------------------------------------------------
    // Option A (recommended) — SMTP2GO, already configured in your DNS:
    //   host mail.smtp2go.com, port 587, user + password from the SMTP2GO
    //   dashboard under "Sending" > "SMTP Users".
    'smtp_host'   => 'mail.smtp2go.com',
    'smtp_port'   => 587,
    'smtp_secure' => 'tls',          // 'tls' for 587, 'ssl' for 465
    'smtp_user'   => 'PASTE-SMTP2GO-USERNAME',
    'smtp_pass'   => 'PASTE-SMTP2GO-PASSWORD',

    // Option B — Microsoft 365 mailbox (needs SMTP AUTH enabled for that
    // mailbox in the Microsoft admin centre; many tenants disable it):
    //   'smtp_host' => 'smtp.office365.com', 'smtp_port' => 587,
    //   'smtp_secure' => 'tls',
    //   'smtp_user' => 'info@hotelmayflower.nl', 'smtp_pass' => '...',

    // Secret for the built-in test:
    //   https://www.hotelmayflower.nl/contact.php?selftest=THIS-VALUE
    // Pick any long random string.
    'selftest_token' => 'CHANGE-ME-to-a-long-random-string',
];
