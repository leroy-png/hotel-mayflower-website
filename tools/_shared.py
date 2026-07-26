# Hotel Mayflower site — one-time page generator (shared templates).
# The deliverable is the plain HTML this writes; edit pages directly afterwards,
# or edit the body strings here and re-run gen_en.py / gen_nl.py.
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = "https://direct-book.com/properties/HotelMayflowerDirect"
DOMAIN = "https://www.hotelmayflower.nl"

NAV = {
    "en": [("Home", "/en/"), ("Rooms", "/en/rooms/"), ("Leiden", "/en/leiden/"),
           ("Hotel information", "/en/hotel-information/"), ("Contact", "/en/contact/")],
    "nl": [("Home", "/nl/"), ("Kamers", "/nl/kamers/"), ("Leiden", "/nl/leiden/"),
           ("Hotelinformatie", "/nl/hotelinformatie/"), ("Contact", "/nl/contact/")],
}

STR = {
    "en": dict(skip="Skip to content", book="Book now", menu="Menu",
               theme="Switch between dark and light mode", brand_home="Hotel Mayflower — home",
               footer_tag="A welcoming two-star hotel in the historic heart of Leiden, five minutes on foot from Leiden Central Station.",
               visit="Visit", contact="Contact", direct="Book direct", check="Check availability",
               faq_label="FAQ", leiden_label="Leiden & location", info_label="Hotel information",
               rooms_label="Rooms", contact_label="Contact",
               faq_url="/en/faq/", privacy="Privacy & cookies", privacy_url="/en/privacy/",
               terms="Terms & conditions", terms_url="/en/terms/",
               nl_country="The Netherlands",
               copyright="© 2026 Hotel Mayflower, Leiden. All rights reserved.",
               cookie="This site stores only your preferences (theme, language) on your own device. The interactive map loads from Google Maps once you allow it.",
               cookie_yes="Allow map", cookie_no="Essentials only"),
    "nl": dict(skip="Naar de inhoud", book="Boek nu", menu="Menu",
               theme="Wissel tussen donkere en lichte weergave", brand_home="Hotel Mayflower — startpagina",
               footer_tag="Een gastvrij tweesterrenhotel in het historische hart van Leiden, op vijf minuten lopen van Leiden Centraal.",
               visit="Ontdek", contact="Contact", direct="Direct boeken", check="Beschikbaarheid bekijken",
               faq_label="Veelgestelde vragen", leiden_label="Leiden & omgeving", info_label="Hotelinformatie",
               rooms_label="Kamers", contact_label="Contact",
               faq_url="/nl/veelgestelde-vragen/", privacy="Privacy & cookies", privacy_url="/nl/privacy/",
               terms="Algemene voorwaarden", terms_url="/nl/voorwaarden/",
               nl_country="Nederland",
               copyright="© 2026 Hotel Mayflower, Leiden. Alle rechten voorbehouden.",
               cookie="Deze website bewaart alleen uw voorkeuren (weergave, taal) op uw eigen apparaat. De interactieve kaart wordt pas geladen van Google Maps zodra u dat toestaat.",
               cookie_yes="Kaart toestaan", cookie_no="Alleen noodzakelijk"),
}


def head(lang, title, desc, path, alt_path, extra_jsonld="", og_title=None, og_desc=None):
    other = "nl" if lang == "en" else "en"
    xdef = path if lang == "en" else alt_path
    og_title = og_title or title
    og_desc = og_desc or desc
    return f"""<!DOCTYPE html>
<html lang="{lang}" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{path}">
<link rel="alternate" hreflang="{lang}" href="{DOMAIN}{path}">
<link rel="alternate" hreflang="{other}" href="{DOMAIN}{alt_path}">
<link rel="alternate" hreflang="x-default" href="{DOMAIN}{xdef}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Hotel Mayflower Leiden">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:image" content="{DOMAIN}/assets/img/og-hotel-mayflower.jpg">
<meta property="og:url" content="{DOMAIN}{path}">
<link rel="icon" href="/assets/logo/favicon-32.png" type="image/png">
<link rel="icon" href="/assets/logo/beeldmerk_gold.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/logo/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/css/main.css">
<script>(function(){{try{{var t=localStorage.getItem("hm-theme");if(!t)t=window.matchMedia&&matchMedia("(prefers-color-scheme: light)").matches?"light":"dark";document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}}})();</script>
{extra_jsonld}</head>
"""


def header(lang, active, path, alt_path, body_class=""):
    s = STR[lang]
    CUR = ' aria-current="page"'
    nav_items = "\n".join(
        f'        <li><a href="{url}"{CUR if url == active else ""}>{label}</a></li>'
        for label, url in NAV[lang])
    mob_items = "\n".join(
        f'    <li><a class="nav-link" href="{url}"{CUR if url == active else ""}>{label}</a></li>'
        for label, url in NAV[lang])
    en_path = path if lang == "en" else alt_path
    nl_path = alt_path if lang == "en" else path
    en_cur = ' aria-current="true"' if lang == "en" else ""
    nl_cur = ' aria-current="true"' if lang == "nl" else ""
    return f"""<body{f' class="{body_class}"' if body_class else ""}>
<a class="skip-link" href="#main">{s['skip']}</a>

<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="/{lang}/" aria-label="{s['brand_home']}">
      <span class="brand-lockup logo-dark">
        <img class="ship" src="/assets/logo/beeldmerk_gold.svg" alt="" width="57" height="65">
        <img class="wordmark" src="/assets/logo/text_gold.svg" alt="Hotel Mayflower" width="88" height="38">
      </span>
      <img class="logo-light" src="/assets/logo/logo-horiz-goldink.svg" alt="Hotel Mayflower" width="196" height="65">
    </a>
    <nav class="main-nav" aria-label="Main">
      <ul>
{nav_items}
      </ul>
    </nav>
    <div class="header-tools">
      <div class="lang-switch" aria-label="Language">
        <a href="{en_path}"{en_cur} lang="en" hreflang="en">EN</a>
        <a href="{nl_path}"{nl_cur} lang="nl" hreflang="nl">NL</a>
      </div>
      <button class="theme-toggle" type="button" aria-label="{s['theme']}">
        <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.4M12 19.1v2.4M2.5 12h2.4M19.1 12h2.4M5 5l1.7 1.7M17.3 17.3 19 19M19 5l-1.7 1.7M6.7 17.3 5 19"/></svg>
        <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M20.4 14.2A8.6 8.6 0 0 1 9.8 3.6a8.6 8.6 0 1 0 10.6 10.6Z"/></svg>
      </button>
      <a class="btn btn-gold header-book" href="{BOOK}" rel="noopener">{s['book']}</a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="{s['menu']}">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>

<nav class="mobile-menu" id="mobile-menu" aria-label="Mobile">
  <ul>
{mob_items}
    <li><a class="btn btn-gold menu-book" href="{BOOK}" rel="noopener">{s['book']}</a></li>
  </ul>
</nav>
"""


def footer(lang, path, alt_path):
    s = STR[lang]
    root = f"/{lang}/"
    rooms = NAV[lang][1][1]
    leiden = NAV[lang][2][1]
    info = NAV[lang][3][1]
    contact = NAV[lang][4][1]
    en_path = path if lang == "en" else alt_path
    nl_path = alt_path if lang == "en" else path
    en_cur = ' aria-current="true"' if lang == "en" else ""
    nl_cur = ' aria-current="true"' if lang == "nl" else ""
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <span class="brand-lockup logo-dark">
          <img class="ship" src="/assets/logo/beeldmerk_gold.svg" alt="" width="57" height="65">
          <img class="wordmark" src="/assets/logo/text_gold.svg" alt="Hotel Mayflower" width="97" height="42">
        </span>
        <img class="logo-light" src="/assets/logo/logo-horiz-goldink.svg" alt="Hotel Mayflower" width="176" height="58">
        <p>{s['footer_tag']}</p>
      </div>
      <div>
        <h4>{s['visit']}</h4>
        <ul>
          <li><a href="{rooms}">{s['rooms_label']}</a></li>
          <li><a href="{leiden}">{s['leiden_label']}</a></li>
          <li><a href="{info}">{s['info_label']}</a></li>
          <li><a href="{s['faq_url']}">{s['faq_label']}</a></li>
          <li><a href="{contact}">{s['contact_label']}</a></li>
        </ul>
      </div>
      <div>
        <h4>{s['contact']}</h4>
        <ul>
          <li>Beestenmarkt 2<br>2312 CC Leiden<br>{s['nl_country']}</li>
          <li><a href="tel:+31715142641">+31 71 514 2641</a></li>
          <li><a href="mailto:info@hotelmayflower.nl">info@hotelmayflower.nl</a></li>
        </ul>
      </div>
      <div>
        <h4>{s['direct']}</h4>
        <ul>
          <li><a href="{BOOK}" rel="noopener">{s['check']}</a></li>
        </ul>
        <div class="lang-switch" style="margin-top:1.2rem" aria-label="Language">
          <a href="{en_path}"{en_cur} lang="en" hreflang="en">EN</a>
          <a href="{nl_path}"{nl_cur} lang="nl" hreflang="nl">NL</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>{s['copyright']}</p>
      <ul>
        <li><a href="{s['privacy_url']}">{s['privacy']}</a></li>
        <li><a href="{s['terms_url']}">{s['terms']}</a></li>
      </ul>
    </div>
  </div>
</footer>

<div class="cookie-banner" id="cookie-banner" role="dialog" aria-label="Cookies">
  <p>{s['cookie']}</p>
  <div class="row">
    <button class="btn btn-gold" type="button" data-consent="yes">{s['cookie_yes']}</button>
    <button class="btn btn-ghost" type="button" data-consent="no">{s['cookie_no']}</button>
  </div>
</div>

<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


def picture(name, alt, sizes="(min-width: 760px) 30vw, 92vw", widths=(480, 960), lazy=True):
    av = ", ".join(f"/assets/img/{name}-{w}.avif {w}w" for w in widths)
    wp = ", ".join(f"/assets/img/{name}-{w}.webp {w}w" for w in widths)
    jp = ", ".join(f"/assets/img/{name}-{w}.jpg {w}w" for w in widths)
    mid = widths[min(1, len(widths) - 1)]
    loading = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    return f"""<picture>
  <source type="image/avif" srcset="{av}" sizes="{sizes}">
  <source type="image/webp" srcset="{wp}" sizes="{sizes}">
  <img src="/assets/img/{name}-{mid}.jpg" srcset="{jp}" sizes="{sizes}" alt="{alt}"{loading}>
</picture>"""


def write_page(lang, rel, title, desc, active, path, alt_path, body,
               jsonld="", body_class="", og_title=None, og_desc=None):
    html = (head(lang, title, desc, path, alt_path, jsonld, og_title, og_desc)
            + header(lang, active, path, alt_path, body_class)
            + body
            + footer(lang, path, alt_path))
    out = os.path.join(ROOT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", rel)
