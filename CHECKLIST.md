# Launch checklist — items needing confirmation or delivery

Deliverable 13 from the design brief: everything that is missing, unconfirmed,
or intentionally left out, in priority order.

## Blocking questions (answer before/at launch)

1. **Reception staffed hours.** Your documents conflict: the welcome letter says
   07:00–21:00, the printed room guide says 09:00–18:00. The site currently
   avoids naming reception hours (it says "during staffed hours" for luggage).
   Confirm the real hours and I add them to Hotel information + Contact.
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
8. **Contact-form endpoint** — form falls back to the visitor's email app until
   you create a form service account (2 minutes, see CONTENT-GUIDE.md).
9. **Terrace** — photos excluded on your instruction (not presentable yet). When
   ready: shoot 2–3 photos, confirm whether smoking is allowed there, and it gets
   a section on Home + Hotel information.

## Photo wishlist (site works, but these would lift it)

10. Bathroom (none supplied — rooms pages currently show no bathroom photo).
11. A true single room.
12. Reception / entrance interior.
13. Facade at dusk with the gold lettering lit.
14. Optional: Higgsfield cinemagraph from the hero photo for extra hero motion —
    slot and poster structure are ready (`.hero-media` swaps image for video).

## Hosting & domain (when you're ready to go live)

15. Choose a static host (Netlify / Cloudflare Pages recommended), point the
    hotelmayflower.nl DNS at it, deploy this folder.
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
