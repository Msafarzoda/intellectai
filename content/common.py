"""Shared, language-independent data: coach order, app names, icons, tints, links."""

BASE = "https://intellectai.app"
LANGS = ["en", "ru", "ar"]
APP_STORE = "https://apps.apple.com/app/id6759160035"
GOOGLE_PLAY = "https://play.google.com/store/apps/details?id=com.audiobook.zehn"
ZEHN = "https://thezehnapp.com"
EMAIL = "contact@safarigrp.com"

# slug -> (English name used inside the app, icon key, tint)
COACHES = [
    ("business-mentor", "Business Mentor", "brief", "#FFE9C7"),
    ("money-coach", "Money Coach", "coin", "#D9F7E4"),
    ("productivity-coach", "Productivity Coach", "cal", "#DDEBFF"),
    ("mindfulness-guide", "Mindfulness Guide", "mind", "#E9E3FF"),
    ("psychologist", "Psychologist", "psy", "#FFE1E6"),
    ("negotiator", "Negotiator", "nego", "#FFF2C2"),
    ("language-tutor", "Language Tutor", "lang", "#D6F4F7"),
    ("leadership-mentor", "Leadership Mentor", "flag", "#F3E2D2"),
    ("science-explainer", "Science Explainer", "atom", "#E2F0D5"),
]
SENSITIVE = {"psychologist", "mindfulness-guide"}

# Thin outline icons in the style of the app's persona chips (drawn by hand, no logos)
ICONS = {
    "brief": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5h6v2M3 12h18M11 12v2h2v-2"/>',
    "coin": '<circle cx="12" cy="12" r="9"/><path d="M15 9.5c-.5-1-1.6-1.5-3-1.5-1.7 0-3 .8-3 2s1.3 1.7 3 2 3 .9 3 2.1-1.3 2-3 2c-1.4 0-2.6-.6-3-1.6M12 6v12"/>',
    "cal": '<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M8 3v4M16 3v4M4 10h16M9 15l2 2 4-4"/>',
    "mind": '<circle cx="12" cy="12" r="2.2"/><circle cx="12" cy="12" r="5.5"/><circle cx="12" cy="12" r="9" stroke-dasharray="2 2.4"/>',
    "psy": '<path d="M6 20v-5a6 6 0 1 1 12 0v5"/><path d="M9 20v-5a3 3 0 0 1 6 0v5"/>',
    "nego": '<path d="M12 4v16M8 20h8M4 8h16M4 8l-2.5 6h5zM20 8l-2.5 6h5z"/>',
    "lang": '<rect x="3" y="4" width="12" height="9" rx="2"/><path d="M6 13v3l3-3"/><rect x="10" y="10" width="11" height="8" rx="2"/><path d="M18 18v3l-3-3M13 14h5"/>',
    "flag": '<path d="M6 21V3M6 4h11l-2.5 4L17 12H6"/>',
    "atom": '<circle cx="12" cy="12" r="1.6"/><ellipse cx="12" cy="12" rx="9.5" ry="3.8"/><ellipse cx="12" cy="12" rx="9.5" ry="3.8" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="9.5" ry="3.8" transform="rotate(120 12 12)"/>',
}


def icon(key, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[key]}</svg>'
