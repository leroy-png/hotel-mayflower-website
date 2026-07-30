# Launch checklist — items needing confirmation or delivery

Deliverable 13 from the design brief: everything that is missing, unconfirmed,
or intentionally left out, in priority order.

## Blocking questions (answer before/at launch)

1. ~~Reception staffed hours.~~ **Resolved 2026-07-26:** reception is open
   09:00–18:00 and guests have 24/7 building access with their own key — now
   stated on Hotel information, Contact and FAQ in both languages. Note: the
   printed welcome letter still says 07:00–21:00; update that print item to
   match.
2. **Key-locker wording.** The site says: arrange in advance → key in the locker →
   let yourself in. Confirm this matches the actual procedure (and whether the
   locker is by the entrance or across from reception).
3. **"22 rooms"** is mentioned on the rooms pages — taken from your staff app.
   Confirm the number.
4. **Geo-coordinates** in structured data are `52.1607, 4.4854` (approximate).
   Verify the pin in Google Maps and correct if needed.
5. **Breakfast timeline.** Copy says "temporarily unavailable due to renovation
   works". When breakfast returns (or is discontinued permanently), the texts on
   Home, Hotel information and FAQ need one-line updates — in both languages.

## Missing content (site has prepared slots)

6. **Guest reviews** — homepage section is built but commented out. Provide three
   genuine quotes (Google/Booking.com, with reviewer consent) per language.
7. **Social media URLs** — the footer currently has no social links; send the
   Facebook/Instagram URLs and they go in.
8. ~~Contact-form endpoint~~ **Resolved 2026-07-27:** the site now ships its
   own `contact.php` on the cPanel server; submissions are emailed to
   info@hotelmayflower.nl (honeypot spam filter included). Note: the form on
   the GitHub Pages preview URL shows the error message by design — PHP only
   runs on the real server.
9. **Terrace** — photos excluded on your instruction (not presentable yet). When
   ready: shoot 2–3 photos, confirm whether smoking is allowed there, and it gets
   a section on Home + Hotel information.

## Photo wishlist (site works, but these would lift it)

10. ~~Bathroom~~ **Added 2026-07-30**, on all three room pages. You confirmed
    **every room has a private bathroom with a bath**, so this is now stated in
    the facility lists, the photo captions and the structured data. More
    bathroom photos (per room type) are still welcome for variety.
11. ~~A true single room~~ **Added 2026-07-30** (room 20) — single, double and
    triple pages plus the home/overview cards now all use your new photos.
    Note: one double-room photo was left out because the ceiling shows a
    water stain; worth a touch-up before re-shooting that room.
12. Reception / entrance interior.
13. Facade at dusk with the gold lettering lit.
14. ~~Video hero~~ **Decided 2026-07-30:** we compared a video hero (your
    Beestenmarkt market clip) against the facade photo and kept the **photo
    hero** — it shows guests the building they need to find. The preview page
    and hero video files have been removed. 18 room/market clips remain
    unused in your local `nieuwe foto's` folder if we ever want a room-video
    section.

## Hosting & domain (when you're ready to go live)

15. **Preview is live** (since 2026-07-27) at
    https://leroy-png.github.io/hotel-mayflower-website/ — every push to
    `main` redeploys automatically. **Production route (cPanel):** every push
    also builds a clean production copy on the `production` branch (site
    files only, cache-busted assets, `.cpanel.yml` included). In cPanel:
    Git Version Control → Create → clone
    `https://github.com/leroy-png/hotel-mayflower-website.git` to a
    repository path outside public_html, checked-out branch `production`,
    then Pull or Deploy → Deploy HEAD Commit copies the site to
    `~/public_html/hotel` (test subdomain hotel.themayflower.nl). For the
    real go-live, change DEPLOYPATH in `.cpanel.yml` (or add a second task)
    once the hotelmayflower.nl domain is transferred to the server.
16. Submit `sitemap.xml` in Google Search Console; claim/refresh the Google
    Business Profile so Maps shows the new site.
17. After launch, verify the booking deep-link opens with dates prefilled from
    the live domain (it did from the test environment: dates, language AND
    guest count all carry through).
18. **Booking-engine photos look wrong.** The room photo shown on
    direct-book.com (dated furnishing, mountain artwork) does not appear to be
    this hotel. Review and replace the property photos inside SiteMinder — the
    new website sends guests there, so the mismatch will be noticed.

## Verified during build (no action needed)

- Booking engine is SiteMinder "The Booking Button"; deep links use
  `checkInDate` / `checkOutDate` / `locale` / `currency` (confirmed in the
  engine's own code). Guest count cannot be passed via URL — visitors pick
  occupancy on the engine page.
- No false amenity claims: the old site's "Delicious Breakfast", "Room Service"
  and "Bike Rentals" claims are gone; audit script: `tools/audit.sh`.
- Wi-Fi network name/password are deliberately **not** published on the site.
