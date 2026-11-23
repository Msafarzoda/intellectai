# intellectai.app

Static site "Intellect AI by Zehn": free AI coaching guides (9 coaches × EN/RU/AR).

- Content: `content/en.py`, `content/ru.py`, `content/ar.py`; shared data in `content/common.py`
- Build: `python3 -I build.py` (writes `dist/`), `--og` re-renders the OG images (needs Google Chrome)
- Hosting: Cloudflare Pages, no build command, output directory `dist`
