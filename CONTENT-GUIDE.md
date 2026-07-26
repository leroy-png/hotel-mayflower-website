# Hotel Mayflower website — content guide

The site is plain HTML, CSS and JavaScript. There is no CMS and no build step:
**what you edit is what goes live.** Any text editor works (VS Code recommended).

## Folder map

| What | Where |
|---|---|
| English pages | `en/…/index.html` (home, `rooms/`, `rooms/single/`, `rooms/double/`, `rooms/triple/`, `leiden/`, `hotel-information/`, `contact/`, `faq/`, `privacy/`, `terms/`) |
| Dutch pages | `nl/…/index.html` (same structure: `kamers/`, `hotelinformatie/`, `veelgestelde-vragen/`, `voorwaarden/`) |
| All styling | `assets/css/main.css` (brand colours at the top under `Tokens`) |
| Behaviour | `assets/js/main.js` |
| Photos | `assets/img/` — each photo exists as `-480/-960/-1600/(-2400)` in `.avif`, `.webp`, `.jpg` |
| Videos | `assets/video/` |
| Logos | `assets/logo/` |
| Fonts | `assets/fonts/` (self-hosted, no Google servers involved) |

## Editing text

Open the page's `index.html`, find the text, change it, save. **Always change both
languages** (`en/…` and `nl/…`) so the site stays in sync.

## Adding or replacing a photo

1. Convert your photo into the three formats and sizes. With
   [ffmpeg](https://ffmpeg.org) + cwebp + avifenc installed (`brew install ffmpeg webp libavif`):

   ```bash
   # from the website folder — replace NAME and SOURCE
   for w in 480 960 1600; do
     sips -s format jpeg -s formatOptions 82 --resampleWidth $w SOURCE.jpg --out assets/img/NAME-$w.jpg
     cwebp -q 78 assets/img/NAME-$w.jpg -o assets/img/NAME-$w.webp
     avifenc -q 55 -s 8 assets/img/NAME-$w.jpg assets/img/NAME-$w.avif
   done
   ```

2. Reference it in the page with the same `<picture>` pattern used everywhere.
3. Write a meaningful `alt` text — describe what a guest actually sees.

## The contact form

The form works out of the box via the visitor's own email app (mailto).
To switch to server-side sending: create a free form endpoint (e.g. formspree.io
or usebasin.com, EU region), then put its URL in `assets/js/main.js`:

```js
var FORM_ENDPOINT = "https://formspree.io/f/XXXXXXX";
```

## The booking bar

Booking buttons link to the SiteMinder engine. The search bar passes check-in,
check-out and language automatically. Nothing to maintain. If the booking URL
ever changes, update `BOOKING_URL` in `assets/js/main.js` **and** every
`direct-book.com` link in the HTML (search & replace across the folder).

## Guest reviews section

The homepage contains a prepared, commented-out reviews section
(search for `GUEST REVIEWS` in `en/index.html` / `GASTBEOORDELINGEN` in
`nl/index.html`). Paste three real guest quotes and remove the comment markers.

## Regenerating pages (optional, for bulk changes)

The interior pages were generated once by the scripts in `tools/`. For a
site-wide change to the header or footer, edit `tools/_shared.py` and run:

```bash
cd tools && python3 gen_en.py && python3 gen_nl.py
```

⚠️ This overwrites the generated pages — if you have edited those HTML files
directly, make the same edit in the `tools/` scripts instead, or skip the
scripts entirely and keep editing the HTML by hand. The EN homepage
(`en/index.html`) and EN rooms overview (`en/rooms/index.html`) are **not**
generated — they are always edited directly.

## Publishing

The folder deploys to any static host (Netlify, Cloudflare Pages, Vercel, or
classic hosting via FTP). Requirements:

- serve `index.html` for `/`, and each folder's `index.html` for clean URLs (default everywhere)
- serve `404.html` for unknown URLs
- HTTPS on — every static host does this automatically

After publishing, submit `https://www.hotelmayflower.nl/sitemap.xml` in
Google Search Console once.
