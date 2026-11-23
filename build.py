#!/usr/bin/env python3
"""Static site generator for intellectai.app.

  python3 -I build.py          -> writes dist/
  python3 -I build.py --og     -> also renders the OG images with headless Chrome

Content lives in content/<lang>.py (UI, HOME, PROMPTS_PAGE, PRIVACY, PICKER, COACHES); shared data in content/common.py.
"""
import html, importlib.util, json, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
sys.path.insert(0, os.path.join(ROOT, "content"))
import common as C  # noqa: E402

PUBLISHED = "2026-11-23"
MODIFIED = "2026-11-23"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
WARN = []


def load(lang):
    spec = importlib.util.spec_from_file_location(lang, os.path.join(ROOT, "content", f"{lang}.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


L = {lang: load(lang) for lang in C.LANGS}
G = {lang: load(f"guides_{lang}") for lang in C.LANGS}
for _lang in C.LANGS:  # merge later batches: content/guides_<lang>_*.py (GUIDES, CATS, ZEHN)
    import glob as _glob
    for _f in sorted(_glob.glob(os.path.join(ROOT, "content", f"guides_{_lang}_*.py"))):
        _m = load(os.path.basename(_f)[:-3])
        G[_lang].GUIDES.update(getattr(_m, "GUIDES", {}))
        G[_lang].CATS.update(getattr(_m, "CATS", {}))
        G[_lang].ZEHN.update(getattr(_m, "ZEHN", {}))
        G[_lang].UI.update(getattr(_m, "UI", {}))
BOOKS = json.load(open(os.path.join(ROOT, "content", "books.json"), encoding="utf-8"))
e = lambda s: html.escape(s, quote=True)  # noqa: E731
SOCIAL = [("X", "https://x.com/thezehnapp"), ("Instagram", "https://www.instagram.com/thezehnapp/"), ("YouTube", "https://www.youtube.com/@thezehnapp")]


def md(s):
    """Escape, then **bold** and [text](url)."""
    s = e(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{m.group(2)}"{" rel=\"noopener\"" if m.group(2).startswith("http") and "intellectai.app" not in m.group(2) else ""}>{m.group(1)}</a>', s)


def plain(s):
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s).replace("**", "")


def gpath(slug, g):
    return g.get("path") or f"guides/{slug}/"


def all_guides(lang):
    gm = G[lang]
    return list(gm.GUIDES.items()) + list(gm.ZEHN.items())


def avail(path):
    """Languages a path exists in (guides can be single-language)."""
    gp = {lang: {gpath(k, g) for k, g in all_guides(lang)} for lang in C.LANGS}
    allg = set().union(*gp.values())
    if path in allg:
        return [x for x in C.LANGS if path in gp[x]]
    return list(C.LANGS)


def xdefault(path):
    a = avail(path)
    return f"{C.BASE}/" if len(a) == len(C.LANGS) else url("en" if "en" in a else a[0], path)


def url(lang, path=""):
    return f"{C.BASE}/{lang}/{path}" if lang else f"{C.BASE}/{path}"


def check_meta(where, title, desc):
    if len(title) > 60:
        WARN.append(f"title {len(title)}>60: {where}: {title}")
    if len(desc) > 155:
        WARN.append(f"desc {len(desc)}>155: {where}")


def words(s):
    return len(re.findall(r"\S+", s))


def check_faq(where, lang, faq):
    lo, hi = (40, 60) if lang == "en" else (30, 70)
    for q, a in faq:
        n = words(a)
        if not lo <= n <= hi:
            WARN.append(f"faq {n} words ({lang}) {where}: {q}")


FONTS = {
    "en": "family=Inter:wght@400;600;700&family=Manrope:wght@700;800",
    "ru": "family=Inter:wght@400;600;700&family=Manrope:wght@700;800",
    "ar": "family=Cairo:wght@400;600;700;800",
}
LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#0B1D2A"/>'
        '<circle cx="16" cy="9.5" r="2.6" fill="#3DDC97"/><path d="M16 14.5v9" stroke="#fff" stroke-width="3.2" stroke-linecap="round"/>'
        '<path d="M8 21.5c2.2 2.6 5 3.9 8 3.9s5.8-1.3 8-3.9" stroke="#3DDC97" stroke-width="2" fill="none" stroke-linecap="round"/></svg>')
APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.4 12.7c0-2.4 2-3.6 2.1-3.7-1.2-1.7-3-1.9-3.6-2-1.5-.2-3 .9-3.8.9-.8 0-2-.9-3.3-.8-1.7 0-3.3 1-4.2 2.5-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8s2 .8 3.3.8c1.4 0 2.3-1.3 3.1-2.5 1-1.4 1.4-2.8 1.4-2.9-.1 0-2.8-1-2.8-4.3zM14 5.5c.7-.9 1.2-2 1-3.2-1 0-2.3.7-3 1.6-.7.8-1.3 2-1.1 3.1 1.2.1 2.3-.6 3.1-1.5z"/></svg>'
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 2.6v18.8c0 .5.5.8.9.6l10.3-10-10.3-10c-.4-.2-.9.1-.9.6zM16.6 9.3 6.8 3.6l8.2 7.9zM16.6 14.7 15 12.5l-8.2 7.9zM20.4 11.1l-2.6-1.5-1.9 2.4 1.9 2.4 2.6-1.5c.8-.5.8-1.4 0-1.8z"/></svg>'

ORG_ID = f"{C.BASE}/#org"
SITE_ID = f"{C.BASE}/#website"


def org_ld():
    return {"@type": "Organization", "@id": ORG_ID, "name": "Intellect AI", "url": C.BASE + "/",
            "logo": {"@type": "ImageObject", "url": C.BASE + "/icon-512.png", "width": 512, "height": 512},
            "email": C.EMAIL,
            "parentOrganization": {"@type": "Organization", "name": "Safari Group",
                                   "foundingDate": "2005", "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"}}}


def site_ld():
    return {"@type": "WebSite", "@id": SITE_ID, "name": "Intellect AI", "url": C.BASE + "/",
            "inLanguage": C.LANGS, "publisher": {"@id": ORG_ID}}


def zehn_ld(lang):
    return {"@type": "MobileApplication", "name": "Zehn", "operatingSystem": "iOS, Android",
            "applicationCategory": "EducationApplication", "url": f"{C.ZEHN}/{lang}/",
            "sameAs": [C.APP_STORE, C.GOOGLE_PLAY] + [u for _, u in SOCIAL],
            "publisher": {"@type": "Organization", "name": "Safari Group"}}


def faq_ld(faq):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in faq]}


def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def ld_script(nodes):
    data = {"@context": "https://schema.org", "@graph": nodes}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"


def head(lang, title, desc, path, ld, alts=True, og_lang=None, noindex=False):
    check_meta(f"{lang}/{path}", title, desc)
    canon = url(lang, path)
    ui = L[lang or "en"].UI
    d = "rtl" if lang == "ar" else "ltr"
    alt = ""
    if alts:
        alt = "".join(f'<link rel="alternate" hreflang="{x}" href="{url(x, path)}">' for x in avail(path))
        alt += f'<link rel="alternate" hreflang="x-default" href="{xdefault(path)}">'
    og = f"{C.BASE}/og/og-{og_lang or lang or 'en'}.jpg"
    fl = FONTS[lang or "en"]
    return f"""<!doctype html>
<html lang="{lang or 'en'}" dir="{d}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'}
<link rel="canonical" href="{canon}">
{alt}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Intellect AI">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="{ui['locale']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B1D2A">
<meta name="msvalidate.01" content="D92BFF32C7F1100C522E700E7E8C8C42">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32x32.png" type="image/png" sizes="32x32">
<link rel="manifest" href="/site.webmanifest">
{f'<link rel="alternate" type="application/rss+xml" title="Intellect AI" href="/{lang}/feed.xml">' if lang else ""}
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fl}&display=swap">
<link rel="stylesheet" href="/style.css?v={STYLE_V}">
{ld_script(ld)}
</head>
<body>
<a class="skip" href="#main">{e(ui['skip'])}</a>"""


def header(lang, path):
    ui = L[lang].UI
    av = avail(path)
    langs = "".join(f'<a href="/{x}/{path if x in av else ""}" hreflang="{x}" lang="{x}"{" aria-current=\"true\"" if x == lang else ""}>{x.upper()}</a>' for x in C.LANGS)
    return f"""<header class="top"><div class="wrap">
<a class="brand" href="/{lang}/" aria-label="Intellect AI">{LOGO}<span>Intellect AI</span></a>
<nav class="nav" aria-label="{e(ui['menu_label'])}">
<a class="hide-s" href="/{lang}/#coaches">{e(ui['nav_coaches'])}</a>
<a href="/{lang}/guides/">{e(G[lang].UI['nav_guides'])}</a>
<a href="/{lang}/prompts/">{e(ui['nav_prompts'])}</a>
<span class="langs" aria-label="{e(ui['lang_label'])}">{langs}</span>
<a class="get hide-s" href="{C.ZEHN}/{lang}/">{e(ui['nav_get'])}</a>
</nav></div></header>
<main id="main">"""


def footer(lang):
    ui = L[lang].UI
    co = L[lang].COACHES
    gu = G[lang].UI
    links = "".join(f'<li><a href="/{lang}/{s}/">{e(co[s]["name"])}</a></li>' for s, *_ in C.COACHES)
    cats = "".join(f'<li><a href="/{lang}/guides/#{k}">{e(v[0])}</a></li>' for k, v in G[lang].CATS.items())
    soc = "".join(f'<li><a href="{u}" rel="noopener">{n}</a></li>' for n, u in SOCIAL)
    return f"""</main>
<footer><div class="wrap">
<div><a class="brand" href="/{lang}/" aria-label="Intellect AI">{LOGO}Intellect AI</a><p style="margin-top:10px">{e(ui['footer_about'])}</p>
<p><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p><b style="margin-top:14px">{e(gu['social_h'])}</b><ul class="soc">{soc}</ul></div>
<div><b>{e(ui['nav_coaches'])}</b><ul>{links}</ul></div>
<div><b>{e(gu['nav_guides'])}</b><ul>{cats}<li><a href="/{lang}/read-next/">{e(gu['quiz_nav'])}</a></li><li><a href="/{lang}/tools/">{e(TL.IDX[lang]['nav'])}</a></li><li><a href="/{lang}/printables/">{e(PR.P[lang]['h1'])}</a></li><li><a href="/{lang}/feed.xml">RSS</a></li></ul></div>
<div><b>{e(ui['footer_links'])}</b><ul><li><a href="/{lang}/">{e(ui['home'])}</a></li><li><a href="/{lang}/prompts/">{e(ui['prompts_all'])}</a></li><li><a href="/{lang}/about/">{e(gu['about'])}</a></li><li><a href="/{lang}/privacy/">{e(ui['privacy'])}</a></li><li><a href="/{lang}/zehn/">Zehn</a></li></ul></div>
<div class="copy">{e(ui['footer_brand'])} · © 2026</div>
</div></footer>
<script>document.addEventListener("click",function(v){{var f=v.target.closest(".fchip");if(f){{var k=f.dataset.k;document.querySelectorAll(".fchip").forEach(function(x){{x.setAttribute("aria-pressed",x===f)}});document.querySelectorAll(".pgroup").forEach(function(g){{g.hidden=!(k==="all"||g.dataset.k===k)}});return}}var b=v.target.closest(".cp");if(!b)return;var t=b.parentNode.querySelector(".pt").textContent;navigator.clipboard.writeText(t).then(function(){{b.textContent=b.dataset.ok;b.classList.add("ok");setTimeout(function(){{b.textContent=b.dataset.l;b.classList.remove("ok")}},1600)}})}});</script>
</body></html>"""


def stores(ui):
    return (f'<div class="stores"><a class="store" href="{C.APP_STORE}" rel="noopener">{APPLE}<span><small>{e(ui["apple_small"])}</small><b>App Store</b></span></a>'
            f'<a class="store" href="{C.GOOGLE_PLAY}" rel="noopener">{PLAY}<span><small>{e(ui["google_small"])}</small><b>Google Play</b></span></a></div>')


def badge(slug, cls="badge"):
    _, _, ik, tint = next(c for c in C.COACHES if c[0] == slug)
    return f'<span class="{cls}" style="background:{tint}">{C.icon(ik)}</span>'


def tldr(ui, items):
    return f'<div class="tldr"><b>{e(ui["tldr"])}</b><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>'


TABS = [("Home", '<path d="M4 11l8-7 8 7v9h-5v-6H9v6H4z"/>'), ("Books", '<rect x="6" y="3" width="12" height="18" rx="1.5"/><path d="M9 8h6M9 12h6M9 16h4"/>'),
        ("AI Chat", '<rect x="5" y="8" width="14" height="10" rx="3"/><path d="M12 8V5M9 12h.01M15 12h.01M8 18l-2 3"/>'),
        ("Book Club", '<circle cx="9" cy="8" r="3"/><circle cx="16" cy="8" r="2.4"/><path d="M3 19c0-3.3 2.7-5 6-5s6 1.7 6 5M15 14c3 0 6 1.5 6 4"/>'),
        ("Library", '<path d="M5 4v16M9 4v16M13 4v16M17 4l3 16"/>')]


def chip(slug):
    app, ik = next((c[1], c[2]) for c in C.COACHES if c[0] == slug)
    return f'<span class="chip"><svg viewBox="0 0 24 24" aria-hidden="true">{C.ICONS[ik]}</svg>{e(app)}</span>'


def phone(lang, h):
    """HTML rebuild of the Zehn AI Chat tab (layout from assets/app_ui_and_CTA/ai_chat_ui/ai_chat_grok_personas.webp).
    App chrome stays English like the real app; the chat text is in-language."""
    rtl = ' dir="rtl"' if lang == "ar" else ""
    others = [c[0] for c in C.COACHES if c[0] != h["phone_persona"]][:4]
    tabs = "".join(f'<div class="tab{" on" if n == "AI Chat" else ""}"><svg viewBox="0 0 24 24">{p}</svg>{n}</div>' for n, p in TABS)
    return f"""<div><div class="phone" role="img" aria-label="Zehn AI Chat"><div class="scr" aria-hidden="true"><div class="isl"></div>
<div class="st"><span>9:41</span><span>5G</span></div>
<div class="hd"><svg viewBox="0 0 24 24"><path d="M3 6h18M3 12h14M3 18h18"/></svg><b>Claude</b><svg viewBox="0 0 24 24" style="width:16px;height:16px"><path d="M6 9l6 6 6-6"/></svg><svg class="dt" viewBox="0 0 24 24"><path d="M12 5h.01M12 12h.01M12 19h.01" stroke-width="3"/></svg></div>
<div class="pc">{chip(h['phone_persona'])}</div>
<div class="me"><span{rtl}>{e(h['phone_q'])}</span></div>
<div class="ai"{rtl}>{e(h['phone_a'])}</div>
<div class="chips">{''.join(chip(s) for s in others)}</div>
<div class="inp"><div class="plus"><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></div><div class="box">Ask anything…<svg viewBox="0 0 24 24"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg></div></div>
<div class="tabs">{tabs}</div></div></div>
<p class="cap">{e(h['phone_cap'])}</p></div>"""


def write(rel, text):
    p = os.path.join(DIST, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)


def coach_cards(lang):
    co, ui = L[lang].COACHES, L[lang].UI
    out = []
    for s, *_ in C.COACHES:
        c = co[s]
        out.append(f'<a class="card" href="/{lang}/{s}/">{badge(s)}<h3>{e(c["name"])}</h3><p>{e(c["short"])}</p><span class="more">{e(ui["view_coach"])} →</span></a>')
    return "".join(out)


def build_home(lang):
    m = L[lang]
    ui, h = m.UI, m.HOME
    check_faq("home", lang, h["faq"])
    items = [{"@type": "ListItem", "position": i + 1, "url": url(lang, s + "/"), "name": m.COACHES[s]["name"]} for i, (s, *_) in enumerate(C.COACHES)]
    ld = [org_ld(), site_ld(),
          {"@type": "WebPage", "@id": url(lang) + "#page", "url": url(lang), "name": h["title"], "description": h["desc"],
           "inLanguage": lang, "isPartOf": {"@id": SITE_ID}, "about": zehn_ld(lang),
           "mainEntity": {"@type": "ItemList", "name": h["grid_h"], "itemListElement": items}},
          faq_ld(h["faq"])]
    pts = "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in h["what_points"])
    steps = "".join(f"<li><div><b>{e(a)}</b><span>{e(b)}</span></div></li>" for a, b in h["how_steps"])
    facts = "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in h["zehn_facts"])
    faq = "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in h["faq"])
    body = f"""<section class="hero"><div class="wrap">
<div><span class="eyebrow">{e(h['eyebrow'])}</span><h1>{e(h['h1'])}</h1><p class="sub">{e(h['sub'])}</p>
{tldr(ui, h['tldr'])}
<div class="btns"><a class="btn p" href="#coaches">{e(h['cta1'])}</a><a class="btn g" href="{C.ZEHN}/{lang}/ai-chat/">{e(h['cta2'])}</a></div></div>
{phone(lang, h)}
</div></section>
<section><div class="wrap narrow"><h2>{e(h['what_h'])}</h2><p class="lead">{e(h['what_p'])}</p><div class="points">{pts}</div></div></section>
<section class="alt" id="coaches"><div class="wrap"><h2>{e(h['grid_h'])}</h2><p class="lead">{e(h['grid_p'])}</p><div class="grid">{coach_cards(lang)}</div></div></section>
<section><div class="wrap narrow"><h2>{e(h['how_h'])}</h2><ol class="steps">{steps}</ol></div></section>
<section><div class="wrap"><div class="zband"><div><h2>{e(h['zehn_h'])}</h2><p>{e(h['zehn_p'])} <a class="ln" style="color:var(--mint)" href="{C.ZEHN}/{lang}/ask-ai/">{e(h['askai_link'])}</a></p>
{stores(ui)}<p class="price">{e(ui['pricing'])}</p></div><div class="facts">{facts}</div></div></div></section>
{home_guides(lang)}
<section class="faq"><div class="wrap narrow"><h2>{e(ui['faq_h'])}</h2>{faq}</div></section>"""
    write(f"{lang}/index.html", head(lang, h["title"], h["desc"], "", ld) + header(lang, "") + body + footer(lang))


def build_coach(lang, slug):
    m = L[lang]
    ui, c = m.UI, m.COACHES[slug]
    app = next(x[1] for x in C.COACHES if x[0] == slug)
    path = slug + "/"
    check_faq(slug, lang, c["faq"])
    if not 10 <= len(c["prompts"]) <= 15:
        WARN.append(f"prompts {len(c['prompts'])} {lang}/{slug}")
    ld = [org_ld(), site_ld(),
          {"@type": "Article", "@id": url(lang, path) + "#article", "headline": c["h1"], "description": c["desc"],
           "inLanguage": lang, "url": url(lang, path), "mainEntityOfPage": url(lang, path), "image": f"{C.BASE}/og/og-{lang}.jpg",
           "datePublished": PUBLISHED, "dateModified": MODIFIED, "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID},
           "isPartOf": {"@id": SITE_ID}, "about": c["name"], "mentions": zehn_ld(lang)},
          faq_ld(c["faq"]),
          crumbs_ld([(ui["home"], url(lang)), (c["name"], url(lang, path))])]
    notes = ""
    if slug in C.SENSITIVE:
        notes = (f'<div class="note warn" role="note"><b>{e(ui["crisis_h"])}</b><p>{e(ui["crisis_p"])} '
                 f'<a href="https://findahelpline.com" rel="noopener">findahelpline.com</a>.</p></div>')
    if slug == "money-coach":
        notes = f'<div class="note info" role="note"><b>{e(ui["money_h"])}</b><p>{e(ui["money_p"])}</p></div>'
    helps = "".join(f"<li>{e(x)}</li>" for x in c["helps"])
    prompts = "".join(f'<li><p class="pt">{e(p)}</p><button class="cp" type="button" data-l="{e(ui["copy"])}" data-ok="{e(ui["copied"])}">{e(ui["copy"])}</button></li>' for p in c["prompts"])
    exs = ""
    for x in c["examples"]:
        turns = "".join(f'<div class="turn {r}"><p><small>{e(ui[r] if r == "you" else c["name"])}</small>{e(t)}</p></div>' for r, t in x["turns"])
        exs += f'<div class="ex"><h3><span class="tag">{e(ui["example_label"])}</span>{e(x["title"])}</h3>{turns}</div>'
    tips = "".join(f"<li>{e(t)}</li>" for t in c["tips"])
    faq = "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in c["faq"])
    rel = "".join(f'<a href="/{lang}/{s}/">{C.icon(ik)}{e(m.COACHES[s]["name"])}</a>' for s, _, ik, _ in C.COACHES if s != slug)
    body = f"""<div class="wrap narrow page">
<nav class="crumbs" aria-label="breadcrumb"><ol><li><a href="/{lang}/">{e(ui['home'])}</a></li><li aria-current="page">{e(c['name'])}</li></ol></nav>
<div class="chead">{badge(slug)}<h1>{e(c['h1'])}</h1></div>
<p class="lead">{e(c['lead'])}</p>
{tldr(ui, c['tldr'])}
{notes}
<section><h2>{e(ui['helps_h'])}</h2><ul class="checks">{helps}</ul></section>
<section id="prompts"><h2>{e(ui['prompts_h'])}</h2><p class="muted">{e(ui['prompts_note'])}</p><ol class="plist">{prompts}</ol></section>
<section><h2>{e(ui['examples_h'])}</h2><p class="muted">{e(ui['example_note'])}</p>{exs}</section>
<section><h2>{e(ui['tips_h'])}</h2><ul class="tips">{tips}</ul></section>
<section><div class="cta"><h2>{e(ui['cta_h'])}</h2>
<div class="path"><span>Zehn</span>→<span>AI Chat</span>→{chip(slug)}</div>
<p>{e(ui['cta_p'].format(app=app))} <a class="ln" href="{C.ZEHN}/{lang}/ai-chat/">{e(ui['cta_more'])}</a></p>
{stores(ui)}<p class="price">{e(ui['pricing'])}</p></div></section>
<section class="faq"><h2>{e(ui['faq_h'])}</h2>{faq}</section>
<section><h2>{e(ui['related_h'])}</h2><div class="related">{rel}</div></section>
</div>"""
    write(f"{lang}/{slug}/index.html", head(lang, c["title"], c["desc"], path, ld) + header(lang, path) + body + footer(lang))


def build_prompts(lang):
    m = L[lang]
    ui, p = m.UI, m.PROMPTS_PAGE
    path = "prompts/"
    n = sum(len(m.COACHES[s]["prompts"]) for s, *_ in C.COACHES)
    ld = [org_ld(), site_ld(),
          {"@type": "CollectionPage", "url": url(lang, path), "name": p["h1"], "description": p["desc"], "inLanguage": lang, "isPartOf": {"@id": SITE_ID},
           "hasPart": [{"@type": "Article", "url": url(lang, s + "/"), "headline": m.COACHES[s]["h1"]} for s, *_ in C.COACHES]},
          crumbs_ld([(ui["home"], url(lang)), (p["h1"], url(lang, path))])]
    groups = ""
    for s, *_ in C.COACHES:
        c = m.COACHES[s]
        li = "".join(f'<li><p class="pt">{e(x)}</p><button class="cp" type="button" data-l="{e(ui["copy"])}" data-ok="{e(ui["copied"])}">{e(ui["copy"])}</button></li>' for x in c["prompts"])
        groups += (f'<div class="pgroup" data-k="{s}"><h2>{badge(s)}<a href="/{lang}/{s}/" style="color:inherit;text-decoration:none">{e(c["name"])}</a></h2>'
                   f'<ol class="plist">{li}</ol><p style="margin-top:10px"><a href="/{lang}/{s}/">{e(p["see_all"])} →</a></p></div>')
    chips = f'<button class="fchip" type="button" data-k="all" aria-pressed="true">{e(p["filter_all"])}</button>' + "".join(
        f'<button class="fchip" type="button" data-k="{s}" aria-pressed="false">{C.icon(ik)}{e(m.COACHES[s]["name"])}</button>' for s, _, ik, _ in C.COACHES)
    groups = f'<div class="filters" role="group" aria-label="{e(p["filter_label"])}">{chips}</div>' + groups
    body = f"""<div class="wrap narrow page">
<nav class="crumbs" aria-label="breadcrumb"><ol><li><a href="/{lang}/">{e(ui['home'])}</a></li><li aria-current="page">{e(p['h1'])}</li></ol></nav>
<h1 style="margin-top:18px">{e(p['h1'])}</h1><p class="lead">{e(p['lead'])}</p>
{tldr(ui, p['tldr'])}<p class="muted">{e(ui['prompts_note'])}</p>
{groups}</div>"""
    if n != 108:
        WARN.append(f"prompt total {n} != 108 ({lang})")
    write(f"{lang}/prompts/index.html", head(lang, p["title"], p["desc"], path, ld) + header(lang, path) + body + footer(lang))


def build_privacy(lang):
    m = L[lang]
    ui, p = m.UI, m.PRIVACY
    path = "privacy/"
    ld = [org_ld(), site_ld(), {"@type": "WebPage", "url": url(lang, path), "name": p["h1"], "inLanguage": lang, "isPartOf": {"@id": SITE_ID}},
          crumbs_ld([(ui["home"], url(lang)), (p["h1"], url(lang, path))])]
    secs = "".join(f"<h2 style='font-size:1.3rem;margin-top:26px'>{e(a)}</h2><p>{e(b)}</p>" for a, b in p["body"])
    body = f"""<div class="wrap narrow page">
<nav class="crumbs" aria-label="breadcrumb"><ol><li><a href="/{lang}/">{e(ui['home'])}</a></li><li aria-current="page">{e(p['h1'])}</li></ol></nav>
<h1 style="margin-top:18px">{e(p['h1'])}</h1><p class="muted">{e(ui['updated'])}: {e(p['updated'])}</p>{secs}</div>"""
    write(f"{lang}/privacy/index.html", head(lang, p["title"], p["desc"], path, ld) + header(lang, path) + body + footer(lang))


def build_root():
    p = L["en"].PICKER
    ld = [org_ld(), site_ld()]
    cards = "".join(f'<a href="/{x}/" hreflang="{x}" lang="{x}">{e(L[x].UI["lang_name"])}<span>{e(L[x].HOME["h1"])}</span></a>' for x in C.LANGS)
    page = head(None, p["title"], p["desc"], "", ld)
    page = page.replace(FONTS["en"], FONTS["en"] + "&family=Cairo:wght@700")
    body = f"""<main id="main" class="picker"><div class="wrap narrow"><a class="brand" href="/">{LOGO}Intellect AI</a>
<h1 style="margin-top:22px">{e(L['en'].HOME['h1'])}</h1><p class="lead">{e(p['sub'])}</p><div class="langs-big">{cards}</div>
<p class="muted" style="margin-top:28px">{e(L['en'].UI['footer_brand'])}</p></div></main></body></html>"""
    write("index.html", page + body)


def build_404():
    m = L["en"]
    ui = m.UI
    page = head("en", "Page not found | Intellect AI", "This page does not exist.", "404/", [org_ld()], alts=False, noindex=True)
    page = page.replace(f'<link rel="canonical" href="{url("en", "404/")}">', "")
    body = f"""<div class="wrap narrow page"><h1 style="margin-top:40px">{e(ui['not_found_h'])}</h1><p class="lead">{e(ui['not_found_p'])}</p>
<div class="grid">{coach_cards('en')}</div></div>"""
    write("404.html", page + header("en", "") + body + footer("en"))


CLUB_LOGO = ('<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M32 30c-8-1-12-7-12-15 8 0 12 6 12 15zm0 0c8-1 12-7 12-15-8 0-12 6-12 15z" fill="none" stroke="#5be26a" stroke-width="3" stroke-linejoin="round"/>'
             '<path d="M14 40c6-4 12 4 18 0s12-4 18 0M14 48c6-4 12 4 18 0s12-4 18 0" fill="none" stroke="#5be26a" stroke-width="3" stroke-linecap="round"/></svg>')


def club_ui(lang):
    """HTML rebuild of a Zehn Book Club screen (layout from assets/app_ui_and_CTA/book_club_ui/club_calm_club.webp).
    App chrome stays English like the real app. No member count, no real user's post: an example post only."""
    gu = G[lang].UI
    post_t, post_b = gu["club_post"]
    rtl = ' dir="rtl"' if lang == "ar" else ""
    return f"""<figure class="uifig"><div class="phone" role="img" aria-label="Zehn Book Club"><div class="scr club" aria-hidden="true"><div class="isl"></div>
<div class="st"><span>9:41</span><span>5G</span></div>
<div class="cbar"><svg viewBox="0 0 24 24"><path d="M19 12H5M11 6l-6 6 6 6"/></svg><span class="lb"><svg viewBox="0 0 24 24"><path d="M4 20h16M7 20v-5h4v5M13 20V11h4v9M12 3l1 2 2 .3-1.5 1.4.4 2.1L12 8l-1.9.8.4-2.1L9 5.3l2-.3z"/></svg></span></div>
<div class="cover">{CLUB_LOGO}<i></i><b>Calm Club</b></div>
<div class="crow"><b>Calm Club</b><span class="pill">Mindfulness &amp; Happiness</span><span class="pill">Leave</span></div>
<p class="cdesc">A quieter club. Focus, attention, and doing less but better.</p>
<div class="rules"><b>Club Rules:</b><span>Read the rules of this club before participating…</span></div>
<div class="comp"><svg viewBox="0 0 24 24"><path d="M4 20h4L19 9l-4-4L4 16zM14 6l4 4"/></svg>What’s on your mind today?</div>
<div class="ctabs"><span class="on">Posts</span><span>Challenges</span></div>
<div class="post"><small>{e(gu['club_member'])}</small><span class="pill sm">Calm Club</span><b{rtl}>{e(post_t)}</b><p{rtl}>{e(post_b)}</p><span class="cm">Comments</span></div>
</div></div><figcaption class="cap">{e(gu['ui_cap_club'])}</figcaption></figure>"""


def blocks(lang, items):
    out = []
    for b in items:
        if isinstance(b, str):
            out.append(f"<p>{md(b)}</p>")
            continue
        k = b[0]
        if k in ("ul", "ol"):
            out.append(f'<{k} class="gl">' + "".join(f"<li>{md(x)}</li>" for x in b[1]) + f"</{k}>")
        elif k == "table":
            hd = "".join(f"<th scope=\"col\">{md(x)}</th>" for x in b[1])
            rows = "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in b[2])
            out.append(f'<div class="tbl"><table><thead><tr>{hd}</tr></thead><tbody>{rows}</tbody></table></div>')
        elif k == "tip":
            out.append(f'<div class="note info"><p>{md(b[1])}</p></div>')
        elif k == "prompt":
            ui = L[lang].UI
            out.append(f'<ol class="plist one"><li><p class="pt">{e(b[1])}</p><button class="cp" type="button" data-l="{e(ui["copy"])}" data-ok="{e(ui["copied"])}">{e(ui["copy"])}</button></li></ol>')
        elif k == "sources":
            out.append('<div class="src"><b>' + e(G[lang].UI.get("sources_h", "Sources")) + '</b><ul>' + "".join(
                f'<li><a href="{u}" rel="noopener nofollow">{e(n)}</a>, {e(d)}</li>' for n, u, d in b[1]) + "</ul></div>")
        elif k == "ui":
            out.append(club_ui(lang) if b[1] == "club" else '<figure class="uifig">' + phone(lang, L[lang].HOME) + "</figure>")
    return "".join(out)


def gwords(g):
    parts = [g["lead"]] + g["tldr"] + [g.get("answer", "")]
    for _, bl in g["sections"]:
        for b in bl:
            if isinstance(b, str):
                parts.append(b)
            elif b[0] in ("ul", "ol"):
                parts += b[1]
            elif b[0] == "table":
                parts += b[1] + [c for r in b[2] for c in r]
            elif b[0] in ("tip", "prompt"):
                parts.append(b[1])
    parts += [q + " " + a for q, a in g["faq"]]
    return words(" ".join(parts))


def guide_card(lang, k, g):
    gu = G[lang].UI
    cat = G[lang].CATS[g["cat"]][0]
    return (f'<a class="card" href="/{lang}/{gpath(k, g)}"><span class="kicker">{e(cat)}</span><h3>{e(g["h1"])}</h3>'
            f'<p>{e(g["desc"])}</p><span class="more">{e(gu["read_min"].format(n=max(3, round(gwords(g) / 220))))} →</span></a>')


def home_guides(lang):
    gu, q = G[lang].UI, G[lang].QUIZ
    picks = ["read-more-books", "how-to-start-a-book-club", "learn-a-language-with-ai", "what-is-zehn", "remember-what-you-read"]
    ag = dict(all_guides(lang))
    cards = "".join(guide_card(lang, k, ag[k]) for k in picks)
    quiz = (f'<a class="card quizcard" href="/{lang}/read-next/"><span class="kicker">Quiz</span><h3>{e(q["h1"])}</h3>'
            f'<p>{e(q["lead"])}</p><span class="more">{e(q["show"])} →</span></a>')
    return f"""<section class="alt"><div class="wrap"><h2>{e(gu['home_guides_h'])}</h2><p class="lead">{e(gu['home_guides_p'])}</p>
<div class="grid">{quiz}{cards}</div><p style="margin-top:18px"><a href="/{lang}/guides/">{e(gu['all_guides'])} →</a></p></div></section>"""


def build_guide(lang, k, g):
    ui, gu = L[lang].UI, G[lang].UI
    path = gpath(k, g)
    check_faq(f"guide {k}", lang, g["faq"])
    n = gwords(g)
    if n < ((700 if lang == "en" else 550) if g.get("kind") != "qa" else (330 if lang == "en" else 260)):
        WARN.append(f"thin guide {lang}/{k}: {n} words")
    if g.get("answer") and not ((40 if lang == "en" else 30) <= words(g["answer"]) <= (60 if lang == "en" else 70)):
        WARN.append(f"answer {words(g['answer'])} words {lang}/{k}")
    cat = G[lang].CATS[g["cat"]][0]
    ld = [org_ld(), site_ld(),
          {"@type": "Article", "@id": url(lang, path) + "#article", "headline": g["h1"], "description": g["desc"], "inLanguage": lang,
           "url": url(lang, path), "mainEntityOfPage": url(lang, path), "image": f"{C.BASE}/og/og-{lang}.jpg", "wordCount": n,
           "datePublished": g.get("date", PUBLISHED), "dateModified": g.get("date", MODIFIED), "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID},
           "isPartOf": {"@id": SITE_ID}, "articleSection": cat, **({"about": zehn_ld(lang)} if g["cat"] == "zehn-guides" else {})},
          faq_ld(g["faq"]),
          crumbs_ld([(ui["home"], url(lang)), (gu["nav_guides"], url(lang, "guides/")), (g["h1"], url(lang, path))])]
    secs = "".join(f'<section><h2>{e(h)}</h2>{blocks(lang, bl)}</section>' for h, bl in g["sections"])
    faq = "".join(f"<h3>{e(q)}</h3><p>{md(a)}</p>" for q, a in g["faq"])
    ch, cp = g.get("cta") or (gu["cta_default_h"], gu["cta_default_p"])
    ag = dict(all_guides(lang))
    rel = "".join(guide_card(lang, r, ag[r]) for r in g["related"] if r in ag)
    body = f"""<div class="wrap narrow page">
<nav class="crumbs" aria-label="breadcrumb"><ol><li><a href="/{lang}/">{e(ui['home'])}</a></li><li><a href="/{lang}/guides/#{g['cat']}">{e(cat)}</a></li><li aria-current="page">{e(g['h1'])}</li></ol></nav>
<h1 style="margin-top:18px">{e(g['h1'])}</h1>
<p class="muted">{e(gu['read_min'].format(n=max(3, round(n / 220))))} · {e(gu['updated'])}: {e(g.get('date_h', G[lang].DATE))}</p>
<p class="lead">{md(g['lead'])}</p>
{('<div class="answer"><b>' + e(gu.get('answer_h', 'Short answer')) + '</b><p>' + md(g['answer']) + '</p></div>') if g.get('answer') else ''}
{tldr(ui, g['tldr'])}
{secs}
<section><div class="cta"><h2>{e(ch)}</h2><p>{e(cp)}</p>{stores(ui)}<p class="price">{e(ui['pricing'])}</p></div></section>
<section class="faq"><h2>{e(ui['faq_h'])}</h2>{faq}</section>
<section><h2>{e(gu['related_h'])}</h2><div class="grid g2">{rel}</div></section>
</div>"""
    write(f"{lang}/{path}index.html", head(lang, g["title"], g["desc"], path, ld) + header(lang, path) + body + footer(lang))


def build_guides_index(lang):
    ui, gu = L[lang].UI, G[lang].UI
    path = "guides/"
    gs = all_guides(lang)
    ld = [org_ld(), site_ld(),
          {"@type": "CollectionPage", "url": url(lang, path), "name": gu["guides_h1"], "description": gu["guides_desc"], "inLanguage": lang, "isPartOf": {"@id": SITE_ID},
           "hasPart": [{"@type": "Article", "url": url(lang, gpath(k, g)), "headline": g["h1"]} for k, g in gs]},
          crumbs_ld([(ui["home"], url(lang)), (gu["nav_guides"], url(lang, path))])]
    secs = ""
    for ck, (cn, cd) in G[lang].CATS.items():
        cards = "".join(guide_card(lang, k, g) for k, g in gs if g["cat"] == ck)
        if ck == "reading-habits":
            q = G[lang].QUIZ
            cards += f'<a class="card quizcard" href="/{lang}/read-next/"><span class="kicker">Quiz</span><h3>{e(q["h1"])}</h3><p>{e(q["lead"])}</p><span class="more">{e(q["show"])} →</span></a>'
        secs += f'<section id="{ck}"><h2>{e(cn)}</h2><p class="muted">{e(cd)}</p><div class="grid g2">{cards}</div></section>'
    body = f"""<div class="wrap page" style="max-width:980px">
<nav class="crumbs" aria-label="breadcrumb"><ol><li><a href="/{lang}/">{e(ui['home'])}</a></li><li aria-current="page">{e(gu['nav_guides'])}</li></ol></nav>
<h1 style="margin-top:18px">{e(gu['guides_h1'])}</h1><p class="lead">{e(gu['guides_lead'])}</p>{tldr(ui, gu['guides_tldr'])}
{secs}</div>"""
    write(f"{lang}/{path}index.html", head(lang, gu["guides_title"], gu["guides_desc"], path, ld) + header(lang, path) + body + footer(lang))


def build_about(lang):
    ui, gu, a = L[lang].UI, G[lang].UI, G[lang].ABOUT
    path = "about/"
    ld = [org_ld(), site_ld(), {"@type": "AboutPage", "url": url(lang, path), "name": a["h1"], "inLanguage": lang, "isPartOf": {"@id": SITE_ID}, "about": {"@id": ORG_ID}},
          crumbs_ld([(ui["home"], url(lang)), (a["h1"], url(lang, path))])]
    secs = "".join(f"<h2 style='font-size:1.3rem;margin-top:26px'>{e(h)}</h2><p>{md(t)}</p>" for h, t in a["body"])
    body = f"""<div class="wrap narrow page">
<nav class="crumbs" aria-label="breadcrumb"><ol><li><a href="/{lang}/">{e(ui['home'])}</a></li><li aria-current="page">{e(a['h1'])}</li></ol></nav>
<h1 style="margin-top:18px">{e(a['h1'])}</h1>{tldr(ui, a['tldr'])}{secs}
<p><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p></div>"""
    write(f"{lang}/{path}index.html", head(lang, a["title"], a["desc"], path, ld) + header(lang, path) + body + footer(lang))


def build_quiz(lang):
    ui, gu, q = L[lang].UI, G[lang].UI, G[lang].QUIZ
    path = "read-next/"
    check_faq("quiz", lang, q["faq"])
    ld = [org_ld(), site_ld(),
          {"@type": "WebApplication", "name": q["h1"], "url": url(lang, path), "applicationCategory": "EducationalApplication", "operatingSystem": "Any",
           "isAccessibleForFree": True, "inLanguage": lang, "publisher": {"@id": ORG_ID}, "description": q["desc"]},
          faq_ld(q["faq"]), crumbs_ld([(ui["home"], url(lang)), (q["h1"], url(lang, path))])]

    def opts(name, items):
        return "".join(f'<label class="opt"><input type="radio" name="{name}" value="{k}"{" checked" if i == 0 and name != "g" else ""}><span>{e(t)}</span></label>' for i, (k, t) in enumerate(items))
    data = {k: v[lang] for k, v in BOOKS.items()}
    tips = {"commute": q["tip_commute"], "evening": q["tip_evening"], "weekend": q["tip_weekend"]}
    faq = "".join(f"<h3>{e(a)}</h3><p>{md(b)}</p>" for a, b in q["faq"])
    js = ("var B=" + json.dumps(data, ensure_ascii=False) + ",T=" + json.dumps(tips, ensure_ascii=False) + ",M=" + json.dumps(q["minutes"], ensure_ascii=False)
          + ",O=" + json.dumps(q["open"], ensure_ascii=False) + ";"
          """var f=document.getElementById("qz"),r=document.getElementById("qr");f.addEventListener("submit",function(v){v.preventDefault();var d=new FormData(f),g=d.get("g");if(!g){f.querySelector("input[name=g]").focus();return}
var b=B[g].slice();if(d.get("m")==="light")b.sort(function(x,y){return x.m-y.m});b=b.slice(0,3);var h="";b.forEach(function(x){h+='<li><a href="'+x.u+'" rel="noopener"><b></b><span></span><em></em></a></li>'});
r.querySelector("ol").innerHTML=h;var li=r.querySelectorAll("li");b.forEach(function(x,i){li[i].querySelector("b").textContent=x.t;li[i].querySelector("span").textContent=x.a;li[i].querySelector("em").textContent=M.replace("{n}",x.m)+" · "+O+" →"});
r.querySelector(".qtip").textContent=T[d.get("t")];r.hidden=false;r.scrollIntoView({behavior:"smooth",block:"start"});r.focus()});
document.getElementById("qa").addEventListener("click",function(){r.hidden=true;f.reset();window.scrollTo({top:0,behavior:"smooth"})});""")
    body = f"""<div class="wrap narrow page">
<nav class="crumbs" aria-label="breadcrumb"><ol><li><a href="/{lang}/">{e(ui['home'])}</a></li><li aria-current="page">{e(q['h1'])}</li></ol></nav>
<h1 style="margin-top:18px">{e(q['h1'])}</h1><p class="lead">{e(q['lead'])}</p>{tldr(ui, q['tldr'])}
<form id="qz" class="quiz">
<fieldset><legend>1. {e(q['q1'])}</legend><div class="opts">{opts('g', q['goals'])}</div></fieldset>
<fieldset><legend>2. {e(q['q2'])}</legend><div class="opts">{opts('m', q['moods'])}</div></fieldset>
<fieldset><legend>3. {e(q['q3'])}</legend><div class="opts">{opts('t', q['times'])}</div></fieldset>
<button class="btn p" type="submit">{e(q['show'])}</button></form>
<div id="qr" class="qres" hidden tabindex="-1"><h2>{e(q['result_h'])}</h2><ol class="books"></ol><p class="qtip muted"></p>
{stores(ui)}<p class="price">{e(ui['pricing'])}</p><button id="qa" class="btn ghost" type="button">{e(q['again'])}</button></div>
<section><h2>{e(q['more_h'])}</h2><p>{e(q['more_p'])}</p></section>
<section class="faq"><h2>{e(ui['faq_h'])}</h2>{faq}</section></div>
<script>{js}</script>"""
    write(f"{lang}/{path}index.html", head(lang, q["title"], q["desc"], path, ld) + header(lang, path) + body + footer(lang))


import tools as TL  # noqa: E402

WPM = {"en": 250, "ru": 200, "ar": 180}


def tool_widget(lang, slug, t):
    ui = L[lang].UI
    if slug == "reading-time-calculator":
        f, r = t["f"], t["r"]
        inp = lambda k, v, mn, mx: f'<label class="fld"><span>{e(f[k])}</span><input type="number" inputmode="numeric" id="{k}" value="{v}" min="{mn}" max="{mx}"></label>'
        js = ("var R=" + json.dumps(r, ensure_ascii=False) + ";"
              """function c(){var g=function(i){return Math.max(1,+document.getElementById(i).value||0)};var m=g('pages')*g('wpp')/g('wpm');var h=Math.floor(m/60),mi=Math.round(m%60);
document.getElementById('o1').textContent=R.hm.replace('{h}',h).replace('{m}',mi);document.getElementById('o2').textContent=R.d.replace('{d}',Math.ceil(m/g('mpd')));document.getElementById('o3').textContent=R.s;}
document.getElementById('calc').addEventListener('input',c);document.getElementById('calc').addEventListener('submit',function(v){v.preventDefault();c()});c();""")
        return (f'<form id="calc" class="tool"><div class="fgrid">{inp("pages", 300, 1, 5000)}{inp("wpp", 250, 50, 1000)}{inp("wpm", WPM[lang], 50, 1000)}{inp("mpd", 20, 1, 600)}</div>'
                f'<button class="btn p" type="submit">{e(f["go"])}</button></form>'
                f'<div class="outs" aria-live="polite"><div><span>{e(r["hours"])}</span><b id="o1"></b></div><div><span>{e(r["days"])}</span><b id="o2"></b></div><div><span>{e(r["sum"])}</span><b id="o3"></b></div></div>'
                f'<script>{js}</script>')
    if slug == "book-club-name-generator":
        f = t["f"]
        sel = lambda i, items: f'<select id="{i}">' + "".join(f'<option value="{k}">{e(v)}</option>' for k, v in items) + "</select>"
        pats = {"en": ["{a} {n}", "The {a} {n}", "{a} {t}", "{t} {n}"], "ru": ["{N} «{a}»", "«{a}»", "«{t}»", "{N} «{t}»"], "ar": ["{n} «{a}»", "«{a}»", "«{t}»", "{n} «{t}»"]}[lang]
        js = ("var W=" + json.dumps(TL.NAMES[lang], ensure_ascii=False) + ",P=" + json.dumps(pats, ensure_ascii=False) + ",CP=" + json.dumps(f["copy"], ensure_ascii=False) + ",OK=" + json.dumps(ui["copied"], ensure_ascii=False) + ";"
              """function pk(a){return a[Math.floor(Math.random()*a.length)]}
function gen(){var th=document.getElementById('th').value,st=document.getElementById('st').value,o=document.getElementById('names'),seen={},out=[];var A=W.a[st],T=W.t[th].concat(th==='any'?[]:W.t.any);
for(var i=0;i<60&&out.length<6;i++){var n=pk(W.n);var s=pk(P).replace('{a}',pk(A)).replace('{t}',pk(T)).replace('{n}',n).replace('{N}',n.charAt(0).toUpperCase()+n.slice(1));if(!seen[s]){seen[s]=1;out.push(s)}}
o.innerHTML='';out.forEach(function(s){var li=document.createElement('li');var p=document.createElement('p');p.className='pt';p.textContent=s;var b=document.createElement('button');b.type='button';b.className='cp';b.dataset.l=CP;b.dataset.ok=OK;b.textContent=CP;li.appendChild(p);li.appendChild(b);o.appendChild(li)})}
document.getElementById('gen').addEventListener('submit',function(v){v.preventDefault();gen()});gen();""")
        return (f'<form id="gen" class="tool"><div class="fgrid"><label class="fld"><span>{e(f["theme"])}</span>{sel("th", t["themes"])}</label>'
                f'<label class="fld"><span>{e(f["style"])}</span>{sel("st", t["styles"])}</label></div><button class="btn p" type="submit">{e(f["go"])}</button></form>'
                f'<ol id="names" class="plist one" aria-live="polite"></ol><script>{js}</script>')
    if slug == "reading-challenge-tracker":
        f = t["f"]
        js = ("var F=" + json.dumps(f, ensure_ascii=False) + ";"
              """var gs=document.getElementById('goal'),ys=document.getElementById('yr'),grid=document.getElementById('grid'),st={};
function key(){return 'iai-tracker-'+ys.value}
function load(){try{st=JSON.parse(localStorage.getItem(key())||'{}')}catch(x){st={}}if(st.goal)gs.value=st.goal;draw()}
function save(){try{localStorage.setItem(key(),JSON.stringify(st))}catch(x){}}
function draw(){var g=Math.max(1,Math.min(365,+gs.value||12));st.goal=g;st.t=(st.t||[]).filter(function(i){return i<g});grid.innerHTML='';
for(var i=0;i<g;i++){var b=document.createElement('button');b.type='button';b.className='tick';b.textContent=i+1;b.dataset.i=i;b.setAttribute('aria-pressed',st.t.indexOf(i)>=0);grid.appendChild(b)}stat()}
function stat(){var g=st.goal,n=st.t.length,y=+ys.value,now=new Date(),s=new Date(y,0,1),e=new Date(y+1,0,1),fr=now<s?0:now>=e?1:(now-s)/(e-s);var ex=Math.floor(g*fr),d=n-ex;
document.getElementById('done').textContent=F.done.replace('{n}',n).replace('{g}',g);document.getElementById('bar').style.width=Math.min(100,n/g*100)+'%';
document.getElementById('pace').textContent=d>0?F.pace_ok.replace('{d}',d):d===0?F.pace_even:F.pace_bad.replace('{d}',-d)}
grid.addEventListener('click',function(v){var b=v.target.closest('.tick');if(!b)return;var i=+b.dataset.i,k=st.t.indexOf(i);if(k>=0)st.t.splice(k,1);else st.t.push(i);b.setAttribute('aria-pressed',k<0);save();stat()});
gs.addEventListener('change',function(){draw();save()});ys.addEventListener('change',load);
document.getElementById('rs').addEventListener('click',function(){st={goal:+gs.value,t:[]};save();draw()});document.getElementById('pr').addEventListener('click',function(){window.print()});
var cy=new Date().getFullYear(),nx=new Date().getMonth()>=10;[cy,cy+1].forEach(function(y){var o=document.createElement('option');o.value=y;o.textContent=y;if(nx&&y===cy+1)o.selected=true;ys.appendChild(o)});load();""")
        return (f'<div class="tool"><div class="fgrid"><label class="fld"><span>{e(f["goal"])}</span><select id="goal"><option>12</option><option>24</option><option selected>52</option><option>100</option></select></label>'
                f'<label class="fld"><span>{e(f["year"])}</span><select id="yr"></select></label></div>'
                f'<p class="prog"><b id="done"></b><span class="barw"><span id="bar"></span></span><span id="pace" class="muted"></span></p>'
                f'<div id="grid" class="grid52"></div><div class="btns noprint"><button id="pr" class="btn p" type="button">{e(f["print"])}</button><button id="rs" class="btn ghost" type="button">{e(f["reset"])}</button></div>'
                f'<p class="muted">{e(f["note"])}</p></div><script>{js}</script>')
    return ""


def build_tools(lang):
    ui, gu, ix = L[lang].UI, G[lang].UI, TL.IDX[lang]
    q = G[lang].QUIZ
    for slug, t in TL.TOOLS[lang].items():
        path = f"tools/{slug}/"
        check_faq(f"tool {slug}", lang, t["faq"])
        ld = [org_ld(), site_ld(),
              {"@type": "WebApplication", "name": t["h1"], "url": url(lang, path), "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any",
               "isAccessibleForFree": True, "inLanguage": lang, "publisher": {"@id": ORG_ID}, "description": t["desc"]},
              faq_ld(t["faq"]), crumbs_ld([(ui["home"], url(lang)), (ix["nav"], url(lang, "tools/")), (t["h1"], url(lang, path))])]
        h, ps = t["how"]
        faq = "".join(f"<h3>{e(a)}</h3><p>{md(b)}</p>" for a, b in t["faq"])
        others = "".join(f'<a href="/{lang}/tools/{s}/">{e(o["h1"])}</a>' for s, o in TL.TOOLS[lang].items() if s != slug) + f'<a href="/{lang}/read-next/">{e(q["h1"])}</a>'
        body = f"""<div class="wrap narrow page">
<nav class="crumbs noprint" aria-label="breadcrumb"><ol><li><a href="/{lang}/">{e(ui['home'])}</a></li><li><a href="/{lang}/tools/">{e(ix['nav'])}</a></li><li aria-current="page">{e(t['h1'])}</li></ol></nav>
<h1 style="margin-top:18px">{e(t['h1'])}</h1><p class="lead">{e(t['lead'])}</p>
{tool_widget(lang, slug, t)}
<div class="noprint">{tldr(ui, t['tldr'])}
<section><h2>{e(h)}</h2>{''.join(f'<p>{md(x)}</p>' for x in ps)}</section>
<section class="faq"><h2>{e(ui['faq_h'])}</h2>{faq}</section>
<section><h2>{e(gu['related_h'])}</h2><div class="related">{others}</div></section></div>
</div>"""
        write(f"{lang}/{path}index.html", head(lang, t["title"], t["desc"], path, ld) + header(lang, path) + body + footer(lang))
    path = "tools/"
    cards = "".join(f'<a class="card" href="/{lang}/tools/{s}/"><h3>{e(o["h1"])}</h3><p>{e(o["desc"])}</p><span class="more">{e(ix["open"])} →</span></a>' for s, o in TL.TOOLS[lang].items())
    cards += f'<a class="card quizcard" href="/{lang}/read-next/"><span class="kicker">Quiz</span><h3>{e(q["h1"])}</h3><p>{e(q["lead"])}</p><span class="more">{e(q["show"])} →</span></a>'
    ld = [org_ld(), site_ld(), {"@type": "CollectionPage", "url": url(lang, path), "name": ix["h1"], "inLanguage": lang, "isPartOf": {"@id": SITE_ID}},
          crumbs_ld([(ui["home"], url(lang)), (ix["nav"], url(lang, path))])]
    body = f"""<div class="wrap page" style="max-width:980px"><nav class="crumbs" aria-label="breadcrumb"><ol><li><a href="/{lang}/">{e(ui['home'])}</a></li><li aria-current="page">{e(ix['nav'])}</li></ol></nav>
<h1 style="margin-top:18px">{e(ix['h1'])}</h1><p class="lead">{e(ix['lead'])}</p>{tldr(ui, ix['tldr'])}<div class="grid g2">{cards}</div></div>"""
    write(f"{lang}/{path}index.html", head(lang, ix["title"], ix["desc"], path, ld) + header(lang, path) + body + footer(lang))


import printables as PR  # noqa: E402
KITS = ["tracker", "club", "sheet"]
KIT_PAGES = {"tracker": 1, "club": 2, "sheet": 1}


def kit_html(lang, kit):
    p = PR.P[lang]
    k = p["kits"][kit]
    d = "rtl" if lang == "ar" else "ltr"
    font = "Cairo" if lang == "ar" else "Inter"
    css = (f"@page{{size:A4;margin:14mm}}body{{font-family:'{font}',sans-serif;color:#0B1D2A;font-size:11pt;margin:0}}"
           "h1{font-size:20pt;margin:0 0 4mm}h2{font-size:12.5pt;margin:6mm 0 2mm}table{width:100%;border-collapse:collapse}td,th{border:1px solid #9AA6AE;padding:2.2mm;text-align:start;vertical-align:top}"
           "th{background:#E9F7EF;font-size:9.5pt}.ln td{height:8.4mm}.strip{display:grid;grid-template-columns:repeat(31,1fr);gap:1mm;margin-top:2mm}.strip span{border:1px solid #9AA6AE;height:7mm;font-size:7pt;text-align:center}"
           ".foot{position:fixed;bottom:0;left:0;right:0;font-size:8pt;color:#6B7F90;text-align:center}.two{display:grid;grid-template-columns:1fr 1fr;gap:3mm}.fl{border-bottom:1px solid #9AA6AE;height:9mm;margin-bottom:2mm;font-size:9pt;color:#6B7F90}"
           ".brk{page-break-before:always}.lines{columns:2;column-gap:8mm}.lines div{border-bottom:1px solid #9AA6AE;height:7.7mm;font-size:9pt;display:flex;align-items:flex-end;break-inside:avoid}"
           ".mo{display:grid;grid-template-columns:repeat(4,1fr);gap:1.5mm;font-size:8.5pt;margin:2mm 0 4mm}.mo span{background:#E9F7EF;border-radius:2mm;padding:1.4mm 2mm}.sub{color:#41566A;margin:0 0 3mm}")
    if kit == "tracker":
        rows = "".join("<tr class='ln'>" + "<td></td>" * 6 + "</tr>" for _ in range(15))
        body = (f"<h1>{e(k['h'])}</h1><p>{e(k['month'])}: ____________________</p><table><tr>" + "".join(f"<th>{e(c)}</th>" for c in k["cols"]) + f"</tr>{rows}</table>"
                f"<h2>{e(k['strip'])}</h2><div class='strip'>" + "".join(f"<span>{i}</span>" for i in range(1, 32)) + "</div>")
    elif kit == "club":
        fields = "".join(f"<div class='fl'>{e(f)}</div>" for f in k["fields"])
        rules = "".join(f"<li>{e(r)}</li>" for r in k["rules"])
        roles = "".join(f"<tr><td><b>{e(a)}</b></td><td>{e(b)}</td><td style='width:32%'></td></tr>" for a, b in k["roles"])
        agenda = "".join(f"<li>{e(a)}</li>" for a in k["agenda"])
        qs = "".join(f"<li>{e(q)}</li>" for q in k["qs"])
        body = (f"<h1>{e(k['h'])}</h1><h2>{e(k['card'])}</h2>{fields}<h2>{e(k['rules_h'])}</h2><ol>{rules}</ol><h2>{e(k['roles_h'])}</h2><table>{roles}</table>"
                f"<div class='brk'></div><h2>{e(k['agenda_h'])}</h2><ol>{agenda}</ol><h2>{e(k['q_h'])}</h2><ol>{qs}</ol>")
    else:
        lines = "".join(f"<div>{i}.</div>" for i in range(1, 53))
        body = (f"<h1>{e(k['h'])}</h1><p class='sub'>{e(k['sub'])}</p><div class='mo'>" + "".join(f"<span>{e(m)}</span>" for m in k["months"]) + f"</div><div class='lines'>{lines}</div>")
    return (f"<!doctype html><html lang='{lang}' dir='{d}'><head><meta charset='utf-8'><link rel='stylesheet' href='https://fonts.googleapis.com/css2?{FONTS[lang]}&display=block'>"
            f"<style>{css}</style></head><body>{body}<div class='foot'>{e(p['foot'])}</div></body></html>")


def render_pdfs():
    tmp = os.path.join(ROOT, ".pdf_tmp")
    os.makedirs(tmp, exist_ok=True)
    out = os.path.join(ROOT, "static", "printables")
    os.makedirs(out, exist_ok=True)
    for lang in C.LANGS:
        for kit in KITS:
            hp = os.path.join(tmp, f"{lang}-{kit}.html")
            open(hp, "w", encoding="utf-8").write(kit_html(lang, kit))
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=5000",
                            f"--print-to-pdf={os.path.join(out, f'{lang}-{kit}.pdf')}", "file://" + hp],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, timeout=120)
    shutil.rmtree(tmp)


def build_printables(lang):
    ui, p = L[lang].UI, PR.P[lang]
    path = "printables/"
    check_faq("printables", lang, p["faq"])
    items = ""
    for kit in KITS:
        k = p["kits"][kit]
        n = KIT_PAGES[kit]
        items += (f'<div class="card"><h3>{e(k["name"])}</h3><p>{e(k["what"])}</p><p class="muted">PDF · {e(p["page1"] if n == 1 else p["pages"].format(n=n))}</p>'
                  f'<a class="btn p" href="/printables/{lang}-{kit}.pdf" download>{e(p["dl"])}</a></div>')
    ld = [org_ld(), site_ld(),
          {"@type": "CollectionPage", "url": url(lang, path), "name": p["h1"], "description": p["desc"], "inLanguage": lang, "isPartOf": {"@id": SITE_ID},
           "hasPart": [{"@type": "DigitalDocument", "name": p["kits"][k]["name"], "url": f"{C.BASE}/printables/{lang}-{k}.pdf", "encodingFormat": "application/pdf", "isAccessibleForFree": True} for k in KITS]},
          faq_ld(p["faq"]), crumbs_ld([(ui["home"], url(lang)), (p["h1"], url(lang, path))])]
    faq = "".join(f"<h3>{e(a)}</h3><p>{md(b)}</p>" for a, b in p["faq"])
    body = f"""<div class="wrap page" style="max-width:980px"><nav class="crumbs" aria-label="breadcrumb"><ol><li><a href="/{lang}/">{e(ui['home'])}</a></li><li aria-current="page">{e(p['h1'])}</li></ol></nav>
<h1 style="margin-top:18px">{e(p['h1'])}</h1><p class="lead">{e(p['lead'])}</p>{tldr(ui, p['tldr'])}<div class="grid">{items}</div>
<section><h2>{e(p['use_h'])}</h2><ul class="gl">{''.join(f'<li>{e(x)}</li>' for x in p['use'])}</ul></section>
<section class="faq"><h2>{e(ui['faq_h'])}</h2>{faq}</section></div>"""
    write(f"{lang}/{path}index.html", head(lang, p["title"], p["desc"], path, ld) + header(lang, path) + body + footer(lang))


def build_rss():
    import email.utils as eu, datetime as dt
    for lang in C.LANGS:
        items = []
        for k, g in all_guides(lang):
            d = g.get("date", PUBLISHED)
            items.append((d, g["h1"], url(lang, gpath(k, g)), g["desc"]))
        items.sort(key=lambda x: x[0], reverse=True)
        xi = "".join(f"<item><title>{e(t)}</title><link>{u}</link><guid isPermaLink=\"true\">{u}</guid><pubDate>{eu.format_datetime(dt.datetime.fromisoformat(d + 'T08:00:00+00:00'))}</pubDate><description>{e(ds)}</description></item>" for d, t, u, ds in items)
        h = L[lang].HOME
        write(f"{lang}/feed.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>Intellect AI ({lang.upper()})</title><link>{url(lang)}</link>'
              f'<atom:link href="{url(lang, "feed.xml")}" rel="self" type="application/rss+xml"/><description>{e(h["desc"])}</description><language>{lang}</language>{xi}</channel></rss>\n')


def build_seo():
    gps = []
    for lang in C.LANGS:
        for k, g in all_guides(lang):
            if gpath(k, g) not in gps:
                gps.append(gpath(k, g))
    pages = [""] + [s + "/" for s, *_ in C.COACHES] + ["prompts/", "privacy/", "about/", "guides/", "read-next/", "tools/", "printables/"] + [f"tools/{x}/" for x in TL.TOOLS["en"]] + gps
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
           f"<url><loc>{C.BASE}/</loc><lastmod>{MODIFIED}</lastmod></url>"]
    for p in pages:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{url(x, p)}"/>' for x in avail(p))
        alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{xdefault(p)}"/>'
        for lang in avail(p):
            out.append(f"<url><loc>{url(lang, p)}</loc><lastmod>{MODIFIED}</lastmod>{alts}</url>")
    out.append("</urlset>")
    write("sitemap.xml", "\n".join(out) + "\n")
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User",
            "Google-Extended", "Applebot-Extended", "Bingbot", "CCBot", "meta-externalagent", "DuckAssistBot", "YandexBot"]
    rb = "User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {C.BASE}/sitemap.xml\n"
    write("robots.txt", rb)
    en = L["en"]
    lines = ["# Intellect AI", "",
             "> Free guides, copy-ready prompts and example conversations for nine AI coaching personas (Business Mentor, Money Coach, Productivity Coach, Mindfulness Guide, Psychologist, Negotiator, Language Tutor, Leadership Mentor, Science Explainer). Made by the team behind Zehn, a book-summary app by Safari Group. Available in English, Russian and Arabic.", "",
             "Key facts about Zehn: 10,000+ book summaries, 15-20 minutes a book (audio and text), Ask AI on every book, and an AI Chat tab with the nine personas above and a model picker (Claude, Gemini, DeepSeek, Grok; all four on the yearly plan, one on the monthly plan). Free plan: 1 book a day, no AI. Zehn Pro: $9.99/month or $36/year with a 7-day free trial. 50,000+ readers. iOS: " + C.APP_STORE + " Android: " + C.GOOGLE_PLAY, "",
             "The AI Psychologist and Mindfulness Guide are self-help tools, not therapy or medical advice. The Money Coach is not financial advice.", "",
             "## Coaches (English)"]
    for s, *_ in C.COACHES:
        c = en.COACHES[s]
        lines.append(f"- [{c['h1']}]({url('en', s + '/')}): {c['short']}")
    lines += ["", "## Guides (English)"]
    for k, g in all_guides("en"):
        lines.append(f"- [{g['h1']}]({url('en', gpath(k, g))}): {g['desc']}")
    lines += ["", "## Other pages", f"- [All prompts]({url('en', 'prompts/')}): 108 free prompts, 12 per coach",
              f"- [What should I read next? quiz]({url('en', 'read-next/')}): 3 questions, 3 book picks from Zehn's library",
              f"- [About Intellect AI]({url('en', 'about/')})",
              f"- [Russian version]({url('ru')})", f"- [Arabic version]({url('ar')})", f"- [Privacy]({url('en', 'privacy/')})",
              "", "## Contact", f"- {C.EMAIL}", f"- Zehn website: {C.ZEHN}/"]
    write("llms.txt", "\n".join(lines) + "\n")
    write("_headers", """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=()
/style.css
  Cache-Control: public, max-age=31536000, immutable
/og/*
  Cache-Control: public, max-age=604800
/*.svg
  Cache-Control: public, max-age=604800
""")


def copy_static():
    for f in os.listdir(os.path.join(ROOT, "static")):
        src = os.path.join(ROOT, "static", f)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(DIST, f), dirs_exist_ok=True)
        else:
            shutil.copy2(src, os.path.join(DIST, f))


def render_og():
    """1200x630 OG card per language, rendered from HTML with headless Chrome, saved as JPEG."""
    from PIL import Image
    tmp = os.path.join(ROOT, ".og_tmp")
    os.makedirs(tmp, exist_ok=True)
    os.makedirs(os.path.join(ROOT, "static", "og"), exist_ok=True)
    for lang in C.LANGS:
        h = L[lang].HOME
        d = "rtl" if lang == "ar" else "ltr"
        chips = "".join(f'<span class="c">{C.icon(c[2])}{e(L[lang].COACHES[c[0]]["name"])}</span>' for c in C.COACHES)
        page = f"""<!doctype html><html lang="{lang}" dir="{d}"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{FONTS[lang]}&display=block">
<style>html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}body{{background:radial-gradient(700px 400px at 90% 0%,rgba(61,220,151,.28),transparent 60%),#0B1D2A;color:#fff;
font-family:{'Cairo' if lang=='ar' else 'Manrope'},sans-serif;padding:64px 72px;box-sizing:border-box}}
.b{{display:flex;align-items:center;gap:14px;font-size:30px;font-weight:800}}.b svg{{width:54px;height:54px}}
h1{{font-size:{66 if lang=='en' else 58}px;line-height:1.1;margin:40px 0 18px;max-width:900px;font-weight:800}}
p{{font-size:26px;color:#B9CAD5;margin:0 0 30px;font-family:{'Cairo' if lang=='ar' else 'Inter'},sans-serif}}
.cs{{display:flex;flex-wrap:wrap;gap:10px;max-width:1060px}}.c{{display:inline-flex;align-items:center;gap:8px;background:#12324A;border-radius:12px;padding:8px 14px;font-size:20px;font-weight:700}}
.c svg{{width:22px;height:22px;fill:none;stroke:#3DDC97;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}}</style></head>
<body><div class="b">{LOGO}Intellect AI · Zehn</div><h1>{e(h['h1'])}</h1><p>{e(h['og_sub'])}</p><div class="cs">{chips}</div></body></html>"""
        hp = os.path.join(tmp, f"og_{lang}.html")
        open(hp, "w", encoding="utf-8").write(page)
        png = os.path.join(tmp, f"og_{lang}.png")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,630",
                        "--virtual-time-budget=4000", f"--screenshot={png}", "file://" + hp],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, timeout=90)
        Image.open(png).convert("RGB").resize((1200, 630)).save(os.path.join(ROOT, "static", "og", f"og-{lang}.jpg"), quality=86, optimize=True)
    shutil.rmtree(tmp)


def icons():
    """favicon.svg + PNG app icons rendered from the logo with headless Chrome."""
    st = os.path.join(ROOT, "static")
    open(os.path.join(st, "favicon.svg"), "w").write(LOGO.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ', 1).replace(' aria-hidden="true"', ""))
    if os.path.exists(os.path.join(st, "icon-512.png")):
        return
    from PIL import Image
    tmp = os.path.join(ROOT, ".ic_tmp")
    os.makedirs(tmp, exist_ok=True)
    hp = os.path.join(tmp, "i.html")
    open(hp, "w").write(f"<html><body style='margin:0;width:512px;height:512px;background:#0B1D2A'>{LOGO.replace('<svg ', '<svg width=512 height=512 ', 1).replace('rx=\"9\"', 'rx=\"0\"')}</body></html>")
    png = os.path.join(tmp, "i.png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=512,512", f"--screenshot={png}", "file://" + hp],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, timeout=60)
    im = Image.open(png).convert("RGB").resize((512, 512))
    im.save(os.path.join(st, "icon-512.png"), optimize=True)
    im.resize((180, 180), Image.LANCZOS).save(os.path.join(st, "apple-touch-icon.png"), optimize=True)
    shutil.rmtree(tmp)


STYLE_V = "1"


def main():
    global STYLE_V
    import hashlib
    STYLE_V = hashlib.md5(open(os.path.join(ROOT, "static", "style.css"), "rb").read()).hexdigest()[:8]
    icons()
    if "--pdf" in sys.argv or not os.path.exists(os.path.join(ROOT, "static", "printables", "en-sheet.pdf")):
        render_pdfs()
    if "--og" in sys.argv or not os.path.exists(os.path.join(ROOT, "static", "og", "og-en.jpg")):
        render_og()
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    copy_static()
    for lang in C.LANGS:
        build_home(lang)
        for s, *_ in C.COACHES:
            build_coach(lang, s)
        build_prompts(lang)
        build_privacy(lang)
        build_about(lang)
        build_guides_index(lang)
        for k, g in all_guides(lang):
            build_guide(lang, k, g)
        build_quiz(lang)
        build_tools(lang)
        build_printables(lang)
    build_root()
    build_404()
    build_seo()
    build_rss()
    n = sum(len(fs) for _, _, fs in os.walk(DIST))
    print(f"built {n} files in dist/")
    for w in WARN:
        print("WARN", w)


if __name__ == "__main__":
    main()
