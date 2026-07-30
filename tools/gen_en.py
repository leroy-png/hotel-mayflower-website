# English pages — Hotel Mayflower. Run: python3 tools/gen_en.py
from _shared import write_page, picture, BOOK, DOMAIN


def crumbs(*items):
    lis = []
    for i, (label, url) in enumerate(items):
        if url:
            lis.append(f'<li><a href="{url}">{label}</a></li>')
        else:
            lis.append(f'<li aria-current="page">{label}</li>')
    return ('<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>'
            + "".join(lis) + "</ol></nav>")


def crumb_ld(*items):
    els = ",\n    ".join(
        f'{{ "@type": "ListItem", "position": {i+1}, "name": "{label}", "item": "{DOMAIN}{url}" }}'
        for i, (label, url) in enumerate(items))
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {els}
  ]
}}
</script>
"""


def room_ld(name, occupancy, path, desc):
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HotelRoom",
  "name": "{name}",
  "description": "{desc}",
  "url": "{DOMAIN}{path}",
  "occupancy": {{ "@type": "QuantitativeValue", "maxValue": {occupancy} }},
  "amenityFeature": [
    {{ "@type": "LocationFeatureSpecification", "name": "Private bathroom", "value": true }},
    {{ "@type": "LocationFeatureSpecification", "name": "Free Wi-Fi", "value": true }},
    {{ "@type": "LocationFeatureSpecification", "name": "Television", "value": true }},
    {{ "@type": "LocationFeatureSpecification", "name": "Tea and coffee facilities", "value": true }}
  ],
  "containedInPlace": {{ "@type": "Hotel", "name": "Hotel Mayflower", "url": "{DOMAIN}/en/" }}
}}
</script>
"""


ROOM_FACTS = """<ul class="card-meta" style="font-size:1rem;gap:.6rem 1.4rem">
  <li>✓ Private bathroom</li>
  <li>✓ Free Wi-Fi</li>
  <li>✓ Television</li>
  <li>✓ Tea &amp; coffee facilities</li>
  <li>✓ Fresh linen &amp; towels</li>
</ul>"""

STAIRS_NOTE = """<div class="notice">
  <strong>Historic building, stairs only.</strong> Our building does not have an elevator; all rooms are reached by stairs. If stairs are difficult for you, please <a href="/en/contact/">contact us</a> before booking so we can think along with you.
</div>"""

VARY_NOTE = """<p class="booking-note">Photos show a selection of our rooms. Views, balconies and exact layouts differ per room and depend on availability. On warm days a portable air cooler is provided. Please note that this is an air cooler, not air conditioning.</p>"""


def room_page(slug, name, kicker, occupancy, intro, paras, gallery, nl_slug):
    path = f"/en/rooms/{slug}/"
    alt = f"/nl/kamers/{nl_slug}/"
    figs = "\n".join(
        f'<figure class="reveal{" wide" if i == 0 else ""}>{picture(n, a, sizes="(min-width: 700px) 46vw, 92vw" if i == 0 else "(min-width: 700px) 30vw, 92vw")}<figcaption>{a}</figcaption></figure>'
        for i, (n, a) in enumerate(gallery))
    body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/en/"), ("Rooms", "/en/rooms/"), (name, None))}
      <p class="eyebrow">{kicker}</p>
      <h1>{name}</h1>
      <p class="lede">{intro}</p>
    </div>
  </div>

  <section class="section" style="padding-top:0">
    <div class="container gallery">
{figs}
    </div>
  </section>

  <section class="section section--tint">
    <div class="container split">
      <div class="reveal">
        <h2>What you can count on</h2>
        {ROOM_FACTS}
        {"".join(f"<p>{p}</p>" for p in paras)}
        {STAIRS_NOTE}
        {VARY_NOTE}
      </div>
      <div class="reveal reveal-d1">
        <div class="booking-bar" style="grid-template-columns:1fr">
          <h3 style="margin:0">Ready when you are</h3>
          <p style="color:var(--muted);margin:0">Live rates and availability on our secure booking page. Booking direct always gets you the best price.</p>
          <a class="btn btn-gold" href="{BOOK}" rel="noopener">Book this room</a>
          <a class="btn btn-ghost" href="/en/rooms/">Compare all rooms</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    jsonld = crumb_ld(("Home", "/en/"), ("Rooms", "/en/rooms/"), (name, path)) + room_ld(name, occupancy, path, intro)
    write_page("en", f"en/rooms/{slug}/index.html",
               f"{name} | Hotel Mayflower Leiden",
               intro, "/en/rooms/", path, alt, body, jsonld)


# ---------------- Room pages ----------------
room_page(
    "single", "Single Room", "Sleeps one · Quiet and compact", 1,
    "A compact, quiet room for the solo traveller: a comfortable bed, a private bathroom and the whole of Leiden outside the front door.",
    ["Travelling alone for work, study or a city break? Our single rooms keep it simple: everything you need for a good night, nothing that gets in the way. Drop your bag, make a cup of tea and head out: Leiden Central Station, the museums and the old centre are all within a short walk.",
     "Some rooms look out over the rooftops of the old town; every one of them comes with the same quiet comfort."],
    [("room-single-overview", "Bright single room with bed, desk and window"),
     ("room-single-bed", "A comfortable bed by the window"),
     ("room-single-desk", "Desk with tea and coffee facilities and a television")],
    "eenpersoonskamer")

room_page(
    "double", "Double Room", "Sleeps two · Our most-booked room", 2,
    "Characterful double rooms in a historic building: some with a view over the lively Beestenmarkt, some with a balcony, all with a private bathroom.",
    ["Our doubles are the heart of the hotel: comfortable rooms for two with a seating corner here, sloping beams there, and in the front rooms a grandstand view of the liveliest square in Leiden.",
     "Perfect for a weekend of museums and canal-side dinners, or as a friendly base between Amsterdam, The Hague and the coast."],
    [("room-double-overview", "Renovated double room with bed, desk and seating corner"),
     ("room-double-window-seating", "Window seating with a view over the square"),
     ("room-double-attic", "Attic double room under the sloping white beams"),
     ("room-double-twin", "Some double rooms have two separate beds")],
    "tweepersoonskamer")

room_page(
    "triple", "Triple Room", "Sleeps three · Family favourite", 3,
    "Room for three: three proper beds, a private bathroom and space to spread out. Ideal for friends or a small family exploring Leiden together.",
    ["No sofa beds or squeezing in: our triple rooms have three full beds, so everyone wakes up on the right side. Between the station, the square and the museums you will hardly need public transport all weekend.",
     "Several triple rooms have been freshly renovated; ask us about the current options when you book."],
    [("room-triple-renovated", "Freshly renovated triple room with three beds"),
     ("room-triple-beds", "Triple room with three single beds"),
     ("room-bathroom-tub", "A private bathroom, with fresh towels")],
    "driepersoonskamer")


# ---------------- Leiden & location ----------------
leiden_tiles = [
    ("± 5 min walk", "Leiden Central Station", "Direct trains to Amsterdam (35 min), Schiphol (20 min), The Hague and Rotterdam."),
    ("± 4 min walk", "Museum De Lakenhal", "Fine art and the story of Leiden's cloth trade, including the young Rembrandt."),
    ("± 5 min walk", "Museum Volkenkunde", "One of Europe's oldest ethnographic museums, on the Steenstraat."),
    ("± 10 min walk", "Rijksmuseum van Oudheden", "The national antiquities museum: Egypt, the classical world and Dutch archaeology."),
    ("At the door", "Canals &amp; boat tours", "Rondvaart boats and sloop rental leave from the water right by the square."),
    ("± 3 min walk", "Haarlemmerstraat", "Leiden's main shopping street, with the Nieuwe Rijn market on Wednesdays and Saturdays."),
    ("± 10 min walk", "Pieterskerk quarter", "Atmospheric lanes, independent shops and the church of the Pilgrims."),
    ("± 12 min walk", "Hortus botanicus", "The Netherlands' oldest botanical garden, at the heart of the university quarter."),
]
tiles_html = "\n".join(
    f"""        <div class="tile reveal"><span class="walk">{w}</span><h3>{t}</h3><p>{d}</p></div>"""
    for w, t, d in leiden_tiles)

leiden_body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/en/"), ("Leiden", None))}
      <p class="eyebrow">Leiden &amp; location</p>
      <h1>City of Discoveries, on foot</h1>
      <p class="lede">Hotel Mayflower stands on the Beestenmarkt, where the old city begins. Museums, canals, shopping streets and the station: everything is within walking distance.</p>
    </div>
  </div>

  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="grid grid-4">
{tiles_html}
      </div>
    </div>
  </section>

  <section class="section section--tint">
    <div class="container split">
      <div class="reveal">
        <p class="eyebrow">Why Leiden</p>
        <h2>Rembrandt's cradle, the Pilgrims' harbour</h2>
        <p class="sub-italic">Small enough to walk, rich enough to fill a week.</p>
        <p>Leiden wears its history lightly: thirteen museums, the country's oldest university, windmills over the canals and courtyards (hofjes) hiding behind ordinary front doors. Rent a boat, join a guided city walk, or follow the Singelpark, a six-kilometre green loop around the old centre.</p>
        <p>On Wednesdays and Saturdays the market takes over the Nieuwe Rijn quays, five minutes from your room. And when the museums close, the Beestenmarkt itself becomes the destination: terraces, restaurants and evening light on the water.</p>
        <p style="font-size:.9rem;color:var(--faint)">Tip: see <a href="https://www.visitleiden.nl/en" rel="noopener">visitleiden.nl</a> for exhibitions and events during your stay. Attractions listed here are recommendations for your visit; opening hours and programmes are set by the venues themselves.</p>
      </div>
      <div class="split-media portrait reveal reveal-d1">
        {picture("view-beestenmarkt", "View over the Beestenmarkt square and canal boats", sizes="(min-width: 900px) 44vw, 92vw", widths=(480, 960, 1600))}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="center reveal">
        <p class="eyebrow">Find us</p>
        <h2>Beestenmarkt 2, Leiden</h2>
        <p class="lede">From Leiden Central Station: leave on the centre side, follow Stationsweg straight towards the city, and after about five minutes the square opens up in front of you. We are on the far side, next to the white HOTEL entrance.</p>
      </div>
      <div class="map-embed reveal" data-map-title="Map showing Hotel Mayflower, Beestenmarkt 2, Leiden" style="margin-top:2.4rem">
        <div class="map-consent">
          <svg class="pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/></svg>
          <p>The interactive map is loaded from Google Maps. Click to allow it.</p>
          <button class="btn btn-gold" type="button">Show map</button>
        </div>
      </div>
      <p class="center" style="margin-top:1.4rem"><a href="https://maps.google.com/?q=Hotel+Mayflower,+Beestenmarkt+2,+Leiden" rel="noopener">Open in Google Maps</a></p>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="cta-band reveal">
        <h2>Sleep where Leiden happens</h2>
        <p class="lede">Wake up on the Beestenmarkt and have the city to yourself before the day-trippers arrive.</p>
        <div class="hero-cta" style="justify-content:center">
          <a class="btn btn-gold" href="{BOOK}" rel="noopener">Book your stay</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
write_page("en", "en/leiden/index.html",
           "Leiden & Location | Hotel Mayflower, Beestenmarkt 2",
           "Hotel Mayflower stands in the heart of Leiden: five minutes' walk from Leiden Central Station and close to De Lakenhal, Volkenkunde, the Rijksmuseum van Oudheden and the canals.",
           "/en/leiden/", "/en/leiden/", "/nl/leiden/", leiden_body,
           crumb_ld(("Home", "/en/"), ("Leiden", "/en/leiden/")))


# ---------------- Hotel information ----------------
info_body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/en/"), ("Hotel information", None))}
      <p class="eyebrow">Practical</p>
      <h1>Hotel information</h1>
      <p class="lede">Everything worth knowing before you arrive, honestly and in one place. Questions? Call <a href="tel:+31715142641">+31 71 514 2641</a> or email <a href="mailto:info@hotelmayflower.nl">info@hotelmayflower.nl</a>.</p>
    </div>
  </div>

  <section class="section" style="padding-top:0">
    <div class="container grid grid-2">
      <div class="tile reveal">
        <h3>Check-in</h3>
        <p>Check-in is from <strong>15:00 to 18:00</strong>. Our reception is open from <strong>09:00 to 18:00</strong>. Arriving earlier in the day? You are welcome: your room is ready from 15:00, and until then you can leave your luggage with us at the reception.</p>
      </div>
      <div class="tile reveal reveal-d1">
        <h3>Arriving after 18:00</h3>
        <p>No problem, as long as we know in advance: we place your key in our key locker so you can let yourself in at any hour. Please call or email us before your arrival day to arrange this. Once you have your key, you can come and go around the clock; the hotel is accessible to guests 24/7.</p>
      </div>
      <div class="tile reveal">
        <h3>Check-out</h3>
        <p>Check-out is by <strong>10:30</strong>. Later train or flight? You can leave your luggage at the reception between 09:00 and 18:00 (at your own risk) and enjoy a last stroll through Leiden.</p>
      </div>
      <div class="tile reveal reveal-d1">
        <h3>Payments</h3>
        <p>We accept <strong>card payments only</strong> (debit and credit cards). Cash is not accepted at the hotel.</p>
      </div>
      <div class="tile reveal">
        <h3>Breakfast</h3>
        <p>Hotel Mayflower is currently unable to serve breakfast while renovation works are ongoing. You will find several cafés and breakfast spots within a short walk; see our tips below. If breakfast was included in your booking or paid in advance, the amount is of course refunded.</p>
      </div>
      <div class="tile reveal reveal-d1">
        <h3>No elevator</h3>
        <p>Please note that our historic building does not have an elevator. All guest rooms are reached by stairs. If stairs are difficult for you, contact us before booking and we will think along with you.</p>
      </div>
      <div class="tile reveal">
        <h3>Pets</h3>
        <p>Pets are not permitted at Hotel Mayflower.</p>
      </div>
      <div class="tile reveal reveal-d1">
        <h3>Smoking</h3>
        <p>All rooms and indoor areas are non-smoking.</p>
      </div>
      <div class="tile reveal">
        <h3>Wi-Fi</h3>
        <p>Free Wi-Fi throughout the hotel. You will receive the network details at check-in.</p>
      </div>
      <div class="tile reveal reveal-d1">
        <h3>Warm days</h3>
        <p>Rooms are equipped with a portable air cooler in the warmer months, with ice packs for extra cooling. Please note: this is an air cooler with fan and water evaporation, not air conditioning.</p>
      </div>
    </div>
  </section>

  <section class="section section--tint">
    <div class="container">
      <div class="reveal">
        <p class="eyebrow">Breakfast nearby</p>
        <h2>Four good mornings, minutes away</h2>
      </div>
      <div class="table-wrap reveal" style="margin-top:1.8rem">
        <table class="info-table">
          <thead><tr><th scope="col">Spot</th><th scope="col">Address</th><th scope="col">Open</th></tr></thead>
          <tbody>
            <tr><td>Tootje</td><td>Haarlemmerstraat 2</td><td>Mon–Fri 08:00–18:00 · Sat–Sun 10:00–17:00</td></tr>
            <tr><td>Leidsch Beleg</td><td>Turfmarkt 12</td><td>Mon–Sat 09:00–17:00 · Sun 10:00–17:00</td></tr>
            <tr><td>De Bruine Boon</td><td>Stationsweg 1</td><td>Daily 09:00–22:00</td></tr>
            <tr><td>Ibis Hotel</td><td>Stationsplein 240–242</td><td>Mon–Fri 06:30–10:00 · Sat–Sun 06:30–11:00</td></tr>
          </tbody>
        </table>
      </div>
      <p class="booking-note">Opening hours are set by the venues and may change.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="reveal">
        <p class="eyebrow">Parking</p>
        <h2>Leiden is a walking city, so park at the edge</h2>
        <p class="lede">The hotel has no private parking, and the old centre was never built for cars. These public options work well:</p>
      </div>
      <div class="table-wrap reveal" style="margin-top:1.8rem">
        <table class="info-table">
          <thead><tr><th scope="col">Parking</th><th scope="col">Address</th><th scope="col">From the hotel</th><th scope="col">Good to know</th></tr></thead>
          <tbody>
            <tr><td>Stadsparkeerplan Haagweg</td><td>Haagweg 8</td><td>Free shuttle bus to the door</td><td>Cheapest for longer stays; the shuttle drops you at the hotel. Open 24 h.</td></tr>
            <tr><td>Parkeergarage Lammermarkt</td><td>Lammermarkt 20</td><td>± 3 min walk</td><td>Closest garage, under the De Valk windmill.</td></tr>
            <tr><td>Parkeergarage Morspoort</td><td>Bloemfonteinstraat 2</td><td>± 5 min walk</td><td>24 h in-and-out; EV charging available.</td></tr>
            <tr><td>Parkeerterrein Morssingel</td><td>Morssingel 179</td><td>± 5 min walk</td><td>Open-air, next to the station.</td></tr>
          </tbody>
        </table>
      </div>
      <p class="booking-note">Tariffs are set by the operators and change from time to time; check current rates at <a href="https://www.parkeren-leiden.nl" rel="noopener">parkeren-leiden.nl</a>. On-street parking in the centre is paid and scarce; we recommend the garages.</p>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="cta-band reveal">
        <h2>Anything we didn't answer?</h2>
        <p class="lede">Check the FAQ, or simply call or write. We respond quickly.</p>
        <div class="hero-cta" style="justify-content:center">
          <a class="btn btn-gold" href="/en/faq/">Read the FAQ</a>
          <a class="btn btn-ghost" style="color:#F7F1E4;border-color:rgba(247,241,228,.35)" href="/en/contact/">Contact us</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
write_page("en", "en/hotel-information/index.html",
           "Hotel Information: Check-in, Parking & Practical Details | Hotel Mayflower Leiden",
           "Check-in from 15:00, late arrival by key locker, card payments only, no elevator, parking options and everything else worth knowing before your stay at Hotel Mayflower Leiden.",
           "/en/hotel-information/", "/en/hotel-information/", "/nl/hotelinformatie/", info_body,
           crumb_ld(("Home", "/en/"), ("Hotel information", "/en/hotel-information/")))


# ---------------- Contact ----------------
contact_body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/en/"), ("Contact", None))}
      <p class="eyebrow">Contact</p>
      <h1>We're happy to hear from you</h1>
      <p class="lede">A question about your stay, a special request, or help planning your visit? Call, email or use the form below.</p>
    </div>
  </div>

  <section class="section" style="padding-top:0">
    <div class="container split">
      <div class="reveal">
        <form id="contact-form" class="form" novalidate>
          <div class="form-row">
            <div>
              <label for="cf-name">Your name</label>
              <input id="cf-name" name="name" type="text" autocomplete="name" required>
            </div>
            <div>
              <label for="cf-email">Email address</label>
              <input id="cf-email" name="email" type="email" autocomplete="email" required>
            </div>
          </div>
          <div class="form-row">
            <div>
              <label for="cf-arrival">Arrival date (optional)</label>
              <input id="cf-arrival" name="arrival" type="date">
            </div>
            <div>
              <label for="cf-nights">Nights (optional)</label>
              <input id="cf-nights" name="nights" type="number" min="1" max="30">
            </div>
          </div>
          <div>
            <label for="cf-message">Your message</label>
            <textarea id="cf-message" name="message" required></textarea>
          </div>
          <p style="position:absolute;left:-9999px" aria-hidden="true"><label>Leave this field empty<input type="text" name="website" tabindex="-1" autocomplete="off"></label></p>
          <p class="form-status" role="status"></p>
          <button class="btn btn-gold" type="submit">Send message</button>
          <p class="hint">We reply within one working day. For availability and prices, our <a href="{BOOK}" rel="noopener">booking page</a> is always up to date.</p>
        </form>
      </div>
      <div class="reveal reveal-d1">
        <div class="tile" style="margin-bottom:1rem">
          <h3>Hotel Mayflower</h3>
          <p>Beestenmarkt 2<br>2312 CC Leiden<br>The Netherlands</p>
          <p><a href="tel:+31715142641">+31 71 514 2641</a><br>
          <a href="mailto:info@hotelmayflower.nl">info@hotelmayflower.nl</a></p>
          <p>Reception open 09:00–18:00 · guests have 24/7 access with their own key.</p>
        </div>
        <div class="tile">
          <h3>From Leiden Central Station</h3>
          <p>Leave the station on the centre side and follow Stationsweg straight ahead. Cross the water, and after about five minutes you walk onto the Beestenmarkt. The hotel entrance is on the square.</p>
          <p style="margin-top:.6rem"><strong>Arriving after 18:00?</strong> Arrange the key locker with us in advance and let yourself in whenever you land.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="map-embed reveal" data-map-title="Map showing Hotel Mayflower, Beestenmarkt 2, Leiden">
        <div class="map-consent">
          <svg class="pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/></svg>
          <p>The interactive map is loaded from Google Maps. Click to allow it.</p>
          <button class="btn btn-gold" type="button">Show map</button>
        </div>
      </div>
    </div>
  </section>
</main>
"""
write_page("en", "en/contact/index.html",
           "Contact | Hotel Mayflower Leiden, Beestenmarkt 2",
           "Contact Hotel Mayflower in Leiden: +31 71 514 2641, info@hotelmayflower.nl, Beestenmarkt 2. Directions from Leiden Central Station and arrival information.",
           "/en/contact/", "/en/contact/", "/nl/contact/", contact_body,
           crumb_ld(("Home", "/en/"), ("Contact", "/en/contact/")))


# ---------------- FAQ ----------------
faqs = [
    ("Does the hotel serve breakfast?",
     "Not at the moment. Breakfast is temporarily unavailable while renovation works are ongoing. There are several excellent cafés and breakfast spots within a short walk of the hotel; you will find our favourites on the hotel information page. If breakfast was included in your booking or paid in advance, the amount is refunded."),
    ("What time is check-in?",
     "Check-in is from 15:00 to 18:00. You are welcome to arrive earlier: your room is ready from 15:00, and until then you can leave your luggage with us at the reception."),
    ("Can I arrive after 18:00?",
     "Yes. Let us know in advance and we place your key in our key locker, so you can let yourself in at any hour. Call or email us before your arrival day to arrange it. With your key you have 24/7 access to the hotel throughout your stay."),
    ("What time is check-out?",
     "Check-out is by 10:30. You are welcome to leave your luggage at the reception afterwards, between 09:00 and 18:00."),
    ("Does the hotel have an elevator?",
     "No. Our historic building does not have an elevator; all rooms are reached by stairs. If stairs are difficult for you, please contact us before booking."),
    ("Are pets permitted?",
     "No, pets are not permitted at Hotel Mayflower."),
    ("Is parking available?",
     "The hotel has no private parking. Good public options nearby: the Lammermarkt garage (± 3 minutes' walk), the Morspoort garage and the Morssingel car park (both ± 5 minutes), or the budget-friendly Haagweg site with its free shuttle bus that stops near the hotel."),
    ("Which payment methods are accepted?",
     "We accept card payments only (debit and credit cards). Cash is not accepted."),
    ("How far is the hotel from Leiden Central Station?",
     "About five minutes on foot. Leave the station on the centre side, follow Stationsweg towards the city, and you will walk straight onto the Beestenmarkt."),
    ("Can I leave my luggage before check-in?",
     "Yes. You can leave your luggage at the reception between 09:00 and 18:00, at your own risk. That way you can start exploring Leiden straight away."),
    ("Which room types are available?",
     "We offer single, double and triple rooms, each with a private bathroom, free Wi-Fi, a television and tea &amp; coffee facilities. Views and balconies vary per room and depend on availability."),
]
faq_items = "\n".join(
    f"""        <details class="faq-item"><summary>{q}</summary><div class="faq-a"><p>{a}</p></div></details>"""
    for q, a in faqs)
faq_ld_items = ",\n    ".join(
    f'{{ "@type": "Question", "name": "{q}", "acceptedAnswer": {{ "@type": "Answer", "text": "{a.replace(chr(34), chr(39))}" }} }}'
    for q, a in faqs)
faq_jsonld = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {faq_ld_items}
  ]
}}
</script>
"""
faq_body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/en/"), ("FAQ", None))}
      <p class="eyebrow">Questions &amp; answers</p>
      <h1>Frequently asked questions</h1>
      <p class="lede">The short, honest answers. Anything missing? <a href="/en/contact/">Ask us directly</a>; we respond quickly.</p>
    </div>
  </div>
  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="faq-list reveal">
{faq_items}
      </div>
      <div class="center" style="margin-top:2.6rem">
        <a class="btn btn-gold" href="{BOOK}" rel="noopener">Book your stay</a>
      </div>
    </div>
  </section>
</main>
"""
write_page("en", "en/faq/index.html",
           "FAQ | Hotel Mayflower Leiden",
           "Answers to frequently asked questions about Hotel Mayflower Leiden: check-in and check-out times, late arrival, breakfast, parking, payments, pets and luggage.",
           None, "/en/faq/", "/nl/veelgestelde-vragen/", faq_body,
           crumb_ld(("Home", "/en/"), ("FAQ", "/en/faq/")) + faq_jsonld)


# ---------------- Privacy & cookies ----------------
privacy_body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/en/"), ("Privacy & cookies", None))}
      <p class="eyebrow">Legal</p>
      <h1>Privacy &amp; cookie policy</h1>
      <p class="lede">The short version: this website tracks as little as technically possible, and we only process your data to host your stay.</p>
    </div>
  </div>
  <section class="section" style="padding-top:0">
    <div class="container" style="max-width:46rem">
      <h2>Who we are</h2>
      <p>Hotel Mayflower, Beestenmarkt 2, 2312 CC Leiden, the Netherlands, is the controller for the personal data described here. Contact: <a href="mailto:info@hotelmayflower.nl">info@hotelmayflower.nl</a>, +31 71 514 2641.</p>

      <h2>What this website stores</h2>
      <p>This website sets <strong>no tracking or advertising cookies</strong> and uses no analytics services. It stores a few functional preferences in your browser's local storage, on your own device only: your chosen theme (dark or light), your language, whether you allowed the map, and whether you dismissed the cookie notice. These values never leave your device.</p>

      <h2>The map</h2>
      <p>The interactive map on the location and contact pages is loaded from Google Maps <em>only after you allow it</em>. From that moment Google may process your IP address and set its own cookies; see <a href="https://policies.google.com/privacy" rel="noopener">Google's privacy policy</a>. If you do not allow the map, nothing is loaded from Google.</p>

      <h2>Booking</h2>
      <p>Bookings are handled on our booking page, operated by SiteMinder (The Booking Button). The data you enter there (name, contact details, stay dates, payment details) is processed to conclude and administer your reservation. Payment details are handled by the booking platform and its payment providers; this website itself never receives or stores them.</p>

      <h2>Contact</h2>
      <p>If you email us or use the contact form, we use your details solely to answer you. We keep correspondence no longer than necessary for that purpose and for our administration.</p>

      <h2>Your rights</h2>
      <p>Under the GDPR you may request access to, correction or deletion of your personal data, and you may object to or restrict processing. Email <a href="mailto:info@hotelmayflower.nl">info@hotelmayflower.nl</a>. You can also lodge a complaint with the Dutch Data Protection Authority (Autoriteit Persoonsgegevens).</p>

      <p class="booking-note">Last updated: July 2026.</p>
    </div>
  </section>
</main>
"""
write_page("en", "en/privacy/index.html",
           "Privacy & Cookie Policy | Hotel Mayflower Leiden",
           "How Hotel Mayflower Leiden handles your data: no tracking cookies, functional preferences only, consent-based map loading and GDPR rights.",
           None, "/en/privacy/", "/nl/privacy/", privacy_body,
           crumb_ld(("Home", "/en/"), ("Privacy & cookies", "/en/privacy/")))


# ---------------- Terms ----------------
terms_body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/en/"), ("Terms & conditions", None))}
      <p class="eyebrow">Legal</p>
      <h1>Terms &amp; conditions</h1>
      <p class="lede">The house agreements that keep the hotel pleasant for everyone.</p>
    </div>
  </div>
  <section class="section" style="padding-top:0">
    <div class="container" style="max-width:46rem">
      <h2>Bookings and payment</h2>
      <p>Reservations are made through our booking page and are subject to the rate conditions shown there at the time of booking, including the applicable cancellation policy. We accept card payments only; cash is not accepted at the hotel.</p>

      <h2>Arrival and departure</h2>
      <p>Check-in is from 15:00 to 18:00; arrival after 18:00 is possible via our key locker if arranged in advance. Check-out is by 10:30. Hotel keys remain the property of the hotel; please hand them in at departure.</p>

      <h2>House rules</h2>
      <ul>
        <li>All rooms and indoor areas are non-smoking. A cleaning fee applies if this rule is broken.</li>
        <li>Pets are not permitted.</li>
        <li>Please respect the night's rest of other guests and our neighbours.</li>
        <li>Instructions of hotel staff, given in the interest of safety and good order, must be followed.</li>
        <li>The use or possession of drugs and the carrying of weapons are prohibited. Violation leads to removal and, where appropriate, notification of the police.</li>
      </ul>

      <h2>Liability</h2>
      <p>The hotel accepts no liability for loss of or damage to guests' property, except where required by mandatory Dutch law. Damage to hotel property caused by a guest will be charged. Furniture and other hotel property must remain in the hotel.</p>

      <h2>Applicable law</h2>
      <p>Dutch law applies to all agreements with Hotel Mayflower. In addition, the Uniform Conditions for the Hotel and Catering Industry (Uniforme Voorwaarden Horeca) may apply to hotel accommodation agreements in the Netherlands.</p>

      <p class="booking-note">Last updated: July 2026.</p>
    </div>
  </section>
</main>
"""
write_page("en", "en/terms/index.html",
           "Terms & Conditions | Hotel Mayflower Leiden",
           "Booking conditions and house rules of Hotel Mayflower Leiden: payment, arrival and departure, non-smoking policy and liability.",
           None, "/en/terms/", "/nl/voorwaarden/", terms_body,
           crumb_ld(("Home", "/en/"), ("Terms & conditions", "/en/terms/")))

print("EN pages done.")
