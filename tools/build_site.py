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
COPY = ["en", "nl", "assets", "index.html", "404.html", "robots.txt", "sitemap.xml"]


def rewrite_html(path, base):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    # href="/...", src="/..." and srcset="/..." (leaves https:// and protocol-relative // alone)
    html = re.sub(r'(href|src|srcset|poster)="/(?!/)', rf'\1="{base}/', html)
    # additional srcset candidates after a comma: ", /assets/img/x-960.webp 960w"
    html = re.sub(r'(,\s*)/(assets/)', rf'\1{base}/\2', html)
    # language redirect on the root page
    html = html.replace('location.replace("/" + lang + "/")',
                        f'location.replace("{base}/" + lang + "/")')
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="", help="path prefix, e.g. /hotel-mayflower-website")
    base = ap.parse_args().base.rstrip("/")

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
    if base:
        for dirpath, _dirs, files in os.walk(OUT):
            for name in files:
                if name.endswith(".html"):
                    rewrite_html(os.path.join(dirpath, name), base)
                    n += 1
    print(f"built _site/ (base={base or '(none)'}; {n} pages rewritten)")


if __name__ == "__main__":
    main()
