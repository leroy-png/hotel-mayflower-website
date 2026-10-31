# Fraud-warning notice pages (Noovy data incident, October 2026).
# Run: python3 tools/gen_notice.py
# Facts are taken strictly from the supplier's incident letter of 31-10-2026;
# update or retire these pages when the situation changes.
from _shared import write_page

EN_BODY = """<main id="main">
  <div class="page-hero">
    <div class="container">
      <p class="eyebrow">Important notice · 31 October 2026</p>
      <h1>Warning: fraudulent messages about hotel bookings</h1>
      <p class="lede">Criminals are sending fake WhatsApp and text messages to hotel guests across Europe, including guests of Hotel Mayflower. This page explains what happened, what we know, and what to do.</p>
    </div>
  </div>

  <section class="section" style="padding-top:0">
    <div class="container" style="max-width:46rem">
      <div class="notice" style="margin-bottom:2.5rem">
        <strong>The most important thing to know: we will never ask you to pay, confirm card details, or click a payment link via WhatsApp, text message or chat.</strong> Payment for your stay happens at the hotel, or through the official booking site you booked with.
      </div>

      <h2>What happened</h2>
      <p>The supplier of our booking and online check-in system was hit by a large automated cyber attack, part of a wave that has affected hotel technology providers across Europe, Asia and Australia in recent weeks. The supplier has informed us that booking details of some reservations may have been accessed during a window of about three hours before the vulnerability was closed.</p>
      <p>The data concerned is limited to booking details: guest name, contact details, booking number and stay dates. <strong>Payment card data was never accessible</strong> &#8212; the supplier does not store it. The incident has been reported to the data protection authorities, and the supplier has closed the vulnerability and is strengthening its security.</p>
      <p>Criminals are combining data like this, from several sources across the industry, to send convincing fake messages: typically a WhatsApp message that greets you by name, mentions a real booking, and asks you to "confirm" or "guarantee" your reservation by paying through a link.</p>

      <h2>How to recognise the fraud</h2>
      <ul>
        <li>A WhatsApp, SMS or chat message about your booking that asks for <strong>payment or card details</strong> &#8212; we never do this.</li>
        <li>Pressure and urgency: "your booking will be cancelled unless you pay within a few hours".</li>
        <li>A link to a payment page, often imitating a well-known booking site.</li>
      </ul>

      <h2>What to do</h2>
      <ul>
        <li><strong>Do not click the link and do not pay.</strong> Block the sender.</li>
        <li>Unsure whether a message about your Hotel Mayflower booking is real? Call us on <a href="tel:+31715142641">+31 71 514 2641</a> (09:00&#8211;18:00) or email <a href="mailto:info@hotelmayflower.nl">info@hotelmayflower.nl</a>. We are happy to check &#8212; that is what we are here for.</li>
        <li>A screenshot of the message (sender number and link visible) helps the investigation; you can send it to us by email.</li>
        <li><strong>If you already paid via such a link:</strong> contact your bank immediately to block your card and dispute the payment, and report the fraud to the police.</li>
      </ul>

      <h2>Your booking remains safe with us</h2>
      <p>Your stay and your reservation are not affected. Nothing changes about checking in, and you do not need to do anything unless you receive a suspicious message. We will update this page if there is any news.</p>
      <p class="booking-note">Published 31 October 2026. Questions? <a href="/en/contact/">Contact us</a>.</p>
    </div>
  </section>
</main>
"""

NL_BODY = """<main id="main">
  <div class="page-hero">
    <div class="container">
      <p class="eyebrow">Belangrijk bericht · 31 oktober 2026</p>
      <h1>Waarschuwing: valse berichten over hotelboekingen</h1>
      <p class="lede">Criminelen sturen valse WhatsApp- en sms-berichten naar hotelgasten in heel Europa, ook naar gasten van Hotel Mayflower. Op deze pagina leest u wat er is gebeurd, wat wij weten en wat u kunt doen.</p>
    </div>
  </div>

  <section class="section" style="padding-top:0">
    <div class="container" style="max-width:46rem">
      <div class="notice" style="margin-bottom:2.5rem">
        <strong>Het belangrijkste om te weten: wij vragen u nooit via WhatsApp, sms of chat om te betalen, kaartgegevens te bevestigen of op een betaallink te klikken.</strong> Betalen doet u in het hotel, of via de officiële boekingssite waar u heeft geboekt.
      </div>

      <h2>Wat er is gebeurd</h2>
      <p>De leverancier van ons boekings- en online-inchecksysteem is getroffen door een grootschalige geautomatiseerde cyberaanval, onderdeel van een golf die de afgelopen weken hoteltechnologie-leveranciers in Europa, Azië en Australië heeft geraakt. De leverancier heeft ons laten weten dat boekingsgegevens van een deel van de reserveringen mogelijk zijn ingezien, gedurende een periode van ongeveer drie uur voordat het lek werd gedicht.</p>
      <p>Het gaat uitsluitend om boekingsgegevens: naam, contactgegevens, boekingsnummer en verblijfsdata. <strong>Betaalkaartgegevens waren op geen enkel moment toegankelijk</strong> &#8212; die worden daar niet opgeslagen. Het incident is gemeld bij de privacytoezichthouder, het lek is gedicht en de beveiliging wordt verder aangescherpt.</p>
      <p>Criminelen combineren dit soort gegevens uit meerdere bronnen in de reisbranche om overtuigende valse berichten te sturen: meestal een WhatsApp-bericht dat u met uw naam aanspreekt, een echte boeking noemt en u vraagt uw reservering te "bevestigen" of te "garanderen" door via een link te betalen.</p>

      <h2>Zo herkent u de fraude</h2>
      <ul>
        <li>Een WhatsApp-, sms- of chatbericht over uw boeking waarin om <strong>betaling of kaartgegevens</strong> wordt gevraagd &#8212; dat doen wij nooit.</li>
        <li>Druk en haast: "uw boeking wordt geannuleerd als u niet binnen enkele uren betaalt".</li>
        <li>Een link naar een betaalpagina, vaak nagemaakt van een bekende boekingssite.</li>
      </ul>

      <h2>Wat u kunt doen</h2>
      <ul>
        <li><strong>Klik niet op de link en betaal niet.</strong> Blokkeer de afzender.</li>
        <li>Twijfelt u of een bericht over uw boeking bij Hotel Mayflower echt is? Bel ons op <a href="tel:+31715142641">+31 71 514 2641</a> (09:00&#8211;18:00 uur) of mail <a href="mailto:info@hotelmayflower.nl">info@hotelmayflower.nl</a>. Wij controleren het graag voor u.</li>
        <li>Een schermafbeelding van het bericht (met afzendernummer en link zichtbaar) helpt bij het onderzoek; u kunt die naar ons mailen.</li>
        <li><strong>Heeft u al via zo'n link betaald?</strong> Neem direct contact op met uw bank om uw kaart te blokkeren en de betaling te betwisten, en doe aangifte bij de politie.</li>
      </ul>

      <h2>Uw boeking blijft gewoon staan</h2>
      <p>Uw verblijf en uw reservering zijn niet in gevaar. Er verandert niets aan het inchecken en u hoeft niets te doen, tenzij u een verdacht bericht ontvangt. Zodra er nieuws is, werken wij deze pagina bij.</p>
      <p class="booking-note">Gepubliceerd 31 oktober 2026. Vragen? <a href="/nl/contact/">Neem contact op</a>.</p>
    </div>
  </section>
</main>
"""

write_page("en", "en/fraud-alert/index.html",
           "Warning: Fraudulent Booking Messages | Hotel Mayflower Leiden",
           "Fake WhatsApp and text messages about hotel bookings are circulating. "
           "Hotel Mayflower never asks you to pay via a message link. What happened and what to do.",
           "/en/hotel-information/", "/en/fraud-alert/", "/nl/fraudewaarschuwing/", EN_BODY)

write_page("nl", "nl/fraudewaarschuwing/index.html",
           "Waarschuwing: Valse Berichten over Boekingen | Hotel Mayflower Leiden",
           "Er zijn valse WhatsApp- en sms-berichten over hotelboekingen in omloop. "
           "Hotel Mayflower vraagt u nooit via een berichtlink om te betalen. Wat er speelt en wat u kunt doen.",
           "/nl/hotelinformatie/", "/nl/fraudewaarschuwing/", "/en/fraud-alert/", NL_BODY)
