# Guest guide (QR page) — one data set, both languages.
# Run: python3 tools/gen_guide.py
#
# Walking times are measured from Beestenmarkt 2 and rounded; they are marked
# with "±" everywhere. Facts with a date (F1, Keukenhof, parking tariffs) carry
# a "checked" note so it is obvious when they need refreshing.
from _shared import write_page, BOOK, DOMAIN

HOTEL = "Beestenmarkt 2, Leiden"
CHECKED_EN = "checked August 2026"
CHECKED_NL = "gecontroleerd augustus 2026"


def walk(dest):
    """Google Maps walking directions from the hotel to a destination."""
    return ("https://www.google.com/maps/dir/?api=1&origin="
            + HOTEL.replace(" ", "+").replace(",", "%2C")
            + "&destination=" + dest.replace(" ", "+").replace(",", "%2C")
            + "&travelmode=walking")


def search(query):
    """Google Maps search around the hotel — always shows live ratings."""
    return ("https://www.google.com/maps/search/?api=1&query="
            + query.replace(" ", "+").replace(",", "%2C"))


# ---------------------------------------------------------------- data
# (key, minutes, name, maps destination, website, EN blurb, NL blurb)
MUSEUMS = [
    ("valk", 3, "Molenmuseum De Valk", "Molenmuseum De Valk, Leiden",
     "https://molenmuseumdevalk.nl/",
     "A working seven-storey windmill from 1743 on the edge of the old town. Climb to the balcony for the best free-standing view over Leiden.",
     "Een werkende korenmolen uit 1743 aan de rand van de oude stad. Klim naar de omloop voor het mooiste vrijstaande uitzicht over Leiden."),
    ("lakenhal", 4, "Museum De Lakenhal", "Museum De Lakenhal, Leiden",
     "https://www.lakenhal.nl/",
     "Leiden's own museum, in the seventeenth-century cloth hall: Rembrandt's earliest work, Lucas van Leyden, and the story of the city's cloth trade.",
     "Het museum van de stad zelf, in de zeventiende-eeuwse lakenhal: het vroegste werk van Rembrandt, Lucas van Leyden en het verhaal van het Leidse laken."),
    ("wereldmuseum", 5, "Wereldmuseum Leiden", "Wereldmuseum Leiden, Steenstraat",
     "https://leiden.wereldmuseum.nl/",
     "One of Europe's oldest ethnographic collections (until recently Museum Volkenkunde), telling the stories of cultures worldwide.",
     "Een van de oudste volkenkundige collecties van Europa (tot voor kort Museum Volkenkunde), met verhalen van culturen over de hele wereld."),
    ("boerhaave", 9, "Rijksmuseum Boerhaave", "Rijksmuseum Boerhaave, Leiden",
     "https://www.rijksmuseumboerhaave.nl/",
     "Five centuries of Dutch science and medicine, from the first microscopes to the anatomical theatre. Surprisingly gripping, even if science is not your thing.",
     "Vijf eeuwen Nederlandse wetenschap en geneeskunde, van de eerste microscopen tot het anatomisch theater. Verrassend meeslepend, ook als u niets met wetenschap heeft."),
    ("rmo", 10, "Rijksmuseum van Oudheden", "Rijksmuseum van Oudheden, Leiden",
     "https://www.rmo.nl/",
     "The national museum of antiquities: an entire Egyptian temple stands in the entrance hall, plus Greek, Roman and Dutch archaeology.",
     "Het rijksmuseum voor archeologie: in de entreehal staat een complete Egyptische tempel, daarnaast Griekse, Romeinse en Nederlandse archeologie."),
    ("siebold", 10, "Japanmuseum SieboldHuis", "Japanmuseum SieboldHuis, Leiden",
     "https://www.sieboldhuis.org/",
     "The canal house where Philipp von Siebold displayed the objects he brought back from Japan in 1832: Japanese art in a Dutch merchant's house.",
     "Het grachtenpand waar Philipp von Siebold in 1832 zijn Japanse verzameling toonde: Japanse kunst in een Nederlands koopmanshuis."),
    ("hortus", 12, "Hortus botanicus Leiden", "Hortus botanicus Leiden",
     "https://hortusleiden.nl/",
     "The oldest botanical garden in the Netherlands (1590), where Clusius planted the tulips that started Dutch tulip mania.",
     "De oudste botanische tuin van Nederland (1590), waar Clusius de tulpen plantte waarmee de Nederlandse tulpenhandel begon."),
    ("naturalis", 22, "Naturalis Biodiversity Center", "Naturalis Biodiversity Center, Leiden",
     "https://www.naturalis.nl/",
     "Dinosaurs, including T. rex 'Trix', and the natural history of the planet. A little further out; bus 400 or a 20-minute walk past the station.",
     "Dinosauriërs, waaronder T. rex 'Trix', en de natuurlijke historie van de aarde. Iets verder weg; bus 400 of twintig minuten lopen voorbij het station."),
]

SIGHTS = [
    ("burcht", 10, "Burcht van Leiden", "Burcht van Leiden",
     "https://www.visitleiden.nl/",
     "An eleventh-century circular fortress on an artificial mound where the Old and New Rhine meet. Free to enter, and the rampart walk gives you the rooftops of the whole old town.",
     "Een elfde-eeuwse ringburcht op een kunstmatige heuvel waar Oude en Nieuwe Rijn samenkomen. Gratis toegankelijk, en vanaf de ringmuur kijkt u over de daken van de hele oude stad."),
    ("pieterskerk", 12, "Pieterskerk", "Pieterskerk, Leiden",
     "https://pieterskerk.com/",
     "The great Gothic church where the Pilgrims worshipped before sailing for America; their leader John Robinson is buried here. Leiden is where the Mayflower story begins, and the hotel is named after that ship.",
     "De grote gotische kerk waar de Pilgrims kerkten voordat zij naar Amerika vertrokken; hun voorganger John Robinson ligt hier begraven. In Leiden begint het Mayflower-verhaal, en aan dat schip dankt dit hotel zijn naam."),
    ("hooglandse", 10, "Hooglandse Kerk", "Hooglandse Kerk, Leiden",
     "https://hooglandsekerk.com/",
     "A soaring late-Gothic church, light and almost empty inside, with a monument to the burgomaster who kept the city fed during the 1574 siege.",
     "Een hoog oprijzende laatgotische kerk, licht en bijna leeg van binnen, met het monument voor de burgemeester die de stad tijdens het beleg van 1574 te eten gaf."),
    ("rapenburg", 10, "Rapenburg", "Rapenburg, Leiden",
     "https://www.visitleiden.nl/",
     "Often called the most beautiful canal in the Netherlands: wide water, lime trees and the seventeenth-century houses of professors and merchants. The university's oldest building stands here.",
     "Vaak de mooiste gracht van Nederland genoemd: breed water, lindebomen en de zeventiende-eeuwse huizen van hoogleraren en kooplieden. Hier staat ook het oudste gebouw van de universiteit."),
    ("hofjes", 8, "Leiden's hofjes", "Hofje van Brouchoven, Leiden",
     "https://www.visitleiden.nl/",
     "Leiden has around 35 hidden almshouse courtyards, built from the 1400s onward for elderly residents. Push open an unmarked door and you find a silent garden. Please keep your voice down; people live there.",
     "Leiden telt zo'n 35 verborgen hofjes, vanaf de vijftiende eeuw gebouwd voor ouderen. Achter een onopvallende deur ligt ineens een stille tuin. Houd het rustig; er wonen mensen."),
    ("stadhuis", 8, "Stadhuis & Koornbrug", "Stadhuis Leiden",
     "https://www.visitleiden.nl/",
     "The Renaissance town hall façade on the Breestraat, and round the corner the covered Koornbrug where grain was traded out of the rain.",
     "De renaissancegevel van het stadhuis aan de Breestraat, en om de hoek de overdekte Koornbrug waar graan droog verhandeld werd."),
]

# Restaurants: we deliberately link to Google Maps rather than printing a rating
# that would be out of date next month. The Maps link always shows the live
# score, opening hours and reviews.
FOOD = [
    ("Dutch & modern European", "Nederlands & modern Europees",
     "restaurant Beestenmarkt Leiden",
     "Around the Beestenmarkt itself: the square the hotel stands on is one of Leiden's liveliest for dinner and drinks.",
     "Rondom de Beestenmarkt zelf: het plein waaraan het hotel ligt, is een van de gezelligste plekken van Leiden om te eten en te drinken."),
    ("Italian & pizza", "Italiaans & pizza",
     "Italiaans restaurant Leiden centrum",
     "From simple wood-fired pizza to full Italian dinners, mostly a five-minute walk into the centre.",
     "Van eenvoudige pizza uit de houtoven tot volledige Italiaanse diners, meestal vijf minuten lopen het centrum in."),
    ("Asian: Chinese, Thai, sushi", "Aziatisch: Chinees, Thais, sushi",
     "Aziatisch restaurant Leiden centrum",
     "Several long-established Asian kitchens sit on and around the Beestenmarkt and Steenstraat.",
     "Op en rond de Beestenmarkt en de Steenstraat zitten verschillende vertrouwde Aziatische keukens."),
    ("Burgers, grill & steak", "Burgers, grill & steak",
     "steakhouse burger restaurant Leiden centrum",
     "Straightforward and good for a hungry evening, several within a few minutes' walk.",
     "Eenvoudig en goed voor een hongerige avond, meerdere adressen op een paar minuten lopen."),
    ("Vegetarian & vegan", "Vegetarisch & veganistisch",
     "vegetarisch restaurant Leiden centrum",
     "Leiden is a student city, so meat-free kitchens are easy to find and rarely expensive.",
     "Leiden is een studentenstad, dus vegetarische keukens zijn ruim voorhanden en zelden duur."),
    ("Breakfast, brunch & coffee", "Ontbijt, brunch & koffie",
     "ontbijt brunch koffie Leiden centrum",
     "We do not serve breakfast, but the centre has plenty of places that do; most open from around 08:00.",
     "Wij serveren geen ontbijt, maar in het centrum kunt u op veel plekken terecht; de meeste openen rond 08:00 uur."),
    ("Late-night snack", "Late trek",
     "afhaal snack Leiden centrum open laat",
     "Coming back after a concert or a late dinner? A few places around the centre stay open late.",
     "Laat terug van een concert of diner? Rondom het centrum zijn enkele zaken tot laat open."),
]


def place_card(minutes, name, dest, site, blurb, lang):
    site_label = "Website" if lang == "en" else "Website"
    route = "Walking route" if lang == "en" else "Looproute"
    unit = "min walk" if lang == "en" else "min lopen"
    return f"""        <article class="guide-item reveal">
          <span class="guide-walk">± {minutes} {unit}</span>
          <h3>{name}</h3>
          <p>{blurb}</p>
          <p class="guide-links">
            <a href="{walk(dest)}" rel="noopener nofollow" target="_blank">{route} →</a>
            <a href="{site}" rel="noopener nofollow" target="_blank">{site_label} →</a>
          </p>
        </article>"""


def food_card(title, query, blurb, lang):
    label = "Show on Google Maps" if lang == "en" else "Bekijk op Google Maps"
    return f"""        <article class="guide-item reveal">
          <h3>{title}</h3>
          <p>{blurb}</p>
          <p class="guide-links">
            <a href="{search(query)}" rel="noopener nofollow" target="_blank">{label} →</a>
          </p>
        </article>"""


def build(lang):
    en = lang == "en"
    path = "/en/guide/" if en else "/nl/gids/"
    alt = "/nl/gids/" if en else "/en/guide/"
    checked = CHECKED_EN if en else CHECKED_NL

    museums = "\n".join(place_card(m[1], m[2], m[3], m[4], m[5] if en else m[6], lang) for m in MUSEUMS)
    sights = "\n".join(place_card(s[1], s[2], s[3], s[4], s[5] if en else s[6], lang) for s in SIGHTS)
    food = "\n".join(food_card(f[0] if en else f[1], f[2], f[3] if en else f[4], lang) for f in FOOD)

    if en:
        title = "Guest guide | Leiden tips from Hotel Mayflower"
        desc = ("Everything within walking distance of Hotel Mayflower: museums, restaurants, "
                "historic Leiden, day trips to Keukenhof and Zandvoort, and parking.")
        body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      <p class="eyebrow">For our guests</p>
      <h1>Your guide to Leiden</h1>
      <p class="lede">Everything below starts at our front door on the Beestenmarkt. Walking times are approximate, and every entry opens walking directions in Google Maps.</p>
      <p class="booking-note">Questions? Our reception is open 09:00–18:00, or call <a href="tel:+31715142641">+31 71 514 2641</a>.</p>
    </div>
  </div>

  <section class="section" style="padding-top:0" id="food">
    <div class="container">
      <h2>Where to eat</h2>
      <p class="lede">We would rather point you at the live listings than print a score that is out of date by next month: each link opens Google Maps with current ratings, opening hours and reviews.</p>
      <div class="guide-grid">
{food}
      </div>
    </div>
  </section>

  <section class="section section--tint" id="museums">
    <div class="container">
      <h2>Museums</h2>
      <p class="lede">Leiden has thirteen museums. These are the ones you can reach on foot from the hotel.</p>
      <div class="guide-grid">
{museums}
      </div>
    </div>
  </section>

  <section class="section" id="sights">
    <div class="container">
      <h2>Historic Leiden</h2>
      <p class="lede">The city is small enough to see properly in an afternoon. A short walk in this order makes a good route: Burcht, Hooglandse Kerk, Stadhuis, Rapenburg, Pieterskerk.</p>
      <div class="guide-grid">
{sights}
      </div>
    </div>
  </section>

  <section class="section section--tint" id="daytrips">
    <div class="container">
      <h2>Day trips</h2>
      <div class="grid grid-2" style="margin-top:2rem">
        <div class="tile reveal">
          <h3>Keukenhof &amp; the flower fields</h3>
          <p>The world's largest spring garden, in Lisse. <strong>Keukenhof is a spring attraction only:</strong> the 2027 season runs <strong>18 March to 9 May 2027</strong>. The bulb fields around it are usually at their best from mid-April to early May.</p>
          <p><strong>Getting there:</strong> bus <strong>854</strong> (Keukenhof Express) leaves directly from Leiden Centraal, about four times an hour, roughly 25–30 minutes to the entrance. Combination tickets including entry are sold online. The bus runs during the Keukenhof season only.</p>
          <p class="booking-note">Season dates {checked}; check <a href="https://keukenhof.nl/en/" rel="noopener nofollow" target="_blank">keukenhof.nl</a> before you travel.</p>
          <p class="guide-links"><a href="https://keukenhof.nl/en/" rel="noopener nofollow" target="_blank">Keukenhof website →</a></p>
        </div>
        <div class="tile reveal reveal-d1">
          <h3>Formula 1 at Zandvoort</h3>
          <p>The <strong>Dutch Grand Prix runs 21–23 August 2026</strong> at Circuit Zandvoort, and this is the <strong>final edition</strong> for now, as Zandvoort leaves the calendar in 2027.</p>
          <p><strong>Getting there:</strong> train from Leiden Centraal towards Haarlem and change for Zandvoort aan Zee; roughly an hour in total. On race days trains are very busy and extra services run, so travel early and buy tickets in advance.</p>
          <p class="booking-note">Dates {checked}; confirm at <a href="https://dutchgp.com/" rel="noopener nofollow" target="_blank">dutchgp.com</a>.</p>
          <p class="guide-links"><a href="https://dutchgp.com/" rel="noopener nofollow" target="_blank">Dutch GP website →</a></p>
        </div>
        <div class="tile reveal">
          <h3>The beach</h3>
          <p>Katwijk aan Zee and Noordwijk are the closest stretches of North Sea coast: bus 31 or 32 from Leiden Centraal, around half an hour. Wide sand, dunes and a line of beach cafés in summer.</p>
          <p class="guide-links"><a href="{search('Katwijk aan Zee strand')}" rel="noopener nofollow" target="_blank">Show on Google Maps →</a></p>
        </div>
        <div class="tile reveal reveal-d1">
          <h3>Amsterdam, The Hague &amp; Rotterdam</h3>
          <p>Direct trains from Leiden Centraal, five minutes' walk from the hotel: The Hague about 12 minutes, Amsterdam about 35, Rotterdam about 35, Schiphol about 20.</p>
          <p class="guide-links"><a href="https://www.ns.nl/en" rel="noopener nofollow" target="_blank">Train times (NS) →</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="parking">
    <div class="container split">
      <div class="reveal">
        <h2>Parking: use Haagweg</h2>
        <p>The hotel has no private parking and the old centre was never built for cars. The easiest option is <strong>Parkeerterrein Haagweg</strong> (Haagweg 8), a 750-space car park just outside the centre.</p>
        <p>Best of all, it runs a <strong>free shuttle bus</strong> into town every few minutes, and it will drop you where you ask, including at the Beestenmarkt.</p>
        <ul class="card-meta" style="font-size:1rem;gap:.6rem 1.4rem">
          <li>Shuttle Mon–Wed 06:00–24:00</li>
          <li>Thu &amp; Fri 06:00–02:00</li>
          <li>Sat 07:00–02:00</li>
          <li>Sun 09:00–24:00</li>
        </ul>
        <p>Tariff at the time of writing: first 15 minutes free, up to 90 minutes €4.50, then €1.50 per half hour, maximum €21.00 per day.</p>
        <p class="booking-note">Tariffs and times {checked}; operators change them from time to time. Current rates at <a href="https://www.centrumparkeren.nl/leiden/pr/haagweg" rel="noopener nofollow" target="_blank">centrumparkeren.nl</a>.</p>
        <p class="guide-links"><a href="https://www.google.com/maps/dir/?api=1&amp;destination=Parkeerterrein+Haagweg%2C+Haagweg+8%2C+Leiden&amp;travelmode=driving" rel="noopener nofollow" target="_blank">Drive there →</a></p>
      </div>
      <div class="reveal reveal-d1">
        <div class="booking-bar" style="grid-template-columns:1fr">
          <h3 style="margin:0">Staying another night?</h3>
          <p style="color:var(--muted);margin:0">Booking directly with us is always the best available rate.</p>
          <a class="btn btn-gold" href="{BOOK}" rel="noopener">Check availability</a>
          <a class="btn btn-ghost" href="/en/contact/">Ask us anything</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    else:
        title = "Gastengids | Leidse tips van Hotel Mayflower"
        desc = ("Alles op loopafstand van Hotel Mayflower: musea, restaurants, historisch Leiden, "
                "dagtrips naar Keukenhof en Zandvoort, en parkeren.")
        body = f"""<main id="main">
  <div class="page-hero">
    <div class="container">
      <p class="eyebrow">Voor onze gasten</p>
      <h1>Uw gids voor Leiden</h1>
      <p class="lede">Alles hieronder begint bij onze voordeur aan de Beestenmarkt. Looptijden zijn bij benadering, en elk item opent de looproute in Google Maps.</p>
      <p class="booking-note">Vragen? Onze receptie is geopend van 09:00 tot 18:00 uur, of bel <a href="tel:+31715142641">+31 71 514 2641</a>.</p>
    </div>
  </div>

  <section class="section" style="padding-top:0" id="eten">
    <div class="container">
      <h2>Waar u kunt eten</h2>
      <p class="lede">Liever verwijzen wij u naar de actuele vermeldingen dan dat wij een cijfer afdrukken dat volgende maand niet meer klopt: elke link opent Google Maps met actuele beoordelingen, openingstijden en reviews.</p>
      <div class="guide-grid">
{food}
      </div>
    </div>
  </section>

  <section class="section section--tint" id="musea">
    <div class="container">
      <h2>Musea</h2>
      <p class="lede">Leiden telt dertien musea. Deze bereikt u te voet vanaf het hotel.</p>
      <div class="guide-grid">
{museums}
      </div>
    </div>
  </section>

  <section class="section" id="bezienswaardigheden">
    <div class="container">
      <h2>Historisch Leiden</h2>
      <p class="lede">De stad is klein genoeg om in een middag echt te zien. Een mooie route in deze volgorde: Burcht, Hooglandse Kerk, Stadhuis, Rapenburg, Pieterskerk.</p>
      <div class="guide-grid">
{sights}
      </div>
    </div>
  </section>

  <section class="section section--tint" id="dagtrips">
    <div class="container">
      <h2>Dagtrips</h2>
      <div class="grid grid-2" style="margin-top:2rem">
        <div class="tile reveal">
          <h3>Keukenhof &amp; de bloemenvelden</h3>
          <p>De grootste lentetuin ter wereld, in Lisse. <strong>Keukenhof is uitsluitend in het voorjaar open:</strong> het seizoen 2027 loopt van <strong>18 maart tot en met 9 mei 2027</strong>. De bollenvelden eromheen staan meestal half april tot begin mei op hun mooist.</p>
          <p><strong>Hoe komt u er:</strong> bus <strong>854</strong> (Keukenhof Express) vertrekt rechtstreeks vanaf Leiden Centraal, ongeveer vier keer per uur, in zo'n 25 tot 30 minuten tot de ingang. Online zijn combitickets met entree verkrijgbaar. De bus rijdt alleen tijdens het Keukenhof-seizoen.</p>
          <p class="booking-note">Seizoensdata {checked}; kijk vóór vertrek op <a href="https://keukenhof.nl/nl/" rel="noopener nofollow" target="_blank">keukenhof.nl</a>.</p>
          <p class="guide-links"><a href="https://keukenhof.nl/nl/" rel="noopener nofollow" target="_blank">Website Keukenhof →</a></p>
        </div>
        <div class="tile reveal reveal-d1">
          <h3>Formule 1 op Zandvoort</h3>
          <p>De <strong>Dutch Grand Prix is van 21 tot en met 23 augustus 2026</strong> op Circuit Zandvoort, en dit is voorlopig de <strong>laatste editie</strong>: Zandvoort verdwijnt in 2027 van de kalender.</p>
          <p><strong>Hoe komt u er:</strong> met de trein vanaf Leiden Centraal richting Haarlem en daar overstappen op Zandvoort aan Zee; bij elkaar ongeveer een uur. Op racedagen is het erg druk en rijden er extra treinen; vertrek vroeg en koop uw kaartje vooraf.</p>
          <p class="booking-note">Data {checked}; controleer op <a href="https://dutchgp.com/" rel="noopener nofollow" target="_blank">dutchgp.com</a>.</p>
          <p class="guide-links"><a href="https://dutchgp.com/" rel="noopener nofollow" target="_blank">Website Dutch GP →</a></p>
        </div>
        <div class="tile reveal">
          <h3>Naar het strand</h3>
          <p>Katwijk aan Zee en Noordwijk zijn de dichtstbijzijnde stukken Noordzeekust: bus 31 of 32 vanaf Leiden Centraal, ongeveer een half uur. Breed zand, duinen en in de zomer een rij strandtenten.</p>
          <p class="guide-links"><a href="{search('Katwijk aan Zee strand')}" rel="noopener nofollow" target="_blank">Bekijk op Google Maps →</a></p>
        </div>
        <div class="tile reveal reveal-d1">
          <h3>Amsterdam, Den Haag &amp; Rotterdam</h3>
          <p>Directe treinen vanaf Leiden Centraal, op vijf minuten lopen van het hotel: Den Haag ongeveer 12 minuten, Amsterdam ongeveer 35, Rotterdam ongeveer 35, Schiphol ongeveer 20.</p>
          <p class="guide-links"><a href="https://www.ns.nl/" rel="noopener nofollow" target="_blank">Reisplanner (NS) →</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="parkeren">
    <div class="container split">
      <div class="reveal">
        <h2>Parkeren: kies Haagweg</h2>
        <p>Het hotel heeft geen eigen parkeergelegenheid en de binnenstad is nooit voor auto's gebouwd. De prettigste optie is <strong>Parkeerterrein Haagweg</strong> (Haagweg 8), een terrein met 750 plaatsen net buiten het centrum.</p>
        <p>Het mooiste: er rijdt een <strong>gratis pendelbus</strong> die om de paar minuten naar de stad gaat en u afzet waar u wilt, ook aan de Beestenmarkt.</p>
        <ul class="card-meta" style="font-size:1rem;gap:.6rem 1.4rem">
          <li>Pendelbus ma–wo 06:00–24:00</li>
          <li>do &amp; vr 06:00–02:00</li>
          <li>za 07:00–02:00</li>
          <li>zo 09:00–24:00</li>
        </ul>
        <p>Tarief op het moment van schrijven: eerste 15 minuten gratis, tot 90 minuten € 4,50, daarna € 1,50 per half uur, maximaal € 21,00 per dag.</p>
        <p class="booking-note">Tarieven en tijden {checked}; exploitanten wijzigen deze af en toe. Actuele tarieven op <a href="https://www.centrumparkeren.nl/leiden/pr/haagweg" rel="noopener nofollow" target="_blank">centrumparkeren.nl</a>.</p>
        <p class="guide-links"><a href="https://www.google.com/maps/dir/?api=1&amp;destination=Parkeerterrein+Haagweg%2C+Haagweg+8%2C+Leiden&amp;travelmode=driving" rel="noopener nofollow" target="_blank">Rijroute →</a></p>
      </div>
      <div class="reveal reveal-d1">
        <div class="booking-bar" style="grid-template-columns:1fr">
          <h3 style="margin:0">Nog een nacht blijven?</h3>
          <p style="color:var(--muted);margin:0">Rechtstreeks bij ons boeken is altijd de beste beschikbare prijs.</p>
          <a class="btn btn-gold" href="{BOOK}" rel="noopener">Bekijk beschikbaarheid</a>
          <a class="btn btn-ghost" href="/nl/contact/">Stel ons uw vraag</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""

    write_page(lang, f"{path.strip('/')}/index.html", title, desc,
               "/en/leiden/" if en else "/nl/leiden/", path, alt, body)


build("en")
build("nl")
