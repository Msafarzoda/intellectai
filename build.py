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
e = lambda s: html.escape(s, quote=True)  # noqa: E731


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
            "sameAs": [C.APP_STORE, C.GOOGLE_PLAY],
            "publisher": {"@type": "Organization", "name": "Safari Group"}}


def faq_ld(faq):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


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
        alt = "".join(f'<link rel="alternate" hreflang="{x}" href="{url(x, path)}">' for x in C.LANGS)
        alt += f'<link rel="alternate" hreflang="x-default" href="{C.BASE}/">'
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
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
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
    langs = "".join(f'<a href="/{x}/{path}" hreflang="{x}" lang="{x}"{" aria-current=\"true\"" if x == lang else ""}>{x.upper()}</a>' for x in C.LANGS)
    return f"""<header class="top"><div class="wrap">
<a class="brand" href="/{lang}/">{LOGO}<span>Intellect AI</span></a>
<nav class="nav" aria-label="{e(ui['menu_label'])}">
<a class="hide-s" href="/{lang}/#coaches">{e(ui['nav_coaches'])}</a>
<a href="/{lang}/prompts/">{e(ui['nav_prompts'])}</a>
<span class="langs" aria-label="{e(ui['lang_label'])}">{langs}</span>
<a class="get hide-s" href="{C.ZEHN}/{lang}/">{e(ui['nav_get'])}</a>
</nav></div></header>
<main id="main">"""


def footer(lang):
    ui = L[lang].UI
    co = L[lang].COACHES
    links = "".join(f'<li><a href="/{lang}/{s}/">{e(co[s]["name"])}</a></li>' for s, *_ in C.COACHES)
    return f"""</main>
<footer><div class="wrap">
<div><a class="brand" href="/{lang}/">{LOGO}Intellect AI</a><p style="margin-top:10px">{e(ui['footer_about'])}</p>
<p><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p></div>
<div><b>{e(ui['nav_coaches'])}</b><ul>{links}</ul></div>
<div><b>{e(ui['footer_links'])}</b><ul><li><a href="/{lang}/">{e(ui['home'])}</a></li><li><a href="/{lang}/prompts/">{e(ui['prompts_all'])}</a></li><li><a href="/{lang}/privacy/">{e(ui['privacy'])}</a></li><li><a href="{C.ZEHN}/{lang}/">Zehn</a></li></ul></div>
<div class="copy">{e(ui['footer_brand'])} · © 2026</div>
</div></footer>
<script>document.addEventListener("click",function(v){{var b=v.target.closest(".cp");if(!b)return;var t=b.parentNode.querySelector(".pt").textContent;navigator.clipboard.writeText(t).then(function(){{b.textContent=b.dataset.ok;b.classList.add("ok");setTimeout(function(){{b.textContent=b.dataset.l;b.classList.remove("ok")}},1600)}})}});</script>
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
        li = "".join(f'<li><p class="pt">{e(x)}</p><button class="cp" type="button" data-l="{e(ui["copy"])}" data-ok="{e(ui["copied"])}">{e(ui["copy"])}</button></li>' for x in c["prompts"][:3])
        groups += (f'<div class="pgroup"><h2>{badge(s)}<a href="/{lang}/{s}/" style="color:inherit;text-decoration:none">{e(c["name"])}</a></h2>'
                   f'<ol class="plist">{li}</ol><p style="margin-top:10px"><a href="/{lang}/{s}/#prompts">{e(p["see_all"])} →</a></p></div>')
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


def build_seo():
    pages = [""] + [s + "/" for s, *_ in C.COACHES] + ["prompts/", "privacy/"]
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
           f"<url><loc>{C.BASE}/</loc><lastmod>{MODIFIED}</lastmod></url>"]
    for p in pages:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{url(x, p)}"/>' for x in C.LANGS)
        alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{C.BASE}/"/>'
        for lang in C.LANGS:
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
    lines += ["", "## Other pages", f"- [All prompts]({url('en', 'prompts/')}): 108 free prompts, 12 per coach",
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
    build_root()
    build_404()
    build_seo()
    n = sum(len(fs) for _, _, fs in os.walk(DIST))
    print(f"built {n} files in dist/")
    for w in WARN:
        print("WARN", w)


if __name__ == "__main__":
    main()
