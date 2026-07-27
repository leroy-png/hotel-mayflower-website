# Build the deployable site into _site/, optionally prefixing absolute paths.
#
# GitHub Pages serves project sites under /<repo-name>/, while this site is
# written with root-absolute paths (/en/, /assets/...). The deploy workflow
# passes the base path reported by actions/configure-pages; with a custom
# domain that base path is empty and the site is copied through unchanged.
#
# Usage: python3 tools/build_site.py --base "/hotel-mayflower-website"
import argparse
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_site")
COPY = ["en", "nl", "assets", "index.html", "404.html", "robots.txt", "sitemap.xml",
        ".cpanel.yml"]  # cPanel reads this from the deploy branch; rsync excludes it from the webspace


def rewrite_html(path, base, version):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    if base:
        # href="/...", src="/..." and srcset="/..." (leaves https:// and protocol-relative // alone)
        html = re.sub(r'(href|src|srcset|poster)="/(?!/)', rf'\1="{base}/', html)
        # additional srcset candidates after a comma: ", /assets/img/x-960.webp 960w"
        html = re.sub(r'(,\s*)/(assets/)', rf'\1{base}/\2', html)
        # language redirect on the root page
        html = html.replace('location.replace("/" + lang + "/")',
                            f'location.replace("{base}/" + lang + "/")')
    if version:
        # cache-bust CSS/JS: browsers cache Pages assets for 10 min, phones often longer
        html = html.replace("/assets/css/main.css", f"/assets/css/main.css?v={version}")
        html = html.replace("/assets/js/main.js", f"/assets/js/main.js?v={version}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="", help="path prefix, e.g. /hotel-mayflower-website")
    ap.add_argument("--version", default="", help="cache-bust token for CSS/JS (e.g. commit SHA)")
    args = ap.parse_args()
    base = args.base.rstrip("/")
    version = args.version[:8]

    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    for item in COPY:
        src = os.path.join(ROOT, item)
        dst = os.path.join(OUT, item)
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

    n = 0
    if base or version:
        for dirpath, _dirs, files in os.walk(OUT):
            for name in files:
                if name.endswith(".html"):
                    rewrite_html(os.path.join(dirpath, name), base, version)
                    n += 1
    print(f"built _site/ (base={base or '(none)'}, v={version or '(none)'}; {n} pages rewritten)")


if __name__ == "__main__":
    main()
