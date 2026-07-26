/* Hotel Mayflower — shared behaviour
   Theme · language memory · mobile menu · booking bar · reveals · consent map · contact form
   No dependencies. Everything degrades gracefully without JavaScript. */
(function () {
  "use strict";

  var doc = document.documentElement;
  var LANG = doc.lang === "nl" ? "nl" : "en";

  /* ---------- Configuration ---------- */
  // Contact form: paste a form endpoint here (e.g. Formspree/Basin URL) to switch
  // from the mailto fallback to a real POST. See CONTENT-GUIDE.md.
  var FORM_ENDPOINT = "";
  var BOOKING_URL = "https://direct-book.com/properties/HotelMayflowerDirect";

  /* ---------- Theme toggle (initial theme is set inline in <head>) ---------- */
  function initTheme() {
    var btns = document.querySelectorAll(".theme-toggle");
    btns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var next = doc.getAttribute("data-theme") === "light" ? "dark" : "light";
        doc.classList.add("theme-anim");
        doc.setAttribute("data-theme", next);
        try { localStorage.setItem("hm-theme", next); } catch (e) {}
        window.setTimeout(function () { doc.classList.remove("theme-anim"); }, 700);
      });
    });
    // Follow OS changes only when the visitor has not chosen explicitly
    if (window.matchMedia) {
      window.matchMedia("(prefers-color-scheme: light)").addEventListener("change", function (e) {
        var stored = null;
        try { stored = localStorage.getItem("hm-theme"); } catch (err) {}
        if (!stored) doc.setAttribute("data-theme", e.matches ? "light" : "dark");
      });
    }
  }

  /* ---------- Language memory (used by the root redirect) ---------- */
  function rememberLanguage() {
    try { localStorage.setItem("hm-lang", LANG); } catch (e) {}
  }

  /* ---------- Sticky header ---------- */
  function initHeader() {
    var header = document.querySelector(".site-header");
    if (!header) return;
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 24);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- Mobile menu ---------- */
  function initMenu() {
    var btn = document.querySelector(".menu-btn");
    var menu = document.getElementById("mobile-menu");
    if (!btn || !menu) return;
    function setOpen(open) {
      btn.setAttribute("aria-expanded", String(open));
      menu.classList.toggle("is-open", open);
      document.body.classList.toggle("menu-open", open);
      if (open) {
        var first = menu.querySelector("a");
        if (first) first.focus({ preventScroll: true });
      } else {
        btn.focus({ preventScroll: true });
      }
    }
    btn.addEventListener("click", function () {
      setOpen(btn.getAttribute("aria-expanded") !== "true");
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("is-open")) setOpen(false);
    });
  }

  /* ---------- Booking bar → SiteMinder deep link ---------- */
  function initBooking() {
    var form = document.getElementById("booking-form");
    if (!form) return;
    var ci = form.querySelector('[name="checkin"]');
    var co = form.querySelector('[name="checkout"]');
    var guests = form.querySelector('[name="guests"]');

    var today = new Date();
    var iso = function (d) { return d.toISOString().slice(0, 10); };
    ci.min = iso(today);
    var tomorrow = new Date(today.getTime() + 864e5);
    co.min = iso(tomorrow);

    ci.addEventListener("change", function () {
      if (ci.value) {
        var next = new Date(ci.value);
        next = new Date(next.getTime() + 864e5);
        co.min = iso(next);
        if (co.value && co.value <= ci.value) co.value = iso(next);
      }
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var url = BOOKING_URL + "?locale=" + LANG + "&currency=EUR";
      if (ci.value) url += "&checkInDate=" + encodeURIComponent(ci.value);
      if (co.value) url += "&checkOutDate=" + encodeURIComponent(co.value);
      if (guests && guests.value) url += "&adults=" + encodeURIComponent(guests.value);
      window.open(url, "_blank", "noopener");
    });
  }

  /* Plain "book now" links: append locale so the engine opens in the right language */
  function initBookLinks() {
    document.querySelectorAll('a[href^="' + BOOKING_URL + '"]').forEach(function (a) {
      try {
        var u = new URL(a.href);
        if (!u.searchParams.has("locale")) u.searchParams.set("locale", LANG);
        if (!u.searchParams.has("currency")) u.searchParams.set("currency", "EUR");
        a.href = u.toString();
      } catch (e) {}
    });
  }

  /* ---------- Scroll reveals ---------- */
  function initReveals() {
    var els = document.querySelectorAll(".reveal");
    if (!els.length) return;
    if (!("IntersectionObserver" in window) ||
        window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      els.forEach(function (el) { el.classList.add("is-visible"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        // Reveal when entering the viewport — or when already scrolled past
        // (fast scrolling can skip the intersection entirely).
        if (entry.isIntersecting || entry.boundingClientRect.top < 0) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    els.forEach(function (el) { io.observe(el); });
    // Safety net: on every scroll end, reveal anything the observer missed.
    var sweep = function () {
      els.forEach(function (el) {
        if (!el.classList.contains("is-visible") &&
            el.getBoundingClientRect().top < window.innerHeight) {
          el.classList.add("is-visible");
        }
      });
    };
    window.addEventListener("scrollend", sweep);
    window.addEventListener("scroll", function () {
      window.clearTimeout(sweep._t);
      sweep._t = window.setTimeout(sweep, 180);
    }, { passive: true });
  }

  /* ---------- Ambient videos: play only while visible ---------- */
  function initVideos() {
    var vids = document.querySelectorAll("video[autoplay]");
    if (!vids.length) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      vids.forEach(function (v) { v.removeAttribute("autoplay"); v.pause(); });
      return;
    }
    var play = function (v) { var p = v.play(); if (p && p.catch) p.catch(function () {}); };
    if (!("IntersectionObserver" in window)) { vids.forEach(play); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) play(entry.target);
        else entry.target.pause();
      });
    }, { threshold: 0.2 });
    vids.forEach(function (v) { io.observe(v); });
  }

  /* ---------- Consent-gated map ---------- */
  var MAP_SRC = "https://maps.google.com/maps?q=Hotel%20Mayflower%2C%20Beestenmarkt%202%2C%20Leiden&z=16&output=embed&hl=";
  function loadMap(container) {
    var iframe = document.createElement("iframe");
    iframe.src = MAP_SRC + LANG;
    iframe.title = container.getAttribute("data-map-title") || "Map";
    iframe.loading = "lazy";
    iframe.referrerPolicy = "no-referrer-when-downgrade";
    iframe.allowFullscreen = true;
    var consent = container.querySelector(".map-consent");
    if (consent) consent.remove();
    container.appendChild(iframe);
  }
  function initMap() {
    var containers = document.querySelectorAll(".map-embed");
    if (!containers.length) return;
    var allowed = null;
    try { allowed = localStorage.getItem("hm-map-consent"); } catch (e) {}
    containers.forEach(function (c) {
      if (allowed === "yes") { loadMap(c); return; }
      var btn = c.querySelector(".map-consent button");
      if (btn) btn.addEventListener("click", function () {
        try { localStorage.setItem("hm-map-consent", "yes"); } catch (e) {}
        document.querySelectorAll(".map-embed").forEach(loadMap);
      });
    });
  }

  /* ---------- Cookie banner (functional-only site; banner explains the map) ---------- */
  function initCookieBanner() {
    var banner = document.getElementById("cookie-banner");
    if (!banner) return;
    var seen = null;
    try { seen = localStorage.getItem("hm-cookie-seen"); } catch (e) {}
    if (!seen) banner.classList.add("is-visible");
    banner.querySelectorAll("button").forEach(function (b) {
      b.addEventListener("click", function () {
        try { localStorage.setItem("hm-cookie-seen", "yes"); } catch (e) {}
        if (b.getAttribute("data-consent") === "yes") {
          try { localStorage.setItem("hm-map-consent", "yes"); } catch (e) {}
          document.querySelectorAll(".map-embed").forEach(loadMap);
        }
        banner.classList.remove("is-visible");
      });
    });
  }

  /* ---------- Contact form ---------- */
  function initContactForm() {
    var form = document.getElementById("contact-form");
    if (!form) return;
    var status = form.querySelector(".form-status");
    var t = {
      en: {
        ok: "Thank you — your message has been sent. We reply within one working day.",
        err: "Something went wrong while sending. Please email us directly at info@hotelmayflower.nl.",
        mail: "Your email app will open with the message ready to send."
      },
      nl: {
        ok: "Dank u wel — uw bericht is verzonden. Wij reageren binnen één werkdag.",
        err: "Er ging iets mis bij het verzenden. Mail ons gerust rechtstreeks via info@hotelmayflower.nl.",
        mail: "Uw e-mailprogramma opent met het bericht klaar om te verzenden."
      }
    }[LANG];

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = new FormData(form);
      // Honeypot: real visitors never fill this field
      if (data.get("website")) return;

      if (FORM_ENDPOINT) {
        fetch(FORM_ENDPOINT, { method: "POST", body: data, headers: { Accept: "application/json" } })
          .then(function (r) {
            status.className = "form-status " + (r.ok ? "ok" : "err");
            status.textContent = r.ok ? t.ok : t.err;
            if (r.ok) form.reset();
          })
          .catch(function () {
            status.className = "form-status err";
            status.textContent = t.err;
          });
      } else {
        var subject = (LANG === "nl" ? "Vraag via hotelmayflower.nl — " : "Enquiry via hotelmayflower.nl — ") + (data.get("name") || "");
        var lines = [];
        data.forEach(function (v, k) {
          if (k !== "website" && v) lines.push(k + ": " + v);
        });
        window.location.href = "mailto:info@hotelmayflower.nl?subject=" +
          encodeURIComponent(subject) + "&body=" + encodeURIComponent(lines.join("\n"));
        status.className = "form-status ok";
        status.textContent = t.mail;
      }
    });
  }

  /* ---------- Init ---------- */
  rememberLanguage();
  initTheme();
  initHeader();
  initMenu();
  initBooking();
  initBookLinks();
  initReveals();
  initVideos();
  initMap();
  initCookieBanner();
  initContactForm();
})();
