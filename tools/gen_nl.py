# Nederlandse pagina's — Hotel Mayflower. Run: python3 tools/gen_nl.py
from _shared import write_page, picture, BOOK, DOMAIN


def crumbs(*items):
    lis = []
    for label, url in items:
        if url:
            lis.append(f'<li><a href="{url}">{label}</a></li>')
        else:
            lis.append(f'<li aria-current="page">{label}</li>')
    return ('<nav class="breadcrumbs" aria-label="Kruimelpad"><ol>'
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


# ---------------- Home (NL) ----------------
hotel_ld = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Hotel",
  "name": "Hotel Mayflower",
  "url": "{DOMAIN}/",
  "image": "{DOMAIN}/assets/img/og-hotel-mayflower.jpg",
  "logo": "{DOMAIN}/assets/logo/beeldmerk_gold.svg",
  "starRating": {{ "@type": "Rating", "ratingValue": "2" }},
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Beestenmarkt 2",
    "postalCode": "2312 CC",
    "addressLocality": "Leiden",
    "addressCountry": "NL"
  }},
  "geo": {{ "@type": "GeoCoordinates", "latitude": 52.1628825, "longitude": 4.4848159 }},
  "telephone": "+31715142641",
  "email": "info@hotelmayflower.nl",
  "checkinTime": "15:00",
  "checkoutTime": "10:30",
  "petsAllowed": false,
  "paymentAccepted": "Credit card, debit card",
  "amenityFeature": [
    {{ "@type": "LocationFeatureSpecification", "name": "Gratis wifi", "value": true }},
    {{ "@type": "LocationFeatureSpecification", "name": "Eigen badkamer met ligbad", "value": true }},
    {{ "@type": "LocationFeatureSpecification", "name": "Televisie", "value": true }},
    {{ "@type": "LocationFeatureSpecification", "name": "Thee- en koffiefaciliteiten", "value": true }},
    {{ "@type": "LocationFeatureSpecification", "name": "Lift", "value": false }}
  ],
  "containsPlace": [
    {{ "@type": "HotelRoom", "name": "Eenpersoonskamer", "occupancy": {{ "@type": "QuantitativeValue", "maxValue": 1 }} }},
    {{ "@type": "HotelRoom", "name": "Tweepersoonskamer", "occupancy": {{ "@type": "QuantitativeValue", "maxValue": 2 }} }},
    {{ "@type": "HotelRoom", "name": "Driepersoonskamer", "occupancy": {{ "@type": "QuantitativeValue", "maxValue": 3 }} }}
  ]
}}
</script>
"""

home_body = f"""<main id="main">

  <section class="hero">
    <div class="hero-media" aria-hidden="true">
      {picture("exterior-beestenmarkt", "", sizes="100vw", widths=(960, 1600, 2400), lazy=False)}
    </div>
    <div class="container hero-content">
      <div class="hero-badge">
        <span class="shimmer"><img src="/assets/logo/beeldmerk_gold.svg" alt="" width="62" height="70"></span>
      </div>
      <p class="eyebrow">Hotel Mayflower · Beestenmarkt 2, Leiden <span class="stars" aria-label="Tweesterrenhotel">★★</span></p>
      <h1>Verblijf in het hart<br>van Leiden</h1>
      <p class="lede sub-italic">Een gastvrij stadshotel op loopafstand van Leiden Centraal, musea, restaurants en de historische binnenstad.</p>
      <div class="hero-cta">
        <a class="btn btn-gold" href="{BOOK}" rel="noopener">Boek uw verblijf</a>
        <a class="btn btn-ghost" href="/nl/kamers/">Bekijk onze kamers</a>
      </div>

      <form id="booking-form" class="booking-bar booking-entrance" style="margin-top:2.6rem" aria-label="Beschikbaarheid controleren">
        <div class="field">
          <label for="bk-in">Aankomst</label>
          <input id="bk-in" name="checkin" type="date" required>
        </div>
        <div class="field">
          <label for="bk-out">Vertrek</label>
          <input id="bk-out" name="checkout" type="date" required>
        </div>
        <div class="field">
          <label for="bk-guests">Gasten</label>
          <select id="bk-guests" name="guests">
            <option value="1">1 gast</option>
            <option value="2" selected>2 gasten</option>
            <option value="3">3 gasten</option>
            <option value="4">4 gasten</option>
            <option value="5">5+ gasten</option>
          </select>
        </div>
        <button class="btn btn-gold" type="submit">Bekijk beschikbaarheid</button>
      </form>
      <p class="booking-note">U rondt uw reservering af op onze beveiligde boekingspagina. Direct boeken is altijd de beste prijs.</p>
    </div>
  </section>

  <section class="section">
    <div class="container split">
      <div class="reveal">
        <p class="eyebrow">Welkom</p>
        <h2>Een gastvrije uitvalsbasis aan het gezelligste plein van de stad</h2>
        <p class="sub-italic">Historisch Leiden voor de deur, een comfortabel bed erachter.</p>
        <p>Hotel Mayflower ligt direct aan de Beestenmarkt, het levendige plein waar Leiden afspreekt voor koffie, diner en een borrel aan het water. Leiden Centraal ligt op zo'n vijf minuten lopen, en de musea, grachten en winkelstraten van de binnenstad bereikt u allemaal te voet.</p>
        <p>Wij zijn een tweesterrenhotel in een historisch Nederlands pand: eerlijk comfort, een warm welkom en een van de beste locaties van Leiden, zonder franje waar u niet om vroeg. Een aantal kamers kijkt uit over het plein, en sommige kamers hebben een balkon, afhankelijk van het kamertype.</p>
        <a class="btn btn-ghost" href="/nl/hotelinformatie/">Praktische informatie</a>
      </div>
      <div class="split-media portrait reveal reveal-d1">
        {picture("view-window-seat", "Zithoekje bij een open raam met uitzicht over de Beestenmarkt", sizes="(min-width: 900px) 44vw, 92vw", widths=(480, 960, 1600))}
      </div>
    </div>
  </section>

  <svg class="ripple-divider" viewBox="0 0 1200 60" preserveAspectRatio="none" aria-hidden="true">
    <path class="r1" d="M0 20 Q 30 12, 60 20 T 120 20 T 180 20 T 240 20 T 300 20 T 360 20 T 420 20 T 480 20 T 540 20 T 600 20 T 660 20 T 720 20 T 780 20 T 840 20 T 900 20 T 960 20 T 1020 20 T 1080 20 T 1140 20 T 1200 20"/>
    <path class="r2" d="M0 34 Q 30 26, 60 34 T 120 34 T 180 34 T 240 34 T 300 34 T 360 34 T 420 34 T 480 34 T 540 34 T 600 34 T 660 34 T 720 34 T 780 34 T 840 34 T 900 34 T 960 34 T 1020 34 T 1080 34 T 1140 34 T 1200 34"/>
    <path class="r3" d="M0 48 Q 30 40, 60 48 T 120 48 T 180 48 T 240 48 T 300 48 T 360 48 T 420 48 T 480 48 T 540 48 T 600 48 T 660 48 T 720 48 T 780 48 T 840 48 T 900 48 T 960 48 T 1020 48 T 1080 48 T 1140 48 T 1200 48"/>
  </svg>

  <section class="section" id="kamers">
    <div class="container">
      <div class="center reveal">
        <p class="eyebrow">Onze kamers</p>
        <h2>Eenvoudig, comfortabel, van u</h2>
        <p class="lede">Elke kamer heeft een eigen badkamer met ligbad, gratis wifi, een televisie en thee- en koffiefaciliteiten.</p>
      </div>
      <div class="grid grid-3" style="margin-top:3rem">
        <article class="card reveal">
          <div class="card-media">
            {picture("room-single-overview", "Lichte eenpersoonskamer met bed, bureau en raam")}
          </div>
          <div class="card-body">
            <span class="card-kicker">Voor 1 persoon</span>
            <h3>Eenpersoonskamer</h3>
            <p style="color:var(--muted);font-size:.95rem">Een compacte, rustige kamer voor wie alleen reist: alles wat u nodig heeft voor een nacht of een week Leiden.</p>
            <a class="btn btn-ghost" href="/nl/kamers/eenpersoonskamer/">Bekijk kamer</a>
          </div>
        </article>
        <article class="card reveal reveal-d1">
          <div class="card-media">
            {picture("room-double-overview", "Gerenoveerde tweepersoonskamer met bed, bureau en zithoek")}
          </div>
          <div class="card-body">
            <span class="card-kicker">Voor 2 personen</span>
            <h3>Tweepersoonskamer</h3>
            <p style="color:var(--muted);font-size:.95rem">Onze meest geboekte kamer. Karakteristieke kamers in een historisch pand, sommige met uitzicht op het plein.</p>
            <a class="btn btn-ghost" href="/nl/kamers/tweepersoonskamer/">Bekijk kamer</a>
          </div>
        </article>
        <article class="card reveal reveal-d2">
          <div class="card-media">
            {picture("room-triple-renovated", "Gerenoveerde driepersoonskamer met drie bedden")}
          </div>
          <div class="card-body">
            <span class="card-kicker">Voor 3 personen</span>
            <h3>Driepersoonskamer</h3>
            <p style="color:var(--muted);font-size:.95rem">Ruimte voor drie: ideaal voor vrienden of een klein gezin dat samen Leiden ontdekt.</p>
            <a class="btn btn-ghost" href="/nl/kamers/driepersoonskamer/">Bekijk kamer</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--tint">
    <div class="container">
      <div class="center reveal">
        <p class="eyebrow">De locatie</p>
        <h2>Alles te voet</h2>
        <p class="lede">Laat de auto staan: vanaf onze voordeur ontvouwt Leiden zich op wandeltempo.</p>
      </div>
      <div class="grid grid-4" style="margin-top:3rem">
        <div class="tile reveal">
          <span class="walk">± 5 min lopen</span>
          <h3>Leiden Centraal</h3>
          <p>Rechtstreekse treinen naar Amsterdam, Schiphol, Den Haag en Rotterdam.</p>
        </div>
        <div class="tile reveal reveal-d1">
          <span class="walk">± 5–15 min lopen</span>
          <h3>Musea van wereldklasse</h3>
          <p>De Lakenhal, Volkenkunde, het Rijksmuseum van Oudheden, Naturalis en meer.</p>
        </div>
        <div class="tile reveal reveal-d2">
          <span class="walk">Voor de deur</span>
          <h3>Grachten &amp; terrassen</h3>
          <p>De Beestenmarkt zelf, rondvaartboten en het leven aan het Leidse water.</p>
        </div>
        <div class="tile reveal reveal-d3">
          <span class="walk">± 2–10 min lopen</span>
          <h3>Winkels &amp; restaurants</h3>
          <p>Winkelen op de Haarlemmerstraat, cafés en restaurants in elke richting.</p>
        </div>
      </div>
      <div class="center reveal" style="margin-top:2.6rem">
        <a class="btn btn-ghost" href="/nl/leiden/">Ontdek Leiden</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container split flip">
      <div class="reveal">
        <p class="eyebrow">Het uitzicht vanuit uw kamer</p>
        <h2>Leiden, Stad van Ontdekkingen</h2>
        <p class="sub-italic">Musea, grachten en vier eeuwen verhalen.</p>
        <p>Rembrandt werd hier geboren, de Pilgrims vertrokken hiervandaan, en de oudste universiteit van Nederland bepaalt nog altijd het ritme van de stad. Kijk hoe beneden de markt wordt opgebouwd, stap in een sloep op de grachten of dwaal door de hofjes. Leiden beloont de nieuwsgierige bezoeker.</p>
        <p>Bij de receptie wijzen we u graag de weg naar onze favoriete plekken: de beste koffie, de mooiste wandelroutes en de musea die uw ochtend waard zijn.</p>
        <a class="btn btn-ghost" href="/nl/leiden/">Plan uw bezoek</a>
      </div>
      <div class="split-media portrait reveal reveal-d1">
        <video autoplay muted loop playsinline preload="metadata" poster="/assets/video/beestenmarkt-pan-poster.jpg" aria-label="Video: uitzicht over de Beestenmarkt vanuit een hotelkamer">
          <source src="/assets/video/beestenmarkt-pan.mp4" type="video/mp4">
        </video>
        <img class="video-fallback" src="/assets/video/beestenmarkt-pan-poster.jpg" alt="Uitzicht over de Beestenmarkt vanuit een hotelkamer" loading="lazy" hidden>
      </div>
    </div>
  </section>

  <section class="section section--tint">
    <div class="container">
      <div class="center reveal">
        <p class="eyebrow">Goed om te weten</p>
        <h2>Eerlijk, vóór u boekt</h2>
      </div>
      <div class="know-strip" style="margin-top:2.6rem">
        <div class="know reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 20h4v-4h4v-4h4V8h4M4 20V4"/></svg><div><strong>Historisch pand, geen lift</strong>Alle kamers zijn via de trap bereikbaar.</div></div>
        <div class="know reveal reveal-d1"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h4"/></svg><div><strong>Alleen pinnen</strong>Wij accepteren geen contant geld.</div></div>
        <div class="know reveal reveal-d2"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 4h12M6 4c0 4 3 5 3 8s-3 4-3 8m12-16c0 4-3 5-3 8s3 4 3 8M6 20h12"/></svg><div><strong>Tijdelijk geen ontbijt</strong>Volop goede ontbijtadresjes op loopafstand.</div></div>
        <div class="know reveal reveal-d3"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg><div><strong>Inchecken 15:00 – 18:00</strong>Komt u later aan? Regel vooraf onze sleutelkluis.</div></div>
      </div>
      <div class="center reveal" style="margin-top:2.4rem">
        <a class="btn btn-ghost" href="/nl/hotelinformatie/">Alle praktische informatie</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="center reveal">
        <p class="eyebrow">Gasten over ons</p>
        <h2>Woorden van het plein</h2>
        <p class="lede">Google beoordeelt onze plek aan de Beestenmarkt met 4,7 van 5 voor bezoekers: "buitengewoon aantrekkelijk". Dit zeggen onze gasten.</p>
      </div>
      <div class="grid grid-3" style="margin-top:3rem">
        <div class="tile reveal">
          <blockquote style="margin:0">"Toplocatie met zeer vriendelijke medewerkers. De kamers waren schoon, de bedden sliepen fantastisch en de kamers waren bovendien ruim en comfortabel. Goede prijs-kwaliteitverhouding."</blockquote>
          <cite style="color:var(--faint);font-style:normal">Joran · ★★★★★ via Google</cite>
        </div>
        <div class="tile reveal reveal-d1">
          <blockquote style="margin:0">"Goed ontvangen, zeer mooie kamer, vriendelijke schoonmaakster. Zeer aan te raden."</blockquote>
          <cite style="color:var(--faint);font-style:normal">Piet · ★★★★★ via Google</cite>
        </div>
        <div class="tile reveal reveal-d2">
          <h3 style="font-size:1.25rem">Een nieuw hoofdstuk</h3>
          <p style="color:var(--muted);font-size:.95rem;margin:0">Sinds mei 2026 heeft Hotel Mayflower nieuwe eigenaren. Nieuwe bedden en kussens, vernieuwd meubilair, smart-tv's op elke kamer, en er komen elke maand verbeteringen bij.</p>
          <a href="https://www.google.com/maps?cid=67496388067959428" rel="noopener" target="_blank" style="font-size:.95rem">Lees alle reviews op Google</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="center reveal">
        <p class="eyebrow">Vragen</p>
        <h2>Veelgestelde vragen</h2>
      </div>
      <div class="faq-list reveal" style="margin-top:2.6rem">
        <details class="faq-item">
          <summary>Serveert het hotel ontbijt?</summary>
          <div class="faq-a"><p>Op dit moment niet. Het ontbijt is tijdelijk niet beschikbaar vanwege renovatiewerkzaamheden. Op korte loopafstand van het hotel vindt u diverse goede cafés en ontbijtgelegenheden; wij wijzen u graag onze favorieten. Was ontbijt bij uw boeking inbegrepen of heeft u vooruitbetaald, dan wordt dat bedrag uiteraard terugbetaald.</p></div>
        </details>
        <details class="faq-item">
          <summary>Hoe ver is het hotel van Leiden Centraal?</summary>
          <div class="faq-a"><p>Ongeveer vijf minuten lopen. Verlaat het station aan de centrumzijde, volg de Stationsweg richting de stad en u loopt vanzelf de Beestenmarkt op.</p></div>
        </details>
        <details class="faq-item">
          <summary>Kan ik na 18:00 uur aankomen?</summary>
          <div class="faq-a"><p>Ja. Laat het ons vooraf weten, dan leggen wij uw sleutel in onze sleutelkluis zodat u op elk moment naar binnen kunt. Met uw sleutel heeft u tijdens uw verblijf 24/7 toegang tot het hotel.</p></div>
        </details>
      </div>
      <div class="center" style="margin-top:2rem">
        <a class="btn btn-ghost" href="/nl/veelgestelde-vragen/">Alle vragen &amp; antwoorden</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-band reveal">
        <p class="eyebrow" style="color:var(--gold-soft)">Beestenmarkt 2, Leiden</p>
        <h2>Uw kamer aan het plein staat klaar</h2>
        <p class="lede">Boek rechtstreeks bij ons voor de beste beschikbare prijs, zonder tussenpartij en zonder verrassingen.</p>
        <div class="hero-cta" style="justify-content:center">
          <a class="btn btn-gold" href="{BOOK}" rel="noopener">Boek uw verblijf</a>
          <a class="btn btn-ghost" style="color:#F7F1E4;border-color:rgba(247,241,228,.35)" href="/nl/contact/">Stel ons uw vraag</a>
        </div>
      </div>
    </div>
  </section>

</main>
"""
write_page("nl", "nl/index.html",
           "Hotel Mayflower Leiden | Hotel in centrum Leiden, bij Leiden Centraal",
           "Hotel Mayflower is een gastvrij tweesterrenhotel aan de Beestenmarkt in hartje Leiden, op vijf minuten lopen van Leiden Centraal. Boek direct voor de beste prijs.",
           "/nl/", "/nl/", "/en/", home_body, hotel_ld, body_class="has-hero",
           og_title="Hotel Mayflower: Verblijf in het hart van Leiden",
           og_desc="Een gastvrij stadshotel op loopafstand van Leiden Centraal, musea, restaurants en de historische binnenstad.")


# ---------------- Kamers overzicht ----------------
kamers_body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/nl/"), ("Kamers", None))}
      <p class="eyebrow">Onze kamers</p>
      <h1>Kamers met Leiden voor het raam</h1>
      <p class="lede">Tweeëntwintig kamers in een karakteristiek historisch pand aan de Beestenmarkt. Niets wat u niet nodig heeft, alles wat u wél nodig heeft: een comfortabel bed, een eigen badkamer met ligbad, gratis wifi, een televisie en thee- en koffiefaciliteiten.</p>
    </div>
  </div>

  <section class="section">
    <div class="container grid grid-3">
      <article class="card reveal">
        <div class="card-media">
          {picture("room-single-overview", "Lichte eenpersoonskamer met bed, bureau en raam")}
        </div>
        <div class="card-body">
          <span class="card-kicker">Voor 1 persoon</span>
          <h3>Eenpersoonskamer</h3>
          <ul class="card-meta">
            <li>Eigen badkamer</li>
            <li>Gratis wifi</li>
            <li>TV</li>
            <li>Thee &amp; koffie</li>
          </ul>
          <a class="btn btn-ghost" href="/nl/kamers/eenpersoonskamer/">Bekijk kamer</a>
        </div>
      </article>
      <article class="card reveal reveal-d1">
        <div class="card-media">
          {picture("room-double-overview", "Gerenoveerde tweepersoonskamer met bed, bureau en zithoek")}
        </div>
        <div class="card-body">
          <span class="card-kicker">Voor 2 personen · Sommige met pleinzicht</span>
          <h3>Tweepersoonskamer</h3>
          <ul class="card-meta">
            <li>Eigen badkamer</li>
            <li>Gratis wifi</li>
            <li>TV</li>
            <li>Thee &amp; koffie</li>
          </ul>
          <a class="btn btn-ghost" href="/nl/kamers/tweepersoonskamer/">Bekijk kamer</a>
        </div>
      </article>
      <article class="card reveal reveal-d2">
        <div class="card-media">
          {picture("room-triple-renovated", "Gerenoveerde driepersoonskamer met drie bedden")}
        </div>
        <div class="card-body">
          <span class="card-kicker">Voor 3 personen · Gezinsfavoriet</span>
          <h3>Driepersoonskamer</h3>
          <ul class="card-meta">
            <li>Eigen badkamer</li>
            <li>Gratis wifi</li>
            <li>TV</li>
            <li>Thee &amp; koffie</li>
          </ul>
          <a class="btn btn-ghost" href="/nl/kamers/driepersoonskamer/">Bekijk kamer</a>
        </div>
      </article>
    </div>
  </section>

  <section class="section section--tint">
    <div class="container split">
      <div class="reveal">
        <p class="eyebrow">Voordat u kiest</p>
        <h2>Eerlijk over onze kamers</h2>
        <p>Ons pand stamt uit een tijd van vóór de lift: <strong>alle kamers zijn via de trap bereikbaar</strong>. Is traplopen voor u lastig, neem dan vóór het boeken even <a href="/nl/contact/">contact</a> op, dan denken we met u mee.</p>
        <p>Uitzicht, balkons en de exacte indeling verschillen per kamer en zijn afhankelijk van beschikbaarheid: sommige kamers kijken uit op de Beestenmarkt, sommige hebben een balkon, andere liggen aan de rustigere achterzijde. Op warme dagen staat er een mobiele aircooler op uw kamer: geen airconditioning, maar met de meegeleverde koelelementen houdt u het aangenaam.</p>
        <p>Prijzen staan altijd actueel op onze boekingspagina; wat u daar ziet betaalt u, zonder commissie van een tussenpartij.</p>
        <a class="btn btn-gold" href="{BOOK}" rel="noopener">Bekijk beschikbaarheid</a>
      </div>
      <div class="split-media portrait reveal reveal-d1">
        <video autoplay muted loop playsinline preload="metadata" poster="/assets/video/room-pan-poster.jpg" aria-label="Video: impressie van een hotelkamer">
          <source src="/assets/video/room-pan.mp4" type="video/mp4">
        </video>
        <img class="video-fallback" src="/assets/video/room-pan-poster.jpg" alt="Impressie van een hotelkamer" loading="lazy" hidden>
      </div>
    </div>
  </section>
</main>
"""
write_page("nl", "nl/kamers/index.html",
           "Kamers: Eenpersoons, Tweepersoons & Driepersoons | Hotel Mayflower Leiden",
           "Eenpersoons-, tweepersoons- en driepersoonskamers in het centrum van Leiden, elk met eigen badkamer met ligbad, gratis wifi, televisie en thee- en koffiefaciliteiten.",
           "/nl/kamers/", "/nl/kamers/", "/en/rooms/", kamers_body,
           crumb_ld(("Home", "/nl/"), ("Kamers", "/nl/kamers/")))


# ---------------- Kamerpagina's ----------------
ROOM_FACTS_NL = """<ul class="card-meta" style="font-size:1rem;gap:.6rem 1.4rem">
  <li>✓ Eigen badkamer met ligbad</li>
  <li>✓ Gratis wifi</li>
  <li>✓ Televisie</li>
  <li>✓ Thee- en koffiefaciliteiten</li>
  <li>✓ Fris linnengoed &amp; handdoeken</li>
</ul>"""

STAIRS_NL = """<div class="notice">
  <strong>Historisch pand, alleen trappen.</strong> Ons gebouw heeft geen lift; alle kamers zijn via de trap bereikbaar. Is traplopen voor u lastig, neem dan vóór het boeken even <a href="/nl/contact/">contact</a> met ons op, dan denken we met u mee.
</div>"""

VARY_NL = """<p class="booking-note">De foto's tonen een selectie van onze kamers. Uitzicht, balkons en exacte indeling verschillen per kamer en zijn afhankelijk van beschikbaarheid. Op warme dagen staat er een mobiele aircooler klaar. Let op: dit is een aircooler, geen airconditioning.</p>"""


def kamer_page(slug, name, kicker, occupancy, intro, paras, gallery, en_slug, title, desc):
    path = f"/nl/kamers/{slug}/"
    alt = f"/en/rooms/{en_slug}/"
    figs = "\n".join(
        f'<figure class="reveal{" wide" if i == 0 else ""}>{picture(n, a, sizes="(min-width: 700px) 46vw, 92vw" if i == 0 else "(min-width: 700px) 30vw, 92vw")}<figcaption>{a}</figcaption></figure>'
        for i, (n, a) in enumerate(gallery))
    body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/nl/"), ("Kamers", "/nl/kamers/"), (name, None))}
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
        <h2>Waar u op kunt rekenen</h2>
        {ROOM_FACTS_NL}
        {"".join(f"<p>{p}</p>" for p in paras)}
        {STAIRS_NL}
        {VARY_NL}
      </div>
      <div class="reveal reveal-d1">
        <div class="booking-bar" style="grid-template-columns:1fr">
          <h3 style="margin:0">Klaar wanneer u dat bent</h3>
          <p style="color:var(--muted);margin:0">Actuele prijzen en beschikbaarheid op onze beveiligde boekingspagina. Direct boeken is altijd de beste prijs.</p>
          <a class="btn btn-gold" href="{BOOK}" rel="noopener">Boek deze kamer</a>
          <a class="btn btn-ghost" href="/nl/kamers/">Vergelijk alle kamers</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    jsonld = crumb_ld(("Home", "/nl/"), ("Kamers", "/nl/kamers/"), (name, path))
    write_page("nl", f"nl/kamers/{slug}/index.html", title, desc, "/nl/kamers/", path, alt, body, jsonld)


kamer_page(
    "eenpersoonskamer", "Eenpersoonskamer", "Voor 1 persoon · Rustig en compact", 1,
    "Een compacte, rustige kamer voor wie alleen reist: een comfortabel bed, een eigen badkamer en heel Leiden voor de voordeur.",
    ["Alleen op pad voor werk, studie of een stedentrip? Onze eenpersoonskamers houden het eenvoudig: alles voor een goede nacht, niets dat in de weg staat. Zet uw tas neer, zet een kop thee en stap naar buiten: Leiden Centraal, de musea en de binnenstad liggen allemaal op korte loopafstand.",
     "Sommige kamers kijken uit over de daken van de oude stad; stuk voor stuk bieden ze dezelfde rustige basis."],
    [("room-single-overview", "Lichte eenpersoonskamer met bed, bureau en raam"),
     ("room-single-bed", "Een comfortabel bed bij het raam"),
     ("room-single-desk", "Bureau met thee- en koffiefaciliteiten en televisie"),
     ("room-bathroom-tub", "Elke kamer heeft een eigen badkamer met ligbad")],
    "single",
    "Eenpersoonskamer | Hotel Mayflower Leiden",
    "Compacte eenpersoonskamer in het centrum van Leiden met eigen badkamer met ligbad, gratis wifi, televisie en thee- en koffiefaciliteiten. Boek direct.")

kamer_page(
    "tweepersoonskamer", "Tweepersoonskamer", "Voor 2 personen · Onze meest geboekte kamer", 2,
    "Karakteristieke tweepersoonskamers in een historisch pand: sommige met uitzicht op de levendige Beestenmarkt, sommige met balkon, allemaal met eigen badkamer.",
    ["Onze tweepersoonskamers zijn het hart van het hotel: comfortabele kamers voor twee, hier een zithoekje, daar schuine balken, en in de kamers aan de voorzijde een eersterangs uitzicht op het gezelligste plein van Leiden.",
     "Perfect voor een weekend vol musea en grachtendiners, of als vriendelijke uitvalsbasis tussen Amsterdam, Den Haag en de kust."],
    [("room-double-overview", "Gerenoveerde tweepersoonskamer met bed, bureau en zithoek"),
     ("room-double-window-seating", "Zithoek bij het raam met uitzicht op het plein"),
     ("room-double-attic", "Tweepersoonskamer onder de schuine witte balken"),
     ("room-double-twin", "Sommige tweepersoonskamers hebben twee losse bedden"),
     ("room-bathroom-tub", "Elke kamer heeft een eigen badkamer met ligbad")],
    "double",
    "Tweepersoonskamer | Hotel Mayflower Leiden",
    "Tweepersoonskamer in hartje Leiden, sommige met uitzicht op de Beestenmarkt of balkon. Eigen badkamer, gratis wifi, televisie. Boek direct voor de beste prijs.")

kamer_page(
    "driepersoonskamer", "Driepersoonskamer", "Voor 3 personen · Gezinsfavoriet", 3,
    "Ruimte voor drie: drie volwaardige bedden, een eigen badkamer en plek om uw spullen kwijt te kunnen. Ideaal voor vrienden of een klein gezin.",
    ["Geen slaapbanken of inschikken: onze driepersoonskamers hebben drie volwaardige bedden, zodat iedereen uitgerust aan de dag begint. Tussen het station, het plein en de musea heeft u het openbaar vervoer nauwelijks nodig.",
     "Een aantal driepersoonskamers is onlangs gerenoveerd; vraag bij het boeken gerust naar de actuele mogelijkheden."],
    [("room-triple-renovated", "Gerenoveerde driepersoonskamer met drie bedden"),
     ("room-triple-beds", "Driepersoonskamer met drie eenpersoonsbedden"),
     ("room-bathroom-tub", "Elke kamer heeft een eigen badkamer met ligbad")],
    "triple",
    "Driepersoonskamer | Hotel Mayflower Leiden",
    "Driepersoonskamer met drie volwaardige bedden in het centrum van Leiden. Eigen badkamer, gratis wifi, televisie. Ideaal voor vrienden of gezin. Boek direct.")


# ---------------- Leiden ----------------
leiden_tiles = [
    ("± 5 min lopen", "Leiden Centraal", "Rechtstreekse treinen naar Amsterdam (35 min), Schiphol (20 min), Den Haag en Rotterdam."),
    ("± 4 min lopen", "Museum De Lakenhal", "Beeldende kunst en het verhaal van het Leidse laken, inclusief de jonge Rembrandt."),
    ("± 5 min lopen", "Museum Volkenkunde", "Een van de oudste volkenkundige musea van Europa, aan de Steenstraat."),
    ("± 10 min lopen", "Rijksmuseum van Oudheden", "Het nationale oudhedenmuseum: Egypte, de klassieke wereld en Nederlandse archeologie."),
    ("Voor de deur", "Grachten &amp; rondvaart", "Rondvaartboten en sloepverhuur vertrekken vanaf het water direct aan het plein."),
    ("± 3 min lopen", "Haarlemmerstraat", "De belangrijkste winkelstraat van Leiden, met op woensdag en zaterdag de markt aan de Nieuwe Rijn."),
    ("± 10 min lopen", "Pieterskerkbuurt", "Sfeervolle steegjes, authentieke winkels en de kerk van de Pilgrims."),
    ("± 12 min lopen", "Hortus botanicus", "De oudste botanische tuin van Nederland, midden in het universiteitskwartier."),
]
tiles_html = "\n".join(
    f"""        <div class="tile reveal"><span class="walk">{w}</span><h3>{t}</h3><p>{d}</p></div>"""
    for w, t, d in leiden_tiles)

leiden_body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/nl/"), ("Leiden", None))}
      <p class="eyebrow">Leiden &amp; omgeving</p>
      <h1>Stad van Ontdekkingen, te voet</h1>
      <p class="lede">Hotel Mayflower staat aan de Beestenmarkt, waar de oude stad begint. Musea, grachten, winkelstraten en het station: alles ligt op loopafstand.</p>
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
        <p class="eyebrow">Waarom Leiden</p>
        <h2>De wieg van Rembrandt, de haven van de Pilgrims</h2>
        <p class="sub-italic">Klein genoeg om te lopen, rijk genoeg voor een week.</p>
        <p>Leiden draagt zijn geschiedenis licht: dertien musea, de oudste universiteit van het land, molens boven de grachten en hofjes die schuilgaan achter gewone voordeuren. Huur een sloep, loop mee met een stadswandeling of volg het Singelpark, zes groene kilometers rond de binnenstad.</p>
        <p>Op woensdag en zaterdag strijkt de markt neer langs de Nieuwe Rijn, op vijf minuten van uw kamer. En als de musea sluiten, wordt de Beestenmarkt zelf de bestemming: terrassen, restaurants en avondlicht op het water.</p>
        <p style="font-size:.9rem;color:var(--faint)">Logeert u bij ons? Onze <a href="/nl/gids/">gastengids</a> bundelt restaurants, wandelroutes en dagtrips, allemaal vanaf onze voordeur. Tip: kijk op <a href="https://www.visitleiden.nl" rel="noopener">visitleiden.nl</a> voor tentoonstellingen en evenementen tijdens uw verblijf. De genoemde attracties zijn aanbevelingen voor uw bezoek; openingstijden en programma's worden door de locaties zelf bepaald.</p>
      </div>
      <div class="split-media portrait reveal reveal-d1">
        {picture("view-beestenmarkt", "Uitzicht over de Beestenmarkt en de rondvaartboten", sizes="(min-width: 900px) 44vw, 92vw", widths=(480, 960, 1600))}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="center reveal">
        <p class="eyebrow">Hier vindt u ons</p>
        <h2>Beestenmarkt 2, Leiden</h2>
        <p class="lede">Vanaf Leiden Centraal: verlaat het station aan de centrumzijde, volg de Stationsweg richting de stad, en na zo'n vijf minuten opent het plein zich voor u. Wij zitten aan de overzijde, naast de witte HOTEL-entree.</p>
      </div>
      <div class="map-embed reveal" data-map-title="Kaart met Hotel Mayflower, Beestenmarkt 2, Leiden" style="margin-top:2.4rem">
        <div class="map-consent">
          <svg class="pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/></svg>
          <p>De interactieve kaart wordt geladen van Google Maps. Klik om dit toe te staan.</p>
          <button class="btn btn-gold" type="button">Toon kaart</button>
        </div>
      </div>
      <p class="center" style="margin-top:1.4rem"><a href="https://maps.google.com/?q=Hotel+Mayflower,+Beestenmarkt+2,+Leiden" rel="noopener">Open in Google Maps</a></p>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="cta-band reveal">
        <h2>Slaap waar Leiden gebeurt</h2>
        <p class="lede">Word wakker aan de Beestenmarkt en heb de stad voor uzelf voordat de dagjesmensen arriveren.</p>
        <div class="hero-cta" style="justify-content:center">
          <a class="btn btn-gold" href="{BOOK}" rel="noopener">Boek uw verblijf</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
write_page("nl", "nl/leiden/index.html",
           "Leiden & Omgeving | Hotel Mayflower, Beestenmarkt 2",
           "Hotel Mayflower ligt in hartje Leiden: vijf minuten lopen van Leiden Centraal en vlak bij De Lakenhal, Volkenkunde, het Rijksmuseum van Oudheden en de grachten.",
           "/nl/leiden/", "/nl/leiden/", "/en/leiden/", leiden_body,
           crumb_ld(("Home", "/nl/"), ("Leiden", "/nl/leiden/")))


# ---------------- Hotelinformatie ----------------
info_body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/nl/"), ("Hotelinformatie", None))}
      <p class="eyebrow">Praktisch</p>
      <h1>Hotelinformatie</h1>
      <p class="lede">Alles wat u wilt weten vóór uw aankomst, eerlijk en op één plek. Vragen? Bel <a href="tel:+31715142641">+31 71 514 2641</a> of mail <a href="mailto:info@hotelmayflower.nl">info@hotelmayflower.nl</a>.</p>
    </div>
  </div>

  <section class="section" style="padding-top:0">
    <div class="container grid grid-2">
      <div class="tile reveal">
        <h3>Inchecken</h3>
        <p>Inchecken kan van <strong>15:00 tot 18:00 uur</strong>. Onze receptie is geopend van <strong>09:00 tot 18:00 uur</strong>. Bent u eerder in de stad? Van harte welkom: uw kamer staat vanaf 15:00 uur klaar, en tot die tijd kunt u uw bagage bij de receptie achterlaten.</p>
      </div>
      <div class="tile reveal reveal-d1">
        <h3>Aankomst na 18:00 uur</h3>
        <p>Geen probleem, mits vooraf afgesproken: wij leggen uw sleutel in onze sleutelkluis, zodat u op elk moment naar binnen kunt. Bel of mail ons vóór uw aankomstdag om dit te regelen. Met uw sleutel kunt u vervolgens dag en nacht in en uit; het hotel is voor gasten 24/7 toegankelijk.</p>
      </div>
      <div class="tile reveal">
        <h3>Uitchecken</h3>
        <p>Uitchecken doet u uiterlijk om <strong>10:30 uur</strong>. Latere trein of vlucht? U kunt uw bagage tussen 09:00 en 18:00 uur bij ons achterlaten (op eigen risico) en nog even van Leiden genieten.</p>
      </div>
      <div class="tile reveal reveal-d1">
        <h3>Betalen</h3>
        <p>Wij accepteren <strong>uitsluitend pinbetalingen</strong> (debit- en creditcards). Contant geld wordt in het hotel niet geaccepteerd.</p>
      </div>
      <div class="tile reveal">
        <h3>Ontbijt</h3>
        <p>Hotel Mayflower serveert op dit moment geen ontbijt vanwege renovatiewerkzaamheden. Op korte loopafstand vindt u diverse cafés en ontbijtgelegenheden; zie onze tips hieronder. Was ontbijt bij uw boeking inbegrepen of heeft u vooruitbetaald, dan wordt dat bedrag uiteraard terugbetaald.</p>
      </div>
      <div class="tile reveal reveal-d1">
        <h3>Geen lift</h3>
        <p>Houd er rekening mee dat ons historische gebouw geen lift heeft. Alle hotelkamers zijn via de trap bereikbaar. Is traplopen voor u lastig, neem dan vóór het boeken contact met ons op, dan denken we met u mee.</p>
      </div>
      <div class="tile reveal">
        <h3>Huisdieren</h3>
        <p>Huisdieren zijn in Hotel Mayflower niet toegestaan.</p>
      </div>
      <div class="tile reveal reveal-d1">
        <h3>Roken</h3>
        <p>Alle kamers en binnenruimtes zijn rookvrij.</p>
      </div>
      <div class="tile reveal">
        <h3>Wifi</h3>
        <p>Gratis wifi in het hele hotel. De netwerkgegevens ontvangt u bij het inchecken.</p>
      </div>
      <div class="tile reveal reveal-d1">
        <h3>Warme dagen</h3>
        <p>In de warmere maanden staat er een mobiele aircooler op de kamers, met koelelementen voor extra verkoeling. Let op: dit is een aircooler met ventilator en waterverdamping, geen airconditioning.</p>
      </div>
    </div>
  </section>

  <section class="section section--tint">
    <div class="container">
      <div class="reveal">
        <p class="eyebrow">Ontbijt in de buurt</p>
        <h2>Vier goede ochtenden, op loopafstand</h2>
      </div>
      <div class="table-wrap reveal" style="margin-top:1.8rem">
        <table class="info-table">
          <thead><tr><th scope="col">Adres</th><th scope="col">Locatie</th><th scope="col">Open</th></tr></thead>
          <tbody>
            <tr><td>Tootje</td><td>Haarlemmerstraat 2</td><td>ma–vr 08:00–18:00 · za–zo 10:00–17:00</td></tr>
            <tr><td>Leidsch Beleg</td><td>Turfmarkt 12</td><td>ma–za 09:00–17:00 · zo 10:00–17:00</td></tr>
            <tr><td>De Bruine Boon</td><td>Stationsweg 1</td><td>dagelijks 09:00–22:00</td></tr>
            <tr><td>Ibis Hotel</td><td>Stationsplein 240–242</td><td>ma–vr 06:30–10:00 · za–zo 06:30–11:00</td></tr>
          </tbody>
        </table>
      </div>
      <p class="booking-note">Openingstijden worden door de gelegenheden zelf bepaald en kunnen wijzigen.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="reveal">
        <p class="eyebrow">Parkeren</p>
        <h2>Leiden is een wandelstad, parkeer dus aan de rand</h2>
        <p class="lede">Het hotel heeft geen eigen parkeergelegenheid, en de binnenstad is nooit op auto's gebouwd. Deze openbare opties werken goed:</p>
      </div>
      <div class="table-wrap reveal" style="margin-top:1.8rem">
        <table class="info-table">
          <thead><tr><th scope="col">Parkeren</th><th scope="col">Adres</th><th scope="col">Vanaf het hotel</th><th scope="col">Goed om te weten</th></tr></thead>
          <tbody>
            <tr><td>Stadsparkeerplan Haagweg</td><td>Haagweg 8</td><td>Gratis pendelbus tot de deur</td><td>Voordeligst voor langere verblijven; de pendelbus zet u bij het hotel af. 24 uur open.</td></tr>
            <tr><td>Parkeergarage Lammermarkt</td><td>Lammermarkt 20</td><td>± 3 min lopen</td><td>Dichtstbijzijnde garage, onder molen De Valk.</td></tr>
            <tr><td>Parkeergarage Morspoort</td><td>Bloemfonteinstraat 2</td><td>± 5 min lopen</td><td>24 uur in- en uitrijden; elektrisch laden mogelijk.</td></tr>
            <tr><td>Parkeerterrein Morssingel</td><td>Morssingel 179</td><td>± 5 min lopen</td><td>Buitenterrein, naast het station.</td></tr>
          </tbody>
        </table>
      </div>
      <p class="booking-note">Tarieven worden door de exploitanten bepaald en wijzigen af en toe; kijk voor actuele tarieven op <a href="https://www.parkeren-leiden.nl" rel="noopener">parkeren-leiden.nl</a>. Op straat parkeren in het centrum is betaald en schaars; wij raden de garages aan.</p>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="cta-band reveal">
        <h2>Nog iets niet beantwoord?</h2>
        <p class="lede">Bekijk de veelgestelde vragen, of bel of schrijf ons gewoon. We reageren snel.</p>
        <div class="hero-cta" style="justify-content:center">
          <a class="btn btn-gold" href="/nl/veelgestelde-vragen/">Lees de veelgestelde vragen</a>
          <a class="btn btn-ghost" style="color:#F7F1E4;border-color:rgba(247,241,228,.35)" href="/nl/contact/">Neem contact op</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
write_page("nl", "nl/hotelinformatie/index.html",
           "Hotelinformatie: Inchecken, Parkeren & Praktische Zaken | Hotel Mayflower Leiden",
           "Inchecken vanaf 15:00, late aankomst via de sleutelkluis, alleen pinnen, geen lift, parkeeropties en alles wat u verder wilt weten vóór uw verblijf bij Hotel Mayflower Leiden.",
           "/nl/hotelinformatie/", "/nl/hotelinformatie/", "/en/hotel-information/", info_body,
           crumb_ld(("Home", "/nl/"), ("Hotelinformatie", "/nl/hotelinformatie/")))


# ---------------- Contact ----------------
contact_body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/nl/"), ("Contact", None))}
      <p class="eyebrow">Contact</p>
      <h1>We horen graag van u</h1>
      <p class="lede">Een vraag over uw verblijf, een bijzonder verzoek of hulp bij het plannen van uw bezoek? Bel, mail of gebruik het formulier hieronder.</p>
    </div>
  </div>

  <section class="section" style="padding-top:0">
    <div class="container split">
      <div class="reveal">
        <form id="contact-form" class="form" novalidate>
          <div class="form-row">
            <div>
              <label for="cf-name">Uw naam</label>
              <input id="cf-name" name="name" type="text" autocomplete="name" required>
            </div>
            <div>
              <label for="cf-email">E-mailadres</label>
              <input id="cf-email" name="email" type="email" autocomplete="email" required>
            </div>
          </div>
          <div class="form-row">
            <div>
              <label for="cf-arrival">Aankomstdatum (optioneel)</label>
              <input id="cf-arrival" name="arrival" type="date">
            </div>
            <div>
              <label for="cf-nights">Nachten (optioneel)</label>
              <input id="cf-nights" name="nights" type="number" min="1" max="30">
            </div>
          </div>
          <div>
            <label for="cf-message">Uw bericht</label>
            <textarea id="cf-message" name="message" required></textarea>
          </div>
          <p style="position:absolute;left:-9999px" aria-hidden="true"><label>Laat dit veld leeg<input type="text" name="website" tabindex="-1" autocomplete="off"></label></p>
          <p class="form-status" role="status"></p>
          <button class="btn btn-gold" type="submit">Verstuur bericht</button>
          <p class="hint">Wij reageren binnen 24 uur. Voor beschikbaarheid en prijzen is onze <a href="{BOOK}" rel="noopener">boekingspagina</a> altijd actueel.</p>
        </form>
      </div>
      <div class="reveal reveal-d1">
        <div class="tile" style="margin-bottom:1rem">
          <h3>Hotel Mayflower</h3>
          <p>Beestenmarkt 2<br>2312 CC Leiden<br>Nederland</p>
          <p><a href="tel:+31715142641">+31 71 514 2641</a><br>
          <a href="mailto:info@hotelmayflower.nl">info@hotelmayflower.nl</a></p>
          <p>Receptie geopend 09:00–18:00 uur · gasten hebben met hun eigen sleutel 24/7 toegang.</p>
        </div>
        <div class="tile">
          <h3>Vanaf Leiden Centraal</h3>
          <p>Verlaat het station aan de centrumzijde en volg de Stationsweg rechtdoor. Steek het water over, en na zo'n vijf minuten loopt u de Beestenmarkt op. De hotelingang ligt aan het plein.</p>
          <p style="margin-top:.6rem"><strong>Komt u na 18:00 uur aan?</strong> Regel vooraf de sleutelkluis met ons en kom binnen wanneer het u uitkomt.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="map-embed reveal" data-map-title="Kaart met Hotel Mayflower, Beestenmarkt 2, Leiden">
        <div class="map-consent">
          <svg class="pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/></svg>
          <p>De interactieve kaart wordt geladen van Google Maps. Klik om dit toe te staan.</p>
          <button class="btn btn-gold" type="button">Toon kaart</button>
        </div>
      </div>
    </div>
  </section>
</main>
"""
write_page("nl", "nl/contact/index.html",
           "Contact | Hotel Mayflower Leiden, Beestenmarkt 2",
           "Contact met Hotel Mayflower in Leiden: +31 71 514 2641, info@hotelmayflower.nl, Beestenmarkt 2. Routebeschrijving vanaf Leiden Centraal en aankomstinformatie.",
           "/nl/contact/", "/nl/contact/", "/en/contact/", contact_body,
           crumb_ld(("Home", "/nl/"), ("Contact", "/nl/contact/")))


# ---------------- Veelgestelde vragen ----------------
faqs = [
    ("Serveert het hotel ontbijt?",
     "Op dit moment niet. Het ontbijt is tijdelijk niet beschikbaar vanwege renovatiewerkzaamheden. Op korte loopafstand van het hotel vindt u diverse goede cafés en ontbijtgelegenheden; onze favorieten staan op de pagina hotelinformatie. Was ontbijt bij uw boeking inbegrepen of heeft u vooruitbetaald, dan wordt dat bedrag terugbetaald."),
    ("Hoe laat kan ik inchecken?",
     "Inchecken kan van 15:00 tot 18:00 uur. Eerder aankomen mag: uw kamer staat vanaf 15:00 uur klaar, en tot die tijd kunt u uw bagage bij de receptie achterlaten."),
    ("Kan ik na 18:00 uur aankomen?",
     "Ja. Laat het ons vooraf weten, dan leggen wij uw sleutel in onze sleutelkluis zodat u op elk moment naar binnen kunt. Met uw sleutel heeft u tijdens uw verblijf 24/7 toegang tot het hotel."),
    ("Hoe laat is het uitchecken?",
     "Uitchecken doet u uiterlijk om 10:30 uur. Daarna kunt u uw bagage tussen 09:00 en 18:00 uur bij ons achterlaten."),
    ("Heeft het hotel een lift?",
     "Nee. Ons historische gebouw heeft geen lift; alle kamers zijn via de trap bereikbaar. Is traplopen voor u lastig, neem dan vóór het boeken contact met ons op."),
    ("Zijn huisdieren toegestaan?",
     "Nee, huisdieren zijn in Hotel Mayflower niet toegestaan."),
    ("Is er parkeergelegenheid?",
     "Het hotel heeft geen eigen parkeergelegenheid. Goede openbare opties in de buurt: parkeergarage Lammermarkt (± 3 minuten lopen), parkeergarage Morspoort en parkeerterrein Morssingel (beide ± 5 minuten), of het voordelige Stadsparkeerplan aan de Haagweg met gratis pendelbus die vlak bij het hotel stopt."),
    ("Welke betaalmethoden worden geaccepteerd?",
     "Wij accepteren uitsluitend pinbetalingen (debit- en creditcards). Contant geld wordt niet geaccepteerd."),
    ("Hoe ver is het hotel van Leiden Centraal?",
     "Ongeveer vijf minuten lopen. Verlaat het station aan de centrumzijde, volg de Stationsweg richting de stad en u loopt vanzelf de Beestenmarkt op."),
    ("Kan ik mijn bagage achterlaten vóór het inchecken?",
     "Ja. U kunt uw bagage tussen 09:00 en 18:00 uur bij de receptie achterlaten, op eigen risico. Zo kunt u meteen Leiden in."),
    ("Welke kamertypes zijn er?",
     "Wij bieden eenpersoons-, tweepersoons- en driepersoonskamers, elk met eigen badkamer met ligbad, gratis wifi, televisie en thee- en koffiefaciliteiten. Uitzicht en balkons verschillen per kamer en zijn afhankelijk van beschikbaarheid."),
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
      {crumbs(("Home", "/nl/"), ("Veelgestelde vragen", None))}
      <p class="eyebrow">Vragen &amp; antwoorden</p>
      <h1>Veelgestelde vragen</h1>
      <p class="lede">De korte, eerlijke antwoorden. Mist u iets? <a href="/nl/contact/">Stel uw vraag direct</a>; we reageren snel.</p>
    </div>
  </div>
  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="faq-list reveal">
{faq_items}
      </div>
      <div class="center" style="margin-top:2.6rem">
        <a class="btn btn-gold" href="{BOOK}" rel="noopener">Boek uw verblijf</a>
      </div>
    </div>
  </section>
</main>
"""
write_page("nl", "nl/veelgestelde-vragen/index.html",
           "Veelgestelde Vragen | Hotel Mayflower Leiden",
           "Antwoorden op veelgestelde vragen over Hotel Mayflower Leiden: in- en uitchecktijden, late aankomst, ontbijt, parkeren, betalen, huisdieren en bagage.",
           None, "/nl/veelgestelde-vragen/", "/en/faq/", faq_body,
           crumb_ld(("Home", "/nl/"), ("Veelgestelde vragen", "/nl/veelgestelde-vragen/")) + faq_jsonld)


# ---------------- Privacy ----------------
privacy_body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/nl/"), ("Privacy & cookies", None))}
      <p class="eyebrow">Juridisch</p>
      <h1>Privacy- &amp; cookiebeleid</h1>
      <p class="lede">De korte versie: deze website volgt u zo min mogelijk, en wij verwerken uw gegevens alleen om uw verblijf mogelijk te maken.</p>
    </div>
  </div>
  <section class="section" style="padding-top:0">
    <div class="container" style="max-width:46rem">
      <h2>Wie wij zijn</h2>
      <p>Hotel Mayflower, Beestenmarkt 2, 2312 CC Leiden, is verwerkingsverantwoordelijke voor de hier beschreven persoonsgegevens. Contact: <a href="mailto:info@hotelmayflower.nl">info@hotelmayflower.nl</a>, +31 71 514 2641.</p>

      <h2>Wat deze website bewaart</h2>
      <p>Deze website plaatst <strong>geen tracking- of advertentiecookies</strong> en gebruikt geen analytics-diensten. Er worden enkele functionele voorkeuren bewaard in de lokale opslag van uw browser, uitsluitend op uw eigen apparaat: uw gekozen weergave (donker of licht), uw taal, of u de kaart heeft toegestaan en of u de cookiemelding heeft gesloten. Deze gegevens verlaten uw apparaat nooit.</p>

      <h2>De kaart</h2>
      <p>De interactieve kaart op de locatie- en contactpagina wordt <em>pas geladen van Google Maps nadat u dat toestaat</em>. Vanaf dat moment kan Google uw IP-adres verwerken en eigen cookies plaatsen; zie het <a href="https://policies.google.com/privacy?hl=nl" rel="noopener">privacybeleid van Google</a>. Staat u de kaart niet toe, dan wordt er niets van Google geladen.</p>

      <h2>Reserveren</h2>
      <p>Reserveringen verlopen via onze boekingspagina, die wordt verzorgd door SiteMinder (The Booking Button). De gegevens die u daar invult (naam, contactgegevens, verblijfsdata, betaalgegevens) worden verwerkt om uw reservering te sluiten en te beheren. Betaalgegevens worden verwerkt door het boekingsplatform en zijn betaalproviders; deze website ontvangt of bewaart ze nooit.</p>

      <h2>Contact</h2>
      <p>Mailt u ons of gebruikt u het contactformulier, dan gebruiken wij uw gegevens uitsluitend om u te antwoorden. Wij bewaren correspondentie niet langer dan daarvoor en voor onze administratie nodig is.</p>

      <h2>Uw rechten</h2>
      <p>Op grond van de AVG kunt u inzage, correctie of verwijdering van uw persoonsgegevens vragen, en bezwaar maken tegen of beperking vragen van de verwerking. Mail <a href="mailto:info@hotelmayflower.nl">info@hotelmayflower.nl</a>. U kunt ook een klacht indienen bij de Autoriteit Persoonsgegevens.</p>

      <p class="booking-note">Laatst bijgewerkt: juli 2026.</p>
    </div>
  </section>
</main>
"""
write_page("nl", "nl/privacy/index.html",
           "Privacy- & Cookiebeleid | Hotel Mayflower Leiden",
           "Hoe Hotel Mayflower Leiden met uw gegevens omgaat: geen trackingcookies, alleen functionele voorkeuren, kaart op basis van toestemming en uw AVG-rechten.",
           None, "/nl/privacy/", "/en/privacy/", privacy_body,
           crumb_ld(("Home", "/nl/"), ("Privacy & cookies", "/nl/privacy/")))


# ---------------- Voorwaarden ----------------
terms_body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      {crumbs(("Home", "/nl/"), ("Algemene voorwaarden", None))}
      <p class="eyebrow">Juridisch</p>
      <h1>Algemene voorwaarden</h1>
      <p class="lede">De huisafspraken die het hotel prettig houden voor iedereen.</p>
    </div>
  </div>
  <section class="section" style="padding-top:0">
    <div class="container" style="max-width:46rem">
      <h2>Reserveren en betalen</h2>
      <p>Reserveringen komen tot stand via onze boekingspagina en vallen onder de daar getoonde tariefvoorwaarden op het moment van boeken, inclusief het geldende annuleringsbeleid. Wij accepteren uitsluitend pinbetalingen; contant geld wordt in het hotel niet geaccepteerd.</p>

      <h2>Aankomst en vertrek</h2>
      <p>Inchecken kan van 15:00 tot 18:00 uur; aankomst na 18:00 uur is mogelijk via onze sleutelkluis, mits vooraf afgesproken. Uitchecken uiterlijk om 10:30 uur. Hotelsleutels blijven eigendom van het hotel; lever ze bij vertrek in bij de receptie.</p>

      <h2>Huisregels</h2>
      <ul>
        <li>Alle kamers en binnenruimtes zijn rookvrij. Bij overtreding worden schoonmaakkosten in rekening gebracht.</li>
        <li>Huisdieren zijn niet toegestaan.</li>
        <li>Respecteer de nachtrust van andere gasten en van onze buren.</li>
        <li>Aanwijzingen van het hotelpersoneel, gegeven in het belang van veiligheid en goede orde, dienen te worden opgevolgd.</li>
        <li>Het gebruik of bezit van drugs en het dragen van wapens zijn verboden. Bij overtreding volgt verwijdering en waar nodig melding bij de politie.</li>
      </ul>

      <h2>Aansprakelijkheid</h2>
      <p>Het hotel aanvaardt geen aansprakelijkheid voor verlies van of schade aan eigendommen van gasten, behalve waar dwingend Nederlands recht anders bepaalt. Schade aan hoteleigendommen veroorzaakt door een gast wordt in rekening gebracht. Meubilair en andere hoteleigendommen blijven in het hotel.</p>

      <h2>Toepasselijk recht</h2>
      <p>Op alle overeenkomsten met Hotel Mayflower is Nederlands recht van toepassing. Daarnaast kunnen de Uniforme Voorwaarden Horeca van toepassing zijn op hotelovereenkomsten in Nederland.</p>

      <p class="booking-note">Laatst bijgewerkt: juli 2026.</p>
    </div>
  </section>
</main>
"""
write_page("nl", "nl/voorwaarden/index.html",
           "Algemene Voorwaarden | Hotel Mayflower Leiden",
           "Boekingsvoorwaarden en huisregels van Hotel Mayflower Leiden: betalen, aankomst en vertrek, rookvrij beleid en aansprakelijkheid.",
           None, "/nl/voorwaarden/", "/en/terms/", terms_body,
           crumb_ld(("Home", "/nl/"), ("Algemene voorwaarden", "/nl/voorwaarden/")))

print("NL pages done.")
