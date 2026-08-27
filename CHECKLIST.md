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
4. ~~Geo-coordinates~~ **Fixed 2026-08-04** with the exact Google pin
   (52.1628825, 4.4848159).
5. **Breakfast timeline.** Copy says "temporarily unavailable due to renovation
   works". When breakfast returns (or is discontinued permanently), the texts on
   Home, Hotel information and FAQ need one-line updates — in both languages.

## Missing content (site has prepared slots)

6. ~~Guest reviews~~ **Live 2026-08-04.** Built honestly around what is
   verifiable: Google's 4.7/5 location score, two genuine 5-star Google quotes
   (Joran, Piet; punctuation normalised, wording untouched; EN shows marked
   translations), and a "new chapter since May 2026" card linking to all
   reviews on Google. No overall-score claim: the profile shows 3.6, weighed
   down by pre-2026 reviews of the previous owners.
7. ~~Social media~~ **Instagram in the footer since 2026-08-04**
   (instagram.com/hotel_mayflower). Send other profiles if they exist.
8. ~~Contact form~~ **Working since 2026-08-01, confirmed by Leroy 2026-08-04.**
   Historical notes:
   Messages were not arriving because (a) cPanel treats hotelmayflower.nl as a
   *local* mail domain, so mail to info@ never reaches Office 365, and (b) the
   SPF record ends in `-all` and does not list the web server, so Microsoft
   rejects mail sent from it. Fix: cPanel → Email Routing → set
   hotelmayflower.nl to **Remote Mail Exchanger**, and create
   `/home/themayflower/mayflower-mail-config.php` from `mail-config.sample.php`
   with the SMTP2GO credentials. Every submission is now also stored in
   `/home/themayflower/contact-messages/YYYY-MM.jsonl`, so nothing is lost even
   if mail fails. Test with `/contact.php?selftest=<token>`.
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
17. ~~SiteMinder deep-link check~~ **Superseded 2026-08-27:** the booking
    engine switched to Noovy (mayflower.book.noovy.com). All booking links
    and the booking bar now open Noovy in the visitor's language
    (?lng=nl-NL / en-GB — verified working). **Noovy accepts no date or
    guest URL parameters** (confirmed in its router code: only
    `bookingStep` exists), so the booking bar no longer prefills dates.
    Worth asking Noovy support whether a date deep-link parameter exists
    or is planned; if they add one, wiring it in is a two-line change.
18. ~~SiteMinder property photos~~ **Superseded by the Noovy switch** — the
    site no longer links to direct-book.com. Check instead that the room
    photos inside the Noovy engine are your real, current photos.


## Google Business Profile (found while fetching reviews, 2026-08-04)

19. **Wrong amenities on Google.** The profile lists Zwembad, Ontbijt,
    Parkeren, Airconditioning and Rolstoeltoegankelijk — none of which the
    hotel offers. This is the never-claim list, live on Google. Fix in the
    Business Profile (Bewerken → Voorzieningen).
20. **Check-in time on Google says 11:30**; the real window is 15:00-18:00.
21. **Owner-account review.** There is an unpublished review of the hotel
    from your own Google account; Google does not allow owner reviews, so
    it is best deleted.

## Verified during build (no action needed)

- Booking engine is SiteMinder "The Booking Button"; deep links use
  `checkInDate` / `checkOutDate` / `locale` / `currency` (confirmed in the
  engine's own code). Guest count cannot be passed via URL — visitors pick
  occupancy on the engine page.
- No false amenity claims: the old site's "Delicious Breakfast", "Room Service"
  and "Bike Rentals" claims are gone; audit script: `tools/audit.sh`.
- Wi-Fi network name/password are deliberately **not** published on the site.
