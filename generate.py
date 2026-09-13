# -*- coding: utf-8 -*-
"""Generate 100 sector landing pages + an index gallery.

Run:  python3 generate.py
Output: <slug>.html for each of the 100 brands, plus index.html and README.md
"""
import html
import hashlib
import os
import webbrowser

from data import SECTORS, BRANDS, slugify

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- themes ----

THEMES = [
    dict(name="aurora", head="Sora", body="Inter", mode="light",
         bg="#f6f7fc", surface="#ffffff", fg="#101322", muted="#5b6172", border="#e4e7f0",
         radius="20px", btn="999px", shadow="0 1px 2px rgba(18,22,40,.05), 0 10px 30px rgba(18,22,40,.06)",
         hero="center", feats="cards", extra="""
         body{background:
           radial-gradient(720px 420px at 12% -4%, color-mix(in srgb, var(--accent) 16%, transparent), transparent 68%),
           radial-gradient(760px 460px at 88% 2%, color-mix(in srgb, var(--accent2) 15%, transparent), transparent 70%),
           var(--bg);}
         .mock{box-shadow:0 30px 70px rgba(18,22,40,.14)}
         """),
    dict(name="midnight", head="Space Grotesk", body="Inter", mode="dark",
         bg="#0b0f1d", surface="#121829", fg="#eef1fa", muted="#98a0b8", border="#232c47",
         radius="16px", btn="12px", shadow="0 20px 50px rgba(0,0,0,.45)",
         hero="split", feats="tiles", extra="""
         body{background:radial-gradient(900px 500px at 85% -10%, color-mix(in srgb, var(--accent) 20%, transparent), transparent 70%), var(--bg);}
         .hero h1{background:linear-gradient(92deg,var(--fg),color-mix(in srgb, var(--accent) 55%, var(--fg)) 70%, var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent}
         .btn-primary{box-shadow:0 0 0 1px color-mix(in srgb, var(--accent) 40%, transparent), 0 8px 30px color-mix(in srgb, var(--accent) 35%, transparent)}
         """),
    dict(name="editorial", head="Fraunces", body="Inter", mode="light",
         bg="#faf8f3", surface="#ffffff", fg="#1c1a17", muted="#6d675e", border="#e7e2d8",
         radius="6px", btn="4px", shadow="0 1px 2px rgba(30,26,20,.06), 0 12px 34px rgba(30,26,20,.07)",
         hero="center", feats="cards", extra="""
         .kicker{letter-spacing:.22em}
         .hero h1{font-weight:600;letter-spacing:-.01em}
         .badge{border:1px solid var(--border);background:var(--surface)}
         section{border-top:1px solid var(--border)}
         """),
    dict(name="candy", head="Baloo 2", body="Nunito", mode="light",
         bg="#fff8f3", surface="#ffffff", fg="#2a1d33", muted="#77697f", border="#f3e3ee",
         radius="26px", btn="999px", shadow="0 2px 4px rgba(160,80,140,.06), 0 14px 36px rgba(160,80,140,.10)",
         hero="center", feats="tiles", extra="""
         body{background:
           radial-gradient(500px 320px at 8% 0%, #ffe3f0, transparent 65%),
           radial-gradient(600px 360px at 96% 6%, #e3ecff, transparent 65%),
           var(--bg);}
         .feat-icon{border-radius:30% 70% 62% 38%/55% 40% 60% 45%!important}
         """),
    dict(name="corporate", head="IBM Plex Sans", body="IBM Plex Sans", mode="light",
         bg="#ffffff", surface="#f5f7fa", fg="#0e2138", muted="#4d5f75", border="#dde4ec",
         radius="10px", btn="8px", shadow="0 1px 2px rgba(14,33,56,.08)",
         hero="split", feats="cards", extra="""
         .hero{background:linear-gradient(var(--border) 1px, transparent 1px) 0 0/100% 44px,
               linear-gradient(90deg, var(--border) 1px, transparent 1px) 0 0/44px 100%;}
         .nav{border-top:3px solid var(--accent)}
         h1,h2{letter-spacing:-.02em}
         """),
    dict(name="luxe", head="Playfair Display", body="Manrope", mode="dark",
         bg="#141210", surface="#1e1a16", fg="#f4efe6", muted="#a89e8e", border="#332c23",
         radius="4px", btn="2px", shadow="0 24px 60px rgba(0,0,0,.5)",
         hero="center", feats="cards", extra="""
         .badge{border:1px solid color-mix(in srgb, var(--accent) 45%, transparent);color:var(--fg);background:transparent}
         .hero h1{font-weight:500}
         .plan.featured{border:1px solid color-mix(in srgb, var(--accent) 55%, transparent)}
         section{border-top:1px solid var(--border)}
         """),
    dict(name="neo", head="Archivo Black", body="Space Grotesk", mode="light",
         bg="#fdfdf6", surface="#ffffff", fg="#111111", muted="#4c4c46", border="#111111",
         radius="0px", btn="0px", shadow="6px 6px 0 #111111",
         hero="split", feats="tiles", extra="""
         .card,.btn,.mock,.plan,.stat-band{border:2.5px solid var(--border)!important;box-shadow:var(--shadow)!important}
         .btn-primary{background:var(--accent);color:#fff}
         .kicker{text-transform:uppercase;letter-spacing:.12em}
         .badge{border:2.5px solid var(--border);box-shadow:4px 4px 0 #111}
         h1{text-transform:uppercase;letter-spacing:-.01em}
         """),
    dict(name="glass", head="Outfit", body="Inter", mode="dark",
         bg="#0d1226", surface="rgba(255,255,255,.07)", fg="#f2f4ff", muted="#9aa3c7", border="rgba(255,255,255,.14)",
         radius="22px", btn="999px", shadow="0 24px 60px rgba(3,6,20,.55)",
         hero="center", feats="tiles", extra="""
         body{background:
           radial-gradient(640px 420px at 80% -6%, color-mix(in srgb, var(--accent) 30%, transparent), transparent 65%),
           radial-gradient(560px 400px at 12% 12%, color-mix(in srgb, var(--accent2) 22%, transparent), transparent 65%),
           var(--bg);}
         .card,.mock,.plan{backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid var(--border);background:var(--surface)}
         .hero h1{background:linear-gradient(92deg,var(--fg) 30%,var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent}
         """),
    dict(name="sunset", head="Bricolage Grotesque", body="Inter", mode="light",
         bg="#fff9f2", surface="#ffffff", fg="#231a14", muted="#7a6a5c", border="#f0e2d2",
         radius="24px", btn="999px", shadow="0 2px 4px rgba(180,110,60,.06), 0 18px 44px rgba(180,110,60,.12)",
         hero="center", feats="cards", extra="""
         body{background:linear-gradient(180deg,#fff3e6 0%, var(--bg) 34%)}
         .btn-primary{background:linear-gradient(120deg,var(--accent),var(--accent2))}
         .stat-band{background:linear-gradient(120deg,color-mix(in srgb,var(--accent) 12%,#fff),color-mix(in srgb,var(--accent2) 12%,#fff))}
         """),
    dict(name="forest", head="Lora", body="Inter", mode="light",
         bg="#f1f6ee", surface="#ffffff", fg="#17251a", muted="#5c6f5e", border="#dbe6d8",
         radius="18px", btn="10px", shadow="0 2px 3px rgba(30,60,35,.05), 0 14px 34px rgba(30,60,35,.08)",
         hero="center", feats="tiles", extra="""
         body{background:radial-gradient(700px 420px at 90% -8%, color-mix(in srgb, var(--accent2) 18%, transparent), transparent 66%), var(--bg)}
         .feat-icon{border-radius:58% 42% 55% 45%/48% 55% 45% 52%!important}
         .badge{background:color-mix(in srgb, var(--accent) 10%, #fff)}
         """),
]

# ------------------------------------------------------------- helpers ------

def esc(s): return html.escape(str(s), quote=True)

def rgba(hexcolor, a):
    hexcolor = hexcolor.lstrip("#")
    r, g, b = int(hexcolor[0:2], 16), int(hexcolor[2:4], 16), int(hexcolor[4:6], 16)
    return f"rgba({r},{g},{b},{a})"

def rot(seq, off, n):
    out = []
    for i in range(n):
        out.append(seq[(off + i) % len(seq)])
    return out

def bars(seed, count=8):
    h = hashlib.sha256(seed.encode()).digest()
    return [18 + h[i % len(h)] % 70 for i in range(count)]

def favicon(icon):
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>"
           f"<rect width='100' height='100' rx='22' fill='#111'/>"
           f"<text x='50' y='68' font-size='56' text-anchor='middle'>{icon}</text></svg>")
    return "data:image/svg+xml," + html.escape(svg, quote=True).replace("%", "%25")

# ------------------------------------------------------------ components ----

def mock_ui(brand, sector, theme, seed):
    """A fake product screenshot built from divs."""
    acc, acc2 = sector["accent"], sector["accent2"]
    bs = bars(seed)
    rows = rot(sector["features"], bs[0] % 7, 3)
    chips = rot(sector["stats"], bs[1] % 5, 3)
    chip_html = "".join(
        f'<div class="mk-chip"><b>{esc(c[0])}</b><span>{esc(c[1])}</span></div>' for c in chips)
    bar_html = "".join(f'<i style="height:{h}%"></i>' for h in bs)
    row_html = "".join(
        f'<div class="mk-row"><span class="mk-dot" style="background:{acc2}"></span>'
        f'<span class="mk-name">{esc(r[0])}</span><span class="mk-val">{"✓" if i != 1 else "●"}</span></div>'
        for i, r in enumerate(rows))
    return f"""
    <div class="mock" aria-hidden="true">
      <div class="mk-bar"><i></i><i></i><i></i><span>{esc(brand)} · live</span></div>
      <div class="mk-body">
        <div class="mk-chips">{chip_html}</div>
        <div class="mk-chart"><div class="mk-bars">{bar_html}</div></div>
        <div class="mk-rows">{row_html}</div>
      </div>
    </div>"""

def nav(brand, sector):
    links = [("Features", "#features"), ("How it works", "#how"),
             ("Pricing", "#pricing"), ("FAQ", "#faq")]
    lhtml = "".join(f'<a href="{h}">{t}</a>' for t, h in links)
    mark = sector["icon"]
    return f"""
  <nav class="nav">
    <div class="wrap nav-in">
      <a class="brand" href="#"><span class="brand-mark">{mark}</span>{esc(brand)}</a>
      <div class="nav-links" id="navLinks">{lhtml}</div>
      <div class="nav-actions">
        <a class="btn btn-ghost nav-hide" href="#pricing">See pricing</a>
        <a class="btn btn-primary" href="#cta">Get started</a>
        <button class="burger" id="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
      </div>
    </div>
  </nav>"""

def hero(brand, sector, theme, seed):
    badge = f'<span class="badge">{sector["icon"]} Built for {esc(sector["audience"])}</span>'
    ctas = ('<div class="cta-row"><a class="btn btn-primary btn-lg" href="#cta">Start free</a>'
            '<a class="btn btn-ghost btn-lg" href="#features">See how it works →</a></div>')
    names = rot(sector["testimonials"], 0, 3)
    avs = "".join(f'<span class="av" style="background:{rgba(sector["accent"], .16)};color:{sector["accent"]}">'
                  f'{esc("".join(w[0] for w in n.split()[:2]))}</span>' for _, n, _ in names)
    proof = (f'<div class="proof">{avs}'
             f'<p>Trusted by <b>{esc(sector["stats"][2][0])}</b> {esc(sector["audience"])}</p></div>')
    text = (f'{badge}<h1>{esc(brand[2])}</h1>'
            f'<p class="lede">{esc(brand[3])}</p>{ctas}{proof}')
    m = mock_ui(brand[0], sector, theme, seed)
    if theme["hero"] == "split":
        return f'<header class="hero split"><div class="wrap hero-grid"><div class="hero-copy">{text}</div><div class="hero-visual">{m}</div></div></header>'
    return f'<header class="hero"><div class="wrap hero-center">{text}<div class="hero-visual hero-visual-center">{m}</div></div></header>'

def section_features(brand, sector, theme, off):
    items = rot(sector["features"], off, 6)
    cards = "".join(
        f'<article class="card feat"><div class="feat-icon">{ic}</div>'
        f'<h3>{esc(t)}</h3><p>{esc(d)}</p></article>'
        for ic, t, d in items)
    return (f'<section id="features"><div class="wrap">'
            f'<p class="kicker">Features</p><h2>Everything you need, nothing you don\'t</h2>'
            f'<p class="sub">Why teams choose {esc(brand[0])} over duct-taping five tools together.</p>'
            f'<div class="grid feats">{cards}</div></div></section>')

def section_how(brand, sector, off):
    steps = [
        ("1", "Create your account", "Two minutes to sign up. No credit card, no sales call required."),
        ("2", f"Make {esc(brand[0])} yours", f"Configure it around how your {esc(sector['audience'].split()[-1] if sector['audience'] else 'team')} already works — imports, templates and defaults included."),
        ("3", "See results fast", f"Most {esc(sector['audience'])} get value inside the first week, and it compounds from there."),
    ]
    cards = "".join(
        f'<article class="card step"><span class="step-n">{n}</span><h3>{t}</h3><p>{d}</p></article>'
        for n, t, d in steps)
    return (f'<section id="how"><div class="wrap">'
            f'<p class="kicker">How it works</p><h2>Up and running in three steps</h2>'
            f'<div class="grid three">{cards}</div></div></section>')

def section_stats(sector, off):
    items = rot(sector["stats"], off, 4)
    cells = "".join(f'<div class="stat"><b>{esc(n)}</b><span>{esc(l)}</span></div>' for n, l in items)
    return f'<section class="stat-band"><div class="wrap grid four">{cells}</div></section>'

def section_pricing(brand, sector, off):
    scale = [1.0, 1.15, 1.3, 1.45][off % 4]
    plans = []
    for i, (nm, price, blurb) in enumerate(sector["plans"]):
        if price > 0:
            price = int(round(price * scale / 5.0) * 5) if price >= 20 else int(round(price * scale))
        plans.append((nm, price, blurb, i == 1))
    cards = ""
    for nm, price, blurb, feat in plans:
        ptxt = "Custom" if price == 0 else f"${price}"
        per = "" if price == 0 else "<span class='per'>/mo</span>"
        tag = "<span class='plan-tag'>Most popular</span>" if feat else ""
        cards += (f'<article class="card plan {"featured" if feat else ""}">{tag}'
                  f'<h3>{esc(nm)}</h3><div class="price">{ptxt}{per}</div>'
                  f'<p>{esc(blurb)}</p>'
                  f'<a class="btn {"btn-primary" if feat else "btn-ghost"}" href="#cta">Choose {esc(nm)}</a>'
                  f'</article>')
    return (f'<section id="pricing"><div class="wrap">'
            f'<p class="kicker">Pricing</p><h2>Simple pricing that scales with you</h2>'
            f'<p class="sub">Start free. Upgrade when {esc(brand[0])} has already paid for itself.</p>'
            f'<div class="grid three plans">{cards}</div></div></section>')

def section_testimonials(sector, off):
    items = rot(sector["testimonials"], off, 3)
    cards = ""
    for q, n, r in items:
        ini = "".join(w[0] for w in n.split()[:2])
        cards += (f'<figure class="card quote"><div class="qmark">“</div>'
                  f'<blockquote>{esc(q)}</blockquote>'
                  f'<figcaption><span class="av" style="background:{rgba(sector["accent"], .16)};color:{sector["accent"]}">{esc(ini)}</span>'
                  f'<span><b>{esc(n)}</b><br><span class="role">{esc(r)}</span></span></figcaption></figure>')
    return (f'<section id="testimonials"><div class="wrap">'
            f'<p class="kicker">Testimonials</p><h2>People who switched, in their words</h2>'
            f'<div class="grid three">{cards}</div></div></section>')

def section_faq(sector, off):
    items = rot(sector["faqs"], off, 4)
    rows = "".join(
        f'<details class="card faq"><summary>{esc(q)}<span class="chev">+</span></summary>'
        f'<p>{esc(a)}</p></details>' for q, a in items)
    return (f'<section id="faq"><div class="wrap faq-wrap">'
            f'<p class="kicker">FAQ</p><h2>Questions, answered</h2>'
            f'<div class="faqs">{rows}</div></div></section>')

def cta_band(brand):
    return (f'<section id="cta"><div class="wrap"><div class="cta-band">'
            f'<h2>Ready to see what {esc(brand[0])} can do?</h2>'
            f'<p>Free to try. Set up in minutes. Cancel anytime.</p>'
            f'<a class="btn btn-primary btn-lg" href="#">Get started free</a>'
            f'</div></div></section>')

def footer(brand, sector):
    cols = [
        ("Product", ["Features", "Pricing", "Integrations", "Changelog"]),
        ("Company", ["About", "Blog", "Careers", "Contact"]),
        ("Resources", ["Docs", "Help center", "API status", "Community"]),
        ("Legal", ["Privacy", "Terms", "Security", "DPA"]),
    ]
    colhtml = "".join(
        f'<div class="f-col"><h4>{t}</h4>' + "".join(f'<a href="#">{esc(x)}</a>' for x in items) + "</div>"
        for t, items in cols)
    return (f'<footer><div class="wrap">'
            f'<div class="f-top"><a class="brand" href="#"><span class="brand-mark">{sector["icon"]}</span>{esc(brand[0])}</a>'
            f'<p class="f-tag">{esc(brand[3])}</p></div>'
            f'<div class="f-grid">{colhtml}</div>'
            f'<div class="f-bottom"><span>© 2026 {esc(brand[0])}, Inc. All rights reserved.</span>'
            f'<span>{esc(sector["icon"])} {esc(sector["icon"] and sector_name(sector))}</span></div>'
            f'</div></footer>')

def sector_name(sector):
    for k, v in SECTORS.items():
        if v is sector:
            return k
    return ""

# ------------------------------------------------------------------ page ----

def build_page(idx, brand):
    name, skey, headline, sub = brand
    sector = SECTORS[skey]
    theme = THEMES[idx % len(THEMES)]
    off = idx % 4  # rotation offset within the sector's 4 brands
    seed = f"{name}-{skey}"

    css_vars = f"""
  :root {{
    --bg:{theme["bg"]}; --surface:{theme["surface"]}; --fg:{theme["fg"]};
    --muted:{theme["muted"]}; --border:{theme["border"]};
    --accent:{sector["accent"]}; --accent2:{sector["accent2"]};
    --radius:{theme["radius"]}; --btn-radius:{theme["btn"]};
    --shadow:{theme["shadow"]};
    --font-head:'{theme["head"]}', {SERIF if theme["head"] in ("Fraunces", "Playfair Display", "Lora") else SANS};
    --font-body:'{theme["body"]}', {SANS};
  }}"""

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(name)} — {esc(headline)}</title>
<meta name="description" content="{esc(sub)}">
<link rel="icon" href="{favicon(sector['icon'])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={theme['head'].replace(' ', '+')}:wght@400;500;600;700;800&family={theme['body'].replace(' ', '+')}:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{BASE_CSS}{css_vars}{theme["extra"]}</style>
</head>
<body>
{nav(name, sector)}
{hero(brand, sector, theme, seed)}
<div class="logos"><div class="wrap"><span class="logos-label">Trusted by {esc(sector['audience'])} at</span>{''.join(f'<span class="logo">{esc(l)}</span>' for l in sector['logos'])}</div></div>
{section_features(brand, sector, theme, off)}
{section_how(brand, sector, off)}
{section_stats(sector, off)}
{section_pricing(brand, sector, off)}
{section_testimonials(sector, off)}
{section_faq(sector, off)}
{cta_band(brand)}
{footer(brand, sector)}
<script>{PAGE_JS}</script>
</body>
</html>"""
    return page, theme

SANS = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif"
SERIF = "ui-serif, Georgia, serif"

# --------------------------------------------------------------- base css ----

BASE_CSS = """
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--font-body);line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:clip}
.grid>*{min-width:0}
img{max-width:100%}
a{color:inherit;text-decoration:none}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
h1,h2,h3{font-family:var(--font-head);line-height:1.12;margin:0 0 .5em}
h2{font-size:clamp(1.7rem,3.2vw,2.5rem);letter-spacing:-.015em}
h3{font-size:1.12rem}
p{margin:0 0 1em}
.sub{color:var(--muted);max-width:640px;margin:0 auto 40px;text-align:center}
.kicker{color:var(--accent);font-weight:700;font-size:.78rem;text-transform:uppercase;letter-spacing:.14em;margin:0 0 10px;text-align:center}
section{padding:84px 0}
section .kicker+h2{text-align:center}

/* nav */
.nav{position:sticky;top:0;z-index:50;background:color-mix(in srgb, var(--bg) 82%, transparent);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--border)}
.nav-in{display:flex;align-items:center;gap:22px;height:64px}
.brand{display:flex;align-items:center;gap:10px;font-family:var(--font-head);font-weight:700;font-size:1.12rem;white-space:nowrap}
.brand-mark{display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:9px;background:linear-gradient(135deg,var(--accent),var(--accent2));font-size:17px;box-shadow:0 4px 12px color-mix(in srgb, var(--accent) 35%, transparent)}
.nav-links{display:flex;gap:26px;margin:0 auto}
.nav-links a{color:var(--muted);font-size:.92rem;font-weight:500}
.nav-links a:hover{color:var(--fg)}
.nav-actions{display:flex;align-items:center;gap:10px;margin-left:auto}
.burger{display:none;background:none;border:0;cursor:pointer;padding:6px}
.burger span{display:block;width:20px;height:2px;background:var(--fg);margin:4px 0;border-radius:2px}

/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:10px 20px;border-radius:var(--btn-radius);font-weight:600;font-size:.94rem;border:1px solid transparent;cursor:pointer;transition:transform .15s ease, box-shadow .15s ease, background .15s ease;white-space:nowrap}
.btn-lg{padding:14px 28px;font-size:1.02rem}
.btn-primary{background:var(--accent);color:#fff}
.btn-primary:hover{transform:translateY(-1px);box-shadow:0 10px 26px color-mix(in srgb, var(--accent) 38%, transparent)}
.btn-ghost{border-color:var(--border);color:var(--fg);background:transparent}
.btn-ghost:hover{border-color:var(--muted)}

/* hero */
.hero{padding:88px 0 40px}
.hero h1{font-size:clamp(2.5rem,5.6vw,4rem);margin:18px 0 20px;letter-spacing:-.025em}
.hero .lede{font-size:clamp(1.05rem,1.6vw,1.24rem);color:var(--muted);max-width:600px;margin-bottom:30px}
.badge{display:inline-flex;align-items:center;gap:8px;padding:7px 14px;border-radius:999px;background:color-mix(in srgb, var(--accent) 10%, var(--surface));border:1px solid color-mix(in srgb, var(--accent) 22%, transparent);font-size:.85rem;font-weight:600;color:var(--accent)}
.cta-row{display:flex;gap:14px;flex-wrap:wrap}
.proof{display:flex;align-items:center;gap:12px;margin-top:30px}
.proof .av{width:34px;height:34px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:700;font-size:.78rem;border:2px solid var(--surface);margin-left:-8px}
.proof .av:first-child{margin-left:0}
.proof p{margin:0;font-size:.9rem;color:var(--muted)}
.proof b{color:var(--fg)}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center}
.hero-center{text-align:center;display:flex;flex-direction:column;align-items:center}
.hero-center .lede{margin-left:auto;margin-right:auto}
.hero-center .cta-row{justify-content:center}
.hero-center .proof{justify-content:center}
.hero-visual{min-width:0}
.hero-visual-center{width:min(760px,100%);margin-top:56px}

/* mock ui */
.mock{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);text-align:left}
.mk-bar{display:flex;align-items:center;gap:6px;padding:12px 16px;border-bottom:1px solid var(--border)}
.mk-bar i{width:10px;height:10px;border-radius:50%;background:var(--border)}
.mk-bar i:first-child{background:var(--accent)}
.mk-bar span{margin-left:auto;font-size:.72rem;color:var(--muted);font-weight:600;letter-spacing:.04em}
.mk-body{padding:18px}
.mk-chips{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:16px}
.mk-chip{border:1px solid var(--border);border-radius:calc(var(--radius) - 6px);padding:10px 12px;background:color-mix(in srgb, var(--surface) 60%, var(--bg))}
.mk-chip b{display:block;font-size:1.02rem;font-family:var(--font-head)}
.mk-chip span{font-size:.7rem;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.mk-chart{border:1px solid var(--border);border-radius:calc(var(--radius) - 6px);padding:14px;margin-bottom:14px;background:color-mix(in srgb, var(--surface) 60%, var(--bg))}
.mk-bars{display:flex;align-items:flex-end;gap:8px;height:96px}
.mk-bars i{flex:1;border-radius:5px 5px 2px 2px;background:linear-gradient(180deg,var(--accent2),var(--accent));opacity:.9}
.mk-bars i:nth-child(2n){opacity:.45}
.mk-row{display:flex;align-items:center;gap:10px;padding:9px 4px;border-bottom:1px dashed var(--border);font-size:.86rem}
.mk-row:last-child{border-bottom:0}
.mk-dot{width:8px;height:8px;border-radius:50%}
.mk-name{color:var(--muted)}
.mk-val{margin-left:auto;color:var(--accent);font-weight:700}

/* logos */
.logos{border-block:1px solid var(--border);padding:22px 0;background:color-mix(in srgb, var(--surface) 50%, var(--bg))}
.logos .wrap{display:flex;align-items:center;gap:28px;flex-wrap:wrap;justify-content:center}
.logos-label{font-size:.8rem;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);font-weight:600}
.logo{font-family:var(--font-head);font-weight:700;color:var(--muted);opacity:.75;font-size:1rem;white-space:nowrap}

/* grids & cards */
.grid{display:grid;gap:22px}
.three{grid-template-columns:repeat(3,1fr)}
.four{grid-template-columns:repeat(4,1fr)}
.feats{grid-template-columns:repeat(3,1fr);margin-top:44px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:26px;box-shadow:var(--shadow)}
.feat{transition:transform .18s ease, box-shadow .18s ease}
.feat:hover{transform:translateY(-4px)}
.feat-icon{display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:12px;background:color-mix(in srgb, var(--accent) 13%, transparent);font-size:22px;margin-bottom:16px}
.feat p{color:var(--muted);font-size:.94rem;margin:0}
.tiles .feat{background:linear-gradient(160deg, color-mix(in srgb, var(--accent) 7%, var(--surface)), var(--surface))}

/* steps */
.step{position:relative}
.step-n{display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:999px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;font-weight:800;font-family:var(--font-head);margin-bottom:14px}
.step p{color:var(--muted);font-size:.94rem;margin:0}

/* stats band */
.stat-band{background:linear-gradient(120deg, color-mix(in srgb, var(--accent) 12%, var(--surface)), color-mix(in srgb, var(--accent2) 12%, var(--surface)));border-block:1px solid var(--border);padding:56px 0}
.stat{text-align:center}
.stat b{display:block;font-family:var(--font-head);font-size:clamp(1.9rem,3.4vw,2.7rem);letter-spacing:-.02em;background:linear-gradient(120deg,var(--accent),var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent}
.stat span{color:var(--muted);font-size:.9rem;font-weight:600}

/* pricing */
.plans{margin-top:44px;align-items:stretch}
.plan{display:flex;flex-direction:column;position:relative}
.plan.featured{border:2px solid var(--accent);transform:scale(1.03);z-index:1}
.plan-tag{position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:var(--accent);color:#fff;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:5px 14px;border-radius:999px;white-space:nowrap}
.price{font-family:var(--font-head);font-size:2.6rem;font-weight:800;letter-spacing:-.02em;margin:6px 0 10px}
.price .per{font-size:1rem;color:var(--muted);font-weight:500}
.plan p{color:var(--muted);font-size:.94rem;flex:1}
.plan .btn{margin-top:18px}

/* quotes */
.quote{margin:0;display:flex;flex-direction:column;gap:10px}
.qmark{font-family:var(--font-head);font-size:2.4rem;line-height:1;color:var(--accent);font-weight:800}
.quote blockquote{margin:0;font-size:1.02rem}
.quote figcaption{display:flex;align-items:center;gap:12px;margin-top:auto;padding-top:14px}
.quote .av{width:40px;height:40px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:700;font-size:.82rem;flex:none}
.quote .role{color:var(--muted);font-size:.85rem}

/* faq */
.faq-wrap{max-width:780px}
.faqs{display:flex;flex-direction:column;gap:12px;margin-top:36px}
.faq{padding:0;overflow:hidden}
.faq summary{list-style:none;cursor:pointer;padding:18px 22px;font-weight:600;display:flex;justify-content:space-between;align-items:center;gap:16px}
.faq summary::-webkit-details-marker{display:none}
.faq .chev{color:var(--accent);font-size:1.3rem;font-weight:700;transition:transform .2s ease}
.faq[open] .chev{transform:rotate(45deg)}
.faq p{padding:0 22px 20px;color:var(--muted);margin:0}

/* cta */
#cta{padding-top:20px}
.cta-band{background:linear-gradient(120deg,var(--accent),var(--accent2));border-radius:calc(var(--radius) + 10px);padding:64px 32px;text-align:center;color:#fff;box-shadow:0 30px 70px color-mix(in srgb, var(--accent) 35%, transparent)}
.cta-band h2{color:#fff}
.cta-band p{opacity:.92;margin-bottom:26px}
.cta-band .btn-primary{background:#fff;color:#111}

/* footer */
footer{border-top:1px solid var(--border);padding:56px 0 32px;background:color-mix(in srgb, var(--surface) 55%, var(--bg))}
.f-top{display:flex;align-items:center;gap:16px;margin-bottom:36px;flex-wrap:wrap}
.f-tag{color:var(--muted);font-size:.92rem;margin:0}
.f-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-bottom:40px}
.f-col h4{font-size:.8rem;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin:0 0 14px}
.f-col a{display:block;color:var(--muted);font-size:.92rem;padding:5px 0}
.f-col a:hover{color:var(--fg)}
.f-bottom{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;border-top:1px solid var(--border);padding-top:22px;color:var(--muted);font-size:.85rem}

/* reveal */
.reveal{opacity:0;transform:translateY(16px)}
.reveal.in{opacity:1;transform:none;transition:opacity .6s ease, transform .6s ease}
@media (prefers-reduced-motion: reduce){.reveal{opacity:1;transform:none;transition:none}html{scroll-behavior:auto}}

/* responsive */
@media (max-width: 960px){
  .hero-grid{grid-template-columns:1fr;gap:40px}
  .three,.four,.feats{grid-template-columns:repeat(2,1fr)}
  .f-grid{grid-template-columns:repeat(2,1fr)}
}
@media (max-width: 720px){
  .nav-links{display:none;position:absolute;top:64px;left:0;right:0;background:var(--bg);border-bottom:1px solid var(--border);flex-direction:column;gap:0;padding:8px 0}
  .nav-links a{padding:14px 24px}
  .nav-links.open{display:flex}
  .burger{display:block}
  .nav-hide{display:none}
  .three,.four,.feats{grid-template-columns:1fr}
  .plan.featured{transform:none}
  .mk-chips{grid-template-columns:repeat(3,1fr);gap:6px}
  .mk-chip{padding:8px}
  .mk-chip b{font-size:.9rem}
  .mk-chip span{font-size:.6rem}
  .hero{padding-top:56px}
  section{padding:60px 0}
}
"""

PAGE_JS = """
(function(){
  var b=document.getElementById('burger'),l=document.getElementById('navLinks');
  if(b){b.addEventListener('click',function(){var o=l.classList.toggle('open');b.setAttribute('aria-expanded',o)});}
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}})},{threshold:.08});
    document.querySelectorAll('section, .hero, .logos').forEach(function(el,i){el.classList.add('reveal');el.style.transitionDelay=(Math.min(i%4,3)*60)+'ms';io.observe(el);});
  }
})();
"""

# ------------------------------------------------------------------ main ----

def write_pages():
    os.chdir(HERE)
    themes_used = {}
    for i, brand in enumerate(BRANDS):
        page, theme = build_page(i, brand)
        fn = slugify(brand[0]) + ".html"
        with open(fn, "w") as f:
            f.write(page)
        themes_used[brand[0]] = theme["name"]
    build_index()
    write_readme()
    print(f"Wrote {len(BRANDS)} pages + index.html + README.md")
    print(f"Themes rotation sample: {list(themes_used.items())[:10]}")

INDEX_CSS = """
*,*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:#0a0d1a;color:#eef1fa;font-family:'Inter',system-ui,sans-serif;line-height:1.6}
a{color:inherit;text-decoration:none}
button{font-family:inherit}
.wrap{max-width:1280px;margin:0 auto;padding:0 24px}
header.hero{padding:72px 0 36px;text-align:center;background:radial-gradient(700px 400px at 70% -10%, rgba(124,92,255,.25), transparent 65%),radial-gradient(600px 380px at 15% 0%, rgba(34,193,220,.18), transparent 65%)}
h1{font-family:'Sora',sans-serif;font-size:clamp(2.2rem,5vw,3.4rem);margin:0 0 14px;letter-spacing:-.02em}
.hero p{color:#98a0b8;max-width:600px;margin:0 auto}
.pill-row{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:24px}
.pill{border:1px solid #26304f;border-radius:999px;padding:7px 14px;font-size:.82rem;color:#b9c0d8;background:rgba(255,255,255,.03)}

/* toolbar */
.toolbar{position:sticky;top:0;z-index:60;background:rgba(10,13,26,.88);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid #1d2440;padding:12px 0}
.tb-in{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
#q{flex:1 1 230px;min-width:170px;padding:10px 16px;border-radius:10px;border:1px solid #26304f;background:#0f1428;color:#eef1fa;font-size:.9rem;outline:none}
#q:focus{border-color:#7c5cff}
select{background:#0f1428;border:1px solid #26304f;color:#eef1fa;border-radius:10px;padding:10px 12px;font-size:.85rem;outline:none;cursor:pointer;max-width:180px}
select:focus{border-color:#7c5cff}
.seg{display:flex;border:1px solid #26304f;border-radius:10px;overflow:hidden;flex:none}
.seg button{background:none;border:0;color:#98a0b8;padding:10px 14px;cursor:pointer;font-size:.85rem;font-weight:600}
.seg button.on{background:#1d2440;color:#fff}
.tot{text-align:center;color:#6f7896;font-size:.85rem;margin:16px 0 0}

/* sector pills */
.secnav{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;padding:20px 0 0}
.secnav a{font-size:.8rem;color:#98a0b8;border:1px solid #1d2440;padding:6px 12px;border-radius:999px;cursor:pointer;transition:.15s}
.secnav a:hover{color:#fff;border-color:#3a4573}
.secnav a.on{color:#fff;background:#2a2550;border-color:#7c5cff}

/* sections & groups */
.grp{padding:34px 0 4px}
.grp h2{font-family:'Sora',sans-serif;font-size:1.3rem;display:flex;align-items:center;gap:10px;margin:0 0 18px}
.s-icon{font-size:1.15rem}
.count{font-size:.72rem;background:#1d2440;color:#98a0b8;border-radius:999px;padding:3px 10px;font-weight:600}

/* grid view */
.pg-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(262px,1fr));gap:16px;padding:24px 0 30px}
.pg{position:relative;display:flex;flex-direction:column;gap:8px;background:#101529;border:1px solid #1d2440;border-radius:16px;padding:18px;cursor:pointer;transition:transform .15s ease,border-color .15s ease,box-shadow .15s ease;min-width:0}
.pg:hover{transform:translateY(-3px);border-color:#4c5aa0;box-shadow:0 16px 40px rgba(0,0,0,.45)}
.pg-top{display:flex;align-items:center;justify-content:space-between;gap:8px}
.pg-icon{width:40px;height:40px;border-radius:11px;display:inline-flex;align-items:center;justify-content:center;font-size:20px;flex:none}
.pg-mode{display:inline-flex;align-items:center;gap:6px;font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;color:#6f7896;font-weight:600}
.pg-mode i{width:8px;height:8px;border-radius:50%;display:inline-block}
.pg h3{font-family:'Sora',sans-serif;font-size:1.05rem;margin:2px 0 0}
.pg p{color:#98a0b8;font-size:.86rem;margin:0;flex:1}
.chip{display:inline-flex;align-items:center;gap:6px;width:fit-content;font-size:.72rem;color:#b9c0d8;border:1px solid #1d2440;border-radius:999px;padding:3px 10px;background:rgba(255,255,255,.02)}
.chip i{width:7px;height:7px;border-radius:50%;display:inline-block}
.pg-actions{display:flex;gap:8px;margin-top:12px;opacity:0;transform:translateY(4px);transition:.18s}
.pg:hover .pg-actions,.pg:focus-within .pg-actions{opacity:1;transform:none}
@media (hover:none){.pg .pg-actions{opacity:1;transform:none}}
.act{font-size:.78rem;font-weight:600;padding:7px 12px;border-radius:8px;cursor:pointer;border:1px solid #26304f;background:#0f1428;color:#c7cde6;display:inline-flex;align-items:center;gap:6px}
.act:hover{border-color:#4c5aa0;color:#fff}
.act-pv{background:#2a2550;border-color:#3a4573;color:#fff}

/* list view */
.pg-list{display:flex;flex-direction:column;gap:10px;padding:24px 0 30px}
.pg-row{display:grid;grid-template-columns:44px minmax(0,1fr) auto auto;gap:4px 18px;align-items:center;background:#101529;border:1px solid #1d2440;border-radius:14px;padding:14px 18px;cursor:pointer;transition:border-color .15s ease,transform .15s ease;min-width:0}
.pg-row:hover{border-color:#4c5aa0;transform:translateY(-1px)}
.pg-row .pg-actions{margin-top:0;opacity:1;transform:none}
.pr-body{min-width:0}
.pr-body h3{font-family:'Sora',sans-serif;font-size:1rem;margin:0}
.pr-body p{margin:0;color:#98a0b8;font-size:.85rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pr-meta{display:flex;gap:8px;flex-wrap:wrap;justify-content:flex-end}
@media(max-width:780px){
  .pg-row{grid-template-columns:40px minmax(0,1fr)}
  .pr-meta{grid-column:2;justify-content:flex-start}
  .pg-row .pg-actions{grid-column:2}
}

/* empty state */
#empty{display:none;text-align:center;padding:70px 0;color:#98a0b8}
#empty button{margin-top:14px;background:#2a2550;border:1px solid #3a4573;color:#fff;border-radius:10px;padding:10px 18px;cursor:pointer;font-weight:600}

/* hover live preview */
#hover{position:fixed;z-index:80;width:340px;pointer-events:none;opacity:0;transform:translateY(8px) scale(.98);transition:opacity .18s ease,transform .18s ease}
#hover.on{opacity:1;transform:none}
.hv-head{display:flex;justify-content:space-between;gap:10px;font-size:.72rem;color:#98a0b8;padding:7px 12px;background:#101529;border:1px solid #26304f;border-bottom:0;border-radius:12px 12px 0 0;font-weight:600}
.hv-frame{position:relative;height:214px;border-radius:0 0 12px 12px;overflow:hidden;border:1px solid #26304f;background:#fff;box-shadow:0 30px 70px rgba(0,0,0,.55)}
#hoverFrame{width:1280px;height:820px;transform:scale(.2656);transform-origin:0 0;border:0;display:block}
.spin{position:absolute;inset:0;display:none;place-items:center;color:#98a0b8;font-size:.8rem;background:#0f1428}
@media(max-width:999px){#hover{display:none}}

/* preview modal */
#pv{position:fixed;inset:0;z-index:100;display:none;flex-direction:column;background:rgba(5,7,16,.94)}
#pv.open{display:flex}
.pv-bar{display:flex;align-items:center;gap:12px;padding:10px 16px;border-bottom:1px solid #1d2440;background:#0a0d1a;flex-wrap:wrap}
.pv-bar h3{margin:0;font-family:'Sora',sans-serif;font-size:1.02rem}
#pvMeta{display:flex;gap:8px;flex-wrap:wrap}
.pv-spacer{flex:1}
.pv-x{background:none;border:1px solid #26304f;color:#98a0b8;border-radius:10px;padding:8px 13px;cursor:pointer;font-size:.9rem}
.pv-x:hover{color:#fff;border-color:#4c5aa0}
#pvStage{flex:1;position:relative;overflow:hidden;display:flex;align-items:stretch;justify-content:center;padding:14px}
#pvFrameWrap{position:relative;overflow:hidden;border-radius:12px;border:1px solid #26304f;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.6)}
#pvFrame{position:absolute;top:0;left:0;transform-origin:0 0;border:0;display:block}
.pv-nav{position:absolute;top:50%;transform:translateY(-50%);z-index:5;width:44px;height:44px;border-radius:50%;border:1px solid #26304f;background:rgba(16,21,41,.9);color:#eef1fa;font-size:1.3rem;cursor:pointer;display:grid;place-items:center}
.pv-nav:hover{border-color:#7c5cff;background:#1d2440}
.pv-nav.prev{left:14px}.pv-nav.next{right:14px}
.pv-hint{padding:8px 16px;text-align:center;color:#6f7896;font-size:.75rem;border-top:1px solid #1d2440;background:#0a0d1a}
@media(max-width:720px){.pv-nav{display:none}}
footer{border-top:1px solid #1d2440;margin-top:44px;padding:28px 0;color:#6f7896;font-size:.85rem;text-align:center}
@media(max-width:640px){.pg-grid{grid-template-columns:1fr 1fr}}
@media(max-width:480px){.pg-grid{grid-template-columns:1fr}}
"""

INDEX_JS = """
const PAGES = __PAGES__;
const SECTORS = __SECTORS__;
const $ = s => document.querySelector(s);
const grid = $('#grid');
const state = { q:'', sector:'', theme:'', mode:'', sort:'sector', view:'grid' };
let shuffleMap = null;
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

/* ---------- options ---------- */
SECTORS.forEach(s => $('#fsector').insertAdjacentHTML('beforeend', `<option value="${esc(s.k)}">${s.i} ${esc(s.k)}</option>`));
[...new Set(PAGES.map(p => p.t))].sort().forEach(t => $('#ftheme').insertAdjacentHTML('beforeend', `<option value="${t}">${t}</option>`));

/* ---------- filtering / sorting ---------- */
function matches(p){
  if (state.sector && p.k !== state.sector) return false;
  if (state.theme && p.t !== state.theme) return false;
  if (state.mode && p.m !== state.mode) return false;
  if (state.q){
    const hay = (p.n + ' ' + p.k + ' ' + p.h + ' ' + p.t).toLowerCase();
    if (!hay.includes(state.q.toLowerCase())) return false;
  }
  return true;
}
function sorted(list){
  const s = state.sort;
  if (s === 'az')    return [...list].sort((a,b) => a.n.localeCompare(b.n));
  if (s === 'za')    return [...list].sort((a,b) => b.n.localeCompare(a.n));
  if (s === 'theme') return [...list].sort((a,b) => a.t.localeCompare(b.t) || a.n.localeCompare(b.n));
  if (s === 'shuffle'){
    if (!shuffleMap){ shuffleMap = {}; PAGES.forEach(p => shuffleMap[p.s] = Math.random()); }
    return [...list].sort((a,b) => shuffleMap[a.s] - shuffleMap[b.s]);
  }
  return list; /* data order = grouped by sector */
}

/* ---------- rendering ---------- */
function modeDot(m){ return `<i style="background:${m === 'dark' ? '#8f7bff' : '#f4b942'}"></i>`; }
function acts(){
  return `<div class="pg-actions"><button class="act act-pv" type="button">Preview</button><a class="act act-open" href="#" target="_blank" rel="noopener">Open ↗</a></div>`;
}
function card(p){
  if (state.view === 'list'){
    return `<article class="pg-row" data-slug="${p.s}" data-name="${esc(p.n)}">
      <span class="pg-icon" style="background:linear-gradient(135deg,${p.a},${p.a2})">${p.i}</span>
      <div class="pr-body"><h3>${esc(p.n)}</h3><p>${esc(p.h)}</p></div>
      <div class="pr-meta"><span class="chip">${esc(p.k)}</span><span class="chip">${modeDot(p.m)}${p.t}</span></div>
      ${acts().replace('href="#"', `href="${p.s}.html"`)}
    </article>`;
  }
  return `<article class="pg" data-slug="${p.s}" data-name="${esc(p.n)}">
    <div class="pg-top">
      <span class="pg-icon" style="background:linear-gradient(135deg,${p.a},${p.a2})">${p.i}</span>
      <span class="pg-mode">${modeDot(p.m)}${p.t}</span>
    </div>
    <h3>${esc(p.n)}</h3>
    <p>${esc(p.h)}</p>
    <span class="chip">${esc(p.k)}</span>
    ${acts().replace('href="#"', `href="${p.s}.html"`)}
  </article>`;
}
function render(){
  const list = sorted(PAGES.filter(matches));
  $('#tot').textContent = `Showing ${list.length} of ${PAGES.length} templates`;
  $('#empty').style.display = list.length ? 'none' : 'block';
  let html = '';
  if (state.sort === 'sector'){
    for (const sec of SECTORS){
      const items = list.filter(p => p.k === sec.k);
      if (!items.length) continue;
      html += `<section class="grp"><h2><span class="s-icon">${sec.i}</span>${esc(sec.k)}<span class="count">${items.length}</span></h2>` +
              `<div class="${state.view === 'list' ? 'pg-list' : 'pg-grid'}">` + items.map(card).join('') + `</div></section>`;
    }
  } else {
    html = `<div class="${state.view === 'list' ? 'pg-list' : 'pg-grid'}" style="padding-top:24px">` + list.map(card).join('') + `</div>`;
  }
  grid.innerHTML = html;
}
function syncPills(){
  document.querySelectorAll('#secnav a').forEach(a => a.classList.toggle('on', a.dataset.sector === state.sector));
}

/* ---------- hover live preview ---------- */
const hov = $('#hover'), hovFrame = $('#hoverFrame'), hovSpin = $('#hoverSpin');
let hovSlug = null, hovTimer = null;
function showHover(el){
  const slug = el.dataset.slug;
  clearTimeout(hovTimer);
  hovTimer = setTimeout(() => {
    if (hovSlug !== slug){
      hovSpin.style.display = 'grid';
      hovFrame.src = slug + '.html';
      $('#hoverName').textContent = el.dataset.name;
      hovSlug = slug;
    }
    const r = el.getBoundingClientRect(), W = 340, H = 250;
    let x = r.right + 16;
    if (x + W > innerWidth - 8) x = r.left - W - 16;
    x = Math.max(8, Math.min(x, innerWidth - W - 8));
    const y = Math.max(64, Math.min(r.top - 8, innerHeight - H - 12));
    hov.style.left = x + 'px'; hov.style.top = y + 'px';
    hov.classList.add('on');
  }, 200);
}
function hideHover(){
  clearTimeout(hovTimer);
  hovTimer = setTimeout(() => hov.classList.remove('on'), 120);
}
hovFrame.addEventListener('load', () => { hovSpin.style.display = 'none'; });

/* ---------- preview modal ---------- */
const pv = $('#pv'), pvFrame = $('#pvFrame'), pvStage = $('#pvStage'), pvWrap = $('#pvFrameWrap');
let pvList = [], pvIdx = -1, pvW = 1280;
function currentList(){ return sorted(PAGES.filter(matches)); }
function openPv(slug){
  pvList = currentList();
  pvIdx = Math.max(0, pvList.findIndex(p => p.s === slug));
  pv.classList.add('open');
  document.body.style.overflow = 'hidden';
  loadPv();
}
function loadPv(){
  const p = pvList[pvIdx]; if (!p) return;
  $('#pvName').textContent = p.n;
  $('#pvMeta').innerHTML = `<span class="chip">${esc(p.k)}</span><span class="chip">${modeDot(p.m)}${p.t}</span>`;
  $('#pvOpen').href = p.s + '.html';
  $('#pvSpin').style.display = 'grid';
  pvFrame.src = p.s + '.html';
  if (location.hash !== '#preview=' + p.s) location.hash = 'preview=' + p.s;
  fitPv();
}
function stepPv(d){
  if (!pvList.length) return;
  pvIdx = (pvIdx + d + pvList.length) % pvList.length;
  loadPv();
}
function closePv(){
  if (!pv.classList.contains('open')) return;
  pv.classList.remove('open');
  document.body.style.overflow = '';
  pvFrame.src = 'about:blank';
  if (location.hash.indexOf('preview=') === 0) location.hash = '';
}
function setDevice(w){
  pvW = w;
  document.querySelectorAll('.pv-dev').forEach(b => b.classList.toggle('on', +b.dataset.w === w));
  fitPv();
}
function fitPv(){
  if (!pv.classList.contains('open')) return;
  const avail = pvStage.clientWidth - 28, h = pvStage.clientHeight - 28;
  const s = Math.min(1, avail / pvW);
  pvWrap.style.width = Math.round(pvW * s) + 'px';
  pvWrap.style.height = h + 'px';
  pvFrame.style.width = pvW + 'px';
  pvFrame.style.height = Math.round(h / s) + 'px';
  pvFrame.style.transform = 'scale(' + s + ')';
}
pvFrame.addEventListener('load', () => { $('#pvSpin').style.display = 'none'; });
addEventListener('resize', fitPv);

/* ---------- events ---------- */
grid.addEventListener('click', e => {
  const el = e.target.closest('[data-slug]'); if (!el) return;
  if (e.target.closest('.act-open')) return; /* native link */
  e.preventDefault();
  if (e.target.closest('.pg-mode,.chip')){
    const p = PAGES.find(x => x.s === el.dataset.slug);
    if (p && e.target.closest('.pg-mode')){ state.theme = p.t; $('#ftheme').value = p.t; render(); return; }
  }
  openPv(el.dataset.slug);
});
grid.addEventListener('mouseover', e => {
  const el = e.target.closest('[data-slug]');
  if (!el || matchMedia('(hover: none)').matches || innerWidth < 1000) return;
  showHover(el);
});
grid.addEventListener('mouseout', e => { if (e.target.closest('[data-slug]')) hideHover(); });
$('#q').addEventListener('input', e => { state.q = e.target.value.trim(); render(); });
$('#fsector').addEventListener('change', e => { state.sector = e.target.value; syncPills(); render(); });
$('#ftheme').addEventListener('change', e => { state.theme = e.target.value; render(); });
$('#fmode').addEventListener('change', e => { state.mode = e.target.value; render(); });
$('#fsort').addEventListener('change', e => { state.sort = e.target.value; render(); });
document.querySelectorAll('.vw').forEach(b => b.addEventListener('click', () => setView(b.dataset.v)));
$('#clear').addEventListener('click', () => {
  state.q = state.sector = state.theme = state.mode = '';
  $('#q').value = ''; $('#fsector').value = ''; $('#ftheme').value = ''; $('#fmode').value = '';
  syncPills(); render();
});
$('#secnav').addEventListener('click', e => {
  const a = e.target.closest('a[data-sector]'); if (!a) return;
  e.preventDefault();
  state.sector = (state.sector === a.dataset.sector) ? '' : a.dataset.sector;
  $('#fsector').value = state.sector;
  syncPills(); render();
  scrollTo({ top: 0, behavior: 'smooth' });
});
document.querySelectorAll('.pv-dev').forEach(b => b.addEventListener('click', () => setDevice(+b.dataset.w)));
$('#pvClose').addEventListener('click', closePv);
$('#pvPrev').addEventListener('click', () => stepPv(-1));
$('#pvNext').addEventListener('click', () => stepPv(1));
pv.addEventListener('click', e => { if (e.target === pv || e.target === pvStage) closePv(); });
addEventListener('keydown', e => {
  if (e.key === 'Escape') closePv();
  if (!pv.classList.contains('open')) return;
  if (e.key === 'ArrowRight') stepPv(1);
  if (e.key === 'ArrowLeft') stepPv(-1);
});

/* ---------- view + hash routing ---------- */
function setView(v){
  state.view = (v === 'list') ? 'list' : 'grid';
  document.querySelectorAll('.vw').forEach(b => b.classList.toggle('on', b.dataset.v === state.view));
  render();
}
function applyHash(){
  const params = new URLSearchParams(location.hash.slice(1));
  if (params.get('view') && params.get('view') !== state.view) setView(params.get('view'));
  const pre = params.get('preview');
  if (pre){ if (!pv.classList.contains('open')) openPv(pre); }
  else closePv();
}
addEventListener('hashchange', applyHash);

render();
syncPills();
applyHash();
"""

INDEX_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>100 Landing Pages — browse, search & preview templates</title>
<meta name="description" content="A gallery of 100 handcrafted landing pages across 25 industries. Search, filter, sort and live-preview each template.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='80' font-size='80'%3E%F0%9F%9A%80%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>__INDEX_CSS__</style>
</head>
<body>
<header class="hero"><div class="wrap">
<h1>🚀 100 Landing Pages</h1>
<p>One handcrafted landing page for each of 100 fictional products across 25 industries. Search, filter, sort — hover any card for a live preview, or click to open it in a device-sized viewer.</p>
<div class="pill-row"><span class="pill">25 sectors</span><span class="pill">10 themes</span><span class="pill">🔍 search</span><span class="pill">🎛 filter & sort</span><span class="pill">⊞ grid / ☰ list</span><span class="pill">👀 live preview</span></div>
</div></header>

<div class="toolbar"><div class="wrap tb-in">
<input id="q" type="search" placeholder="🔍 Search name, sector, headline…" aria-label="Search templates">
<select id="fsector" aria-label="Filter by sector"><option value="">All sectors</option></select>
<select id="ftheme" aria-label="Filter by theme"><option value="">All themes</option></select>
<select id="fmode" aria-label="Filter by color mode"><option value="">Light & dark</option><option value="light">Light only</option><option value="dark">Dark only</option></select>
<select id="fsort" aria-label="Sort templates">
  <option value="sector">Sort: Sector</option>
  <option value="az">Sort: Name A→Z</option>
  <option value="za">Sort: Name Z→A</option>
  <option value="theme">Sort: Theme</option>
  <option value="shuffle">Sort: Shuffle</option>
</select>
<div class="seg" role="group" aria-label="View mode">
  <button class="vw on" data-v="grid" title="Grid view">⊞</button>
  <button class="vw" data-v="list" title="List view">☰</button>
</div>
</div></div>

<main class="wrap">
<p class="tot" id="tot">Showing 100 of 100 templates</p>
<nav class="secnav" id="secnav">__SECNAV__</nav>
<div id="grid"></div>
<div id="empty"><p>😕 No templates match your search.</p><button id="clear" type="button">Clear all filters</button></div>
</main>

<div id="hover" aria-hidden="true">
  <div class="hv-head"><span id="hoverName"></span><span>live preview · click to open</span></div>
  <div class="hv-frame"><iframe id="hoverFrame" title="Live preview" loading="lazy" tabindex="-1"></iframe><div class="spin" id="hoverSpin">loading…</div></div>
</div>

<div id="pv" role="dialog" aria-modal="true" aria-label="Template preview">
  <div class="pv-bar">
    <button class="pv-nav prev" id="pvPrev" title="Previous (←)">‹</button>
    <button class="pv-nav next" id="pvNext" title="Next (→)">›</button>
    <h3 id="pvName"></h3>
    <div id="pvMeta"></div>
    <div class="pv-spacer"></div>
    <div class="seg" role="group" aria-label="Preview device">
      <button class="pv-dev on" data-w="1280">🖥 Desktop</button>
      <button class="pv-dev" data-w="834">📱 Tablet</button>
      <button class="pv-dev" data-w="414">📱 Phone</button>
    </div>
    <a class="act" id="pvOpen" href="#" target="_blank" rel="noopener">Open full page ↗</a>
    <button class="pv-x" id="pvClose" title="Close (Esc)">✕</button>
  </div>
  <div id="pvStage">
    <div id="pvFrameWrap"><iframe id="pvFrame" title="Template preview"></iframe><div class="spin" id="pvSpin">loading…</div></div>
  </div>
  <div class="pv-hint">← → to browse templates · Esc to close · click the backdrop to dismiss</div>
</div>

<footer><div class="wrap">Generated with <code>generate.py</code> · open any page directly, no server needed</div></footer>
<noscript><p style="text-align:center;padding:20px">Enable JavaScript to browse the gallery — or open any brand page directly, e.g. <a href="ledgerly.html">ledgerly.html</a>.</p></noscript>
<script>__INDEX_JS__</script>
</body>
</html>"""


def build_index():
    import json

    themes = [THEMES[i % len(THEMES)] for i in range(len(BRANDS))]
    pages = [
        dict(n=b[0], s=slugify(b[0]), k=b[1], h=b[2],
             t=themes[i]["name"], m=themes[i]["mode"],
             a=SECTORS[b[1]]["accent"], a2=SECTORS[b[1]]["accent2"], i=SECTORS[b[1]]["icon"])
        for i, b in enumerate(BRANDS)
    ]
    sectors = [dict(k=k, i=v["icon"]) for k, v in SECTORS.items()]
    secnav = "".join(
        f'<a data-sector="{esc(k)}">{v["icon"]} {esc(k)}</a>' for k, v in SECTORS.items())
    doc = (INDEX_TMPL
           .replace("__INDEX_CSS__", INDEX_CSS)
           .replace("__INDEX_JS__", INDEX_JS)
           .replace("__PAGES__", json.dumps(pages, ensure_ascii=False))
           .replace("__SECTORS__", json.dumps(sectors, ensure_ascii=False))
           .replace("__SECNAV__", secnav))
    with open(os.path.join(HERE, "index.html"), "w") as f:
        f.write(doc)

def write_readme():
    md = """# 100 Landing Pages

100 standalone, self-contained landing pages for fictional products across **25 sectors**
(4 products each), rendered in **10 rotating visual themes**.

## Browse

Open `index.html` — a filterable gallery of all 100 pages:

- **Search** by name, sector or headline
- **Filter** by sector (dropdown or quick pills), theme, and light/dark mode
- **Sort** by sector (grouped), name A→Z / Z→A, theme, or shuffle
- **Grid / list view** toggle
- **Live previews** — hover a card for a scaled live thumbnail; click for a
  full preview modal with desktop/tablet/phone widths, `←`/`→` to browse,
  `Esc` to close, and deep links via `index.html#preview=paystream`
  (also `#view=list`)

Every page works over `file://` with no server and no external assets
(Google Fonts is the only optional network request; pages fall back to
system fonts offline).

## Structure

- `index.html` — filterable gallery of all 100 pages
- `<brand>.html` × 100 — one landing page per product (nav, hero with fake product UI,
  logo strip, features, how-it-works, stats band, pricing, testimonials, FAQ, CTA, footer)
- `data.py` — all copy: sector content banks + 100 brand entries
- `generate.py` — theme engine + page builder

## Regenerate

```bash
python3 generate.py
```

Edit `data.py` to change copy or add brands; edit `THEMES` in `generate.py` for styling.
"""
    with open(os.path.join(HERE, "README.md"), "w") as f:
        f.write(md)

if __name__ == "__main__":
    write_pages()
