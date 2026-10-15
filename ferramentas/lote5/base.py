"""Base visual do Lomax para carrosséis (1080x1350) e quadros de Reels (1080x1920)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(ROOT, "node_modules/@fontsource/barlow/files")

def font_faces():
    css = []
    for w in (400, 500, 600, 700, 800, 900):
        for st in ("normal", "italic"):
            css.append(
                f"@font-face{{font-family:'Barlow';font-weight:{w};font-style:{st};"
                f"src:url('file://{FONTS}/barlow-latin-{w}-{st}.woff2') format('woff2');}}"
            )
    return "\n".join(css)

BLUE = "#0E8DFE"
NAVY = "#0A192C"
LIGHT = "#ECF3FB"

BASE_CSS = font_faces() + f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{font-family:'Barlow',sans-serif;-webkit-font-smoothing:antialiased}}
.s{{position:relative;width:1080px;height:1350px;padding:0 96px;overflow:hidden}}
.dark{{background:{NAVY};color:#fff}}
.light{{background:{LIGHT};color:{NAVY}}}
.stripes{{position:absolute;top:0;right:0;width:280px;height:240px}}
.h{{font-weight:900;font-style:italic;letter-spacing:-1.5px;line-height:1.0}}
.b{{color:#d7e0ec}} .light .b{{color:#3f4d60}}
.blue{{color:{BLUE}}}
.muted{{color:#8796ab}} .light .muted{{color:#6a788c}}
.logo{{position:absolute;left:96px;bottom:106px;height:60px}}
.foot{{position:absolute;right:96px;bottom:118px;font-size:24px;font-weight:500;color:#8796ab}}
.count{{position:absolute;right:96px;top:112px;font-size:24px;font-weight:600;color:#8796ab}}
.card{{background:#16253a;border-radius:24px;padding:36px 40px}}
.light .card{{background:#fff;box-shadow:0 10px 30px rgba(10,25,44,.08)}}
.tag{{display:inline-block;font-weight:800;font-size:24px;letter-spacing:2px;text-transform:uppercase;color:{BLUE}}}
.note{{position:absolute;left:96px;right:96px;bottom:190px;font-size:22px;color:#8796ab}}
"""

STRIPES = f"""<svg class="stripes" viewBox="0 0 280 240"><g fill="{BLUE}">
<polygon points="110,0 172,0 62,240 0,240"/><polygon points="206,0 268,0 158,240 96,240"/>
<polygon points="302,0 364,0 254,240 192,240"/></g></svg>"""

def logo(dark=True):
    f = "logo_on_dark.png" if dark else "logo_on_light.png"
    return f'<img class="logo" src="file://{ROOT}/{f}">'

def page(body_html, extra_css="", w=1080, h=1350):
    css = BASE_CSS.replace("width:1080px;height:1350px", f"width:{w}px;height:{h}px")
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css}{extra_css}</style></head><body>{body_html}</body></html>"

def render_pngs(items, outdir, w=1080, h=1350, quality=92):
    """items: list of (name, html). Saves name.jpg in outdir."""
    from playwright.sync_api import sync_playwright
    os.makedirs(outdir, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": w, "height": h})
        for name, html in items:
            path = os.path.join(outdir, name + ".html")
            open(path, "w").write(html)
            pg.goto("file://" + path)
            pg.wait_for_timeout(250)
            pg.evaluate("document.fonts.ready")
            pg.screenshot(path=os.path.join(outdir, name + ".jpg"), type="jpeg", quality=quality)
        b.close()
