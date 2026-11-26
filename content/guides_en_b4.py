"""Batch 4 (EN): Hindi + Urdu book summary app pages. Facts from each service's own site or store page, checked 26 Nov 2026."""

D = "26 Nov 2026"
S = dict(
    yebook=("yebook.in", "https://yebook.in/", D),
    saarika=("saarika.ai", "https://saarika.ai/", D),
    gigl=("GIGL on Google Play", "https://play.google.com/store/apps/details?hl=en_US&id=com.gigl.app", D),
    sobrief=("sobrief.com", "https://sobrief.com/", D),
    sobrief_gp=("SoBrief on Google Play", "https://play.google.com/store/apps/details?hl=en_US&id=com.sobrief.android", D),
    kuku=("kukufm.com", "https://kukufm.com/", D),
    kafka=("kafkareader.com", "https://kafkareader.com/", D),
    urdunya=("urdunya.com", "https://urdunya.com/", D),
    rekhta=("rekhta.org eBooks", "https://www.rekhta.org/ebooks", D),
    headway=("makeheadway.com FAQ", "https://makeheadway.com/faq", D),
    blinkist=("blinkist.com, What is Blinkist?", "https://www.blinkist.com/learn/what-is-blinkist", D),
    zehn_hi=("thezehnapp.com/hindi", "https://thezehnapp.com/hindi/", D),
    zehn_ur=("thezehnapp.com/urdu", "https://thezehnapp.com/urdu/", D),
)

DISCLOSE = "Disclosure: Intellect AI is made by the team behind Zehn, one of the apps below. We list apps alphabetically, give no scores and take each app's facts from its own website or store page, so you can judge for yourself."

HOW = ("How we compared them", [
    "On 26 November 2026 we read each service's own website or official store listing and used only what it says about itself: languages, library size, summary length, format and free options. We give no scores and no ranking, because the right choice depends on what you read and how. If a service does not state something, we do not guess it.",
    "We make Zehn, so its strengths and limits are listed as plainly as everyone else's. If a fact here is out of date or you know an app we missed, write to contact@safarigrp.com and we will check it.",
])

GUIDES = {
"best-hindi-book-summary-apps": dict(
    cat="summary-apps", date="2026-11-26", date_h="26 November 2026",
    title="Best Hindi Book Summary Apps 2026: Honest Comparison",
    desc="Hindi book summary apps compared: Yebook, Saarika AI, GIGL, SoBrief and Zehn, plus Hindi audiobook apps. Length, free access and AI, from their sites.",
    h1="Best Hindi book summary apps in 2026: an honest comparison",
    lead="If you want book summaries in Hindi, most big international apps will not help: Blinkist and Headway do not list Hindi among their summary languages. A handful of apps do, and they differ a lot in length, library size and whether there is an AI chat. Here is how they compare, using only what each says about itself.",
    tldr=["Hindi summaries exist in Yebook, Saarika AI, GIGL, SoBrief and Zehn; Blinkist and Headway do not list Hindi.", "Short audio only: Saarika AI (about 10 minutes) and Yebook. Many languages: SoBrief (40+).", "Hindi plus an AI chat in every book, and Urdu in the same app: Zehn."],
    sections=[
        ("Which apps have book summaries in Hindi?", [
            "Searches such as “hindi books”, “book summary in hindi” and “hindi audiobook app” bring up three different things: apps that summarise books, apps that read full audiobooks aloud, and libraries of full books. This page is about the first kind, with the others noted where they matter. The apps below state on their own sites that they offer Hindi summaries or audio.",
            DISCLOSE,
        ]),
        ("Hindi book summary apps compared", [
            ("table", ["App", "Hindi content (their words)", "Length and format", "Free access"], [
                ["GIGL", "Hindi and English book summaries, e-books and audiobooks", "Audio, e-book and video summaries", "Described as a free app; contains ads and in-app purchases"],
                ["Saarika AI", "Hindi among 9+ Indian languages", "About 10-minute AI-narrated audio, with an AI chat about each book", "Not stated on its site"],
                ["SoBrief", "Hindi among 40+ languages; 26,000+ summaries", "About 10 minutes; audio, PDF and EPUB", "Free users get 3 summaries a month"],
                ["Yebook", "Summaries in Hindi; 1,200+ Premium summaries", "Audio, about 14 minutes for the examples shown", "Free books, first chapter without an account"],
                ["Zehn", "Hindi library in the app (we publish no title count)", "15–20 minutes, audio with synced text, Ask AI on every book", "1 book a day, no AI"],
            ]),
            "Kuku FM, a large Indian audio platform, offers Hindi audiobooks and stories, including licensed titles such as Penguin Random House India books, but it is an audiobook and storytelling service rather than a summary app. Kafka offers free public-domain classics in Hindi and Urdu, many as audio. Blinkist (English, German, Spanish and Portuguese) and Headway (eleven languages, none of them Hindi) do not list Hindi.",
        ]),
        ("Which Hindi app is best for what you need?", [
            ("ul", ["**Quick audio ideas in Hindi:** Saarika AI and Yebook focus on short audio summaries.", "**One app for many languages:** SoBrief lists more than 40 languages, including Hindi and Urdu.", "**Free to try without paying:** GIGL describes itself as a free app with ads, and Yebook has free books.", "**Ask questions about the book, in Hindi, and read Urdu or English in the same app:** Zehn, with Ask AI on every book.", "**Full audiobooks and stories, not summaries:** Kuku FM or Kafka."]),
        ]),
        ("Summary or audiobook: what is the difference?", [
            "A summary gives the main ideas of a nonfiction book in 10–20 minutes. An audiobook is the whole book read aloud, usually many hours. If you searched “hindi audiobook app” because you want the full text of a novel or a classic, choose an audiobook service. If you want the key ideas of a business or self-help book before a commute ends, choose a summary app.",
        ]),
        HOW,
        ("Zehn in Hindi: strengths and limits", [
            "We make Zehn, so here is what it does well and where another app may suit you better.",
            ("table", ["Strengths", "Limits"], [
                ["Hindi summaries as audio with synced text; the same app also has Urdu, English, Arabic and Russian", "We publish no count of Hindi titles, so check the Hindi library for your topics before subscribing"],
                ["Ask AI on every book, and an AI Chat tab with nine coaches", "AI features are on the paid plan only; no podcast summaries, quizzes or video"],
                ["Free plan: 1 book a day. Pro is $9.99 a month, or $36 a year with a 7-day free trial", "Mobile apps only (iPhone, iPad, Android); a young app with few reviews so far"],
            ]),
            "Read more in our guide to the [Zehn Ask AI feature](/en/zehn/), or open the Hindi page of Zehn directly at thezehnapp.com/hindi.",
        ]),
        ("Sources", [
            ("sources", [S["yebook"], S["saarika"], S["gigl"], S["sobrief"], S["kuku"], S["kafka"], S["headway"], S["blinkist"], S["zehn_hi"]]),
            "Apps change their libraries and prices often. If a fact looks out of date, write to contact@safarigrp.com.",
        ]),
    ],
    faq=[
        ("Is there a book summary app in Hindi?",
         "Yes. Yebook, Saarika AI, GIGL, SoBrief and Zehn each say on their own sites that they offer Hindi summaries or audio. Blinkist and Headway do not list Hindi among their summary languages. The apps differ in length, library size, free access and whether they include an AI chat."),
        ("Which Hindi audiobook app is best?",
         "That depends on whether you want full audiobooks or summaries. Kuku FM has Hindi audiobooks and stories, and Kafka has free classics in Hindi and Urdu. For short audio summaries of nonfiction, look at Yebook, Saarika AI, SoBrief or Zehn. We do not rank them; use their free options to test."),
        ("Are there free Hindi book summaries?",
         "Several services have a free option. Yebook offers free books and the first chapter without an account, SoBrief gives free users three summaries a month, GIGL describes itself as free with ads, and Zehn has one free book a day without the AI features. Terms change, so check each app."),
        ("Can I get Hindi book summaries with an AI chat?",
         "Saarika AI says you can chat with its AI about any book, and Zehn has Ask AI on every book plus an AI Chat tab with nine coaches. In Zehn, the AI features are part of the paid plan. Other services in this comparison do not mention a book chat on their sites."),
    ],
    related=["is-there-a-book-summary-app-in-hindi", "best-urdu-book-summary-apps", "best-book-summary-apps"],
),
"best-urdu-book-summary-apps": dict(
    cat="summary-apps", date="2026-11-26", date_h="26 November 2026",
    title="Best Urdu Book Summary Apps 2026: Honest Comparison",
    desc="Urdu book summary and audio book apps compared: Urdunya, SoBrief and Zehn, plus Rekhta and Kafka for full books. Length and free access, from their sites.",
    h1="Best Urdu book summary apps in 2026: an honest comparison",
    lead="Apps for Urdu readers are few. Blinkist and Headway do not list Urdu, so people searching for “urdu books”, “urdu audio books app” or “book summary in Urdu” usually find a mix of summary apps, audiobook apps and digital libraries. This page separates them and compares them using only what each service says about itself.",
    tldr=["Urdu summaries: Urdunya (Urdu books as short audio), SoBrief (40+ languages) and Zehn (Urdu library plus Ask AI).", "Full Urdu books and audio, not summaries: Rekhta and Kafka.", "Blinkist and Headway do not list Urdu."],
    sections=[
        ("Which apps have book summaries in Urdu?", [
            "Three services say on their own sites that they offer Urdu summaries. Urdunya summarises Urdu's best books as short audio, and its examples are Urdu literature and biographies. SoBrief offers summaries of 26,000+ books, mostly translated, in 40+ languages that include Urdu. Zehn has an Urdu library of nonfiction book summaries with synced text and an AI chat on every book.",
            DISCLOSE,
        ]),
        ("Urdu book apps compared", [
            ("table", ["App", "Urdu content (their words)", "Length and format", "Free access"], [
                ["Kafka", "Free public-domain Hindi and Urdu editions; 1,129 audiobooks in Hindi, Urdu and English", "Full books and audiobooks, not summaries", "Free, no ads (per its site)"],
                ["Rekhta eBooks", "200,000+ Urdu books and 75,000 periodicals in its digital library", "Full e-books", "Not stated on the page we read"],
                ["SoBrief", "Urdu among 40+ languages", "About 10 minutes; audio, PDF, EPUB", "Free users get 3 summaries a month"],
                ["Urdunya", "Urdu books as short audio summaries (for example an 18-minute listen)", "Audio", "Free on iPhone and Android"],
                ["Zehn", "Urdu library in the app (we publish no title count)", "15–20 minutes, audio with synced text, Ask AI on every book", "1 book a day, no AI"],
            ]),
            "Blinkist lists English, German, Spanish and Portuguese, and Headway lists eleven languages without Urdu, so neither is an option for Urdu summaries.",
        ]),
        ("Which Urdu app is best for what you need?", [
            ("ul", ["**Summaries of Urdu literature and biography in audio:** Urdunya.", "**Summaries of nonfiction (business, habits, money) in Urdu, plus Hindi and English in one app:** Zehn.", "**Many languages in one place:** SoBrief.", "**Whole Urdu books, poetry and classics:** Rekhta (e-books) or Kafka (free editions and audiobooks)."]),
        ]),
        ("Urdu audio books or summaries?", [
            "If you search “urdu audio books app”, you may want the full book narrated, which is many hours of listening. A summary is a 10–20 minute version of the main ideas. Summaries help you decide what to read and refresh books you have already read; they do not replace the writing of a poet or novelist, so for literature choose a library or audiobook service.",
        ]),
        HOW,
        ("Zehn in Urdu: strengths and limits", [
            ("table", ["Strengths", "Limits"], [
                ["Urdu summaries as audio with synced text; the same app has Hindi, English, Arabic and Russian", "We publish no count of Urdu titles, so check the Urdu library for your topics first"],
                ["Ask AI on every book, and an AI Chat tab with nine coaches", "AI features are on the paid plan only; no podcast summaries or quizzes"],
                ["Free plan: 1 book a day. Pro is $9.99 a month, or $36 a year with a 7-day free trial", "Mobile apps only; a young app with few reviews so far"],
            ]),
            "The Urdu page of Zehn is at thezehnapp.com/urdu.",
        ]),
        ("Sources", [
            ("sources", [S["urdunya"], S["sobrief"], S["sobrief_gp"], S["rekhta"], S["kafka"], S["headway"], S["blinkist"], S["zehn_ur"]]),
            "Apps change libraries and prices often. If a fact looks out of date, write to contact@safarigrp.com.",
        ]),
    ],
    faq=[
        ("Is there a book summary app in Urdu?",
         "Yes. Urdunya, SoBrief and Zehn each say on their own sites that they offer Urdu summaries or audio. Blinkist and Headway do not list Urdu. They differ in what they summarise: Urdunya focuses on Urdu literature, while SoBrief and Zehn cover many nonfiction topics."),
        ("Which Urdu audio books app should I use?",
         "For full books, Kafka offers free Hindi and Urdu audiobooks, and Rekhta has a very large Urdu e-book library. For short audio summaries, look at Urdunya, SoBrief or Zehn. We do not rank them, so try each one's free option with books you already know."),
        ("Are Urdu book summaries free?",
         "Some are. Urdunya says it is free on iPhone and Android, SoBrief gives free users three summaries a month, and Zehn has one free book a day without AI. Kafka and its Urdu audiobooks are free according to its site. Terms change, so check the current offer."),
        ("Does Zehn have Urdu books?",
         "Yes, Zehn has an Urdu library with audio and synced text, and Ask AI on every book. We do not publish a count of Urdu titles, so check the app's Urdu library for your topics. The free plan gives one book a day without AI."),
    ],
    related=["is-there-a-book-summary-app-in-urdu", "best-hindi-book-summary-apps", "best-book-summary-apps"],
),
"is-there-a-book-summary-app-in-hindi": dict(
    cat="quick-answers", kind="qa", date="2026-11-26", date_h="26 November 2026",
    title="Is There a Book Summary App in Hindi? Quick Answer",
    desc="Yes: Yebook, Saarika AI, GIGL, SoBrief and Zehn offer Hindi book summaries. Which fit audio, free use or an AI chat, in two minutes.",
    h1="Is there a book summary app in Hindi?",
    answer="Yes. Yebook, Saarika AI, GIGL, SoBrief and Zehn each say on their own sites that they offer Hindi book summaries or audio. Blinkist and Headway do not list Hindi. Yebook and Saarika AI are mainly short audio, SoBrief covers 40+ languages, and Zehn adds an AI chat to every book.",
    lead="The short version, with links to the details.",
    tldr=["Five apps with Hindi: Yebook, Saarika AI, GIGL, SoBrief, Zehn.", "Blinkist and Headway: no Hindi.", "Full audiobooks instead: Kuku FM or Kafka."],
    sections=[
        ("What fits you?", [
            ("table", ["If you want…", "Try"], [
                ["Short Hindi audio summaries", "Yebook or Saarika AI"],
                ["Hindi, Urdu and many other languages", "SoBrief"],
                ["Hindi plus an AI chat on every book", "Zehn"],
                ["Full Hindi audiobooks and stories", "Kuku FM"],
            ]),
            "We make Zehn. Facts about other apps come from their own sites, checked on 26 November 2026; sources are in the [full comparison](/en/guides/best-hindi-book-summary-apps/).",
        ]),
        ("What about Blinkist and Headway?", [
            "Blinkist lists English, German, Spanish and Portuguese. Headway lists eleven languages and Hindi is not among them. They are good if you read English, but for Hindi you need one of the apps above.",
        ]),
        ("Summary or full audiobook?", [
            "If you searched for a “hindi audiobook app”, decide first whether you want the whole book or its main ideas. A full audiobook is the complete text read aloud and usually takes many hours, which suits novels, stories and classics. A summary takes ten to twenty minutes and suits business, habits, money and psychology books, where the ideas matter more than the prose. Many readers use a summary to decide which books deserve the full listen.",
        ]),
        ("Are there free options?", [
            "Yebook has free books, SoBrief gives free users three summaries a month, GIGL describes itself as a free app with ads, and Zehn gives one book a day without AI. Check each app's current terms before relying on them.",
        ]),
    ],
    faq=[
        ("Is there a Hindi audiobook app with book summaries?",
         "Yes: Yebook and Saarika AI focus on short audio summaries in Hindi, and Zehn offers audio with synced text. Kuku FM and Kafka have Hindi audiobooks, which are full books rather than summaries. Choose by whether you want the key ideas or the whole book."),
        ("How long is a book summary in Hindi?",
         "Saarika AI says its summaries are designed to be about ten minutes, and the Yebook examples we saw were around fourteen minutes. SoBrief says about ten minutes, and Zehn summaries take fifteen to twenty minutes in audio with synced text."),
    ],
    related=["best-hindi-book-summary-apps", "is-there-a-book-summary-app-in-urdu", "can-ai-explain-a-book"],
),
"is-there-a-book-summary-app-in-urdu": dict(
    cat="quick-answers", kind="qa", date="2026-11-26", date_h="26 November 2026",
    title="Is There a Book Summary App in Urdu? Quick Answer",
    desc="Yes: Urdunya, SoBrief and Zehn offer Urdu book summaries; Rekhta and Kafka have full Urdu books. Which fits you, in two minutes.",
    h1="Is there a book summary app in Urdu?",
    answer="Yes. Urdunya, SoBrief and Zehn each say on their own sites that they offer Urdu book summaries or audio. Urdunya focuses on Urdu literature as short audio, SoBrief covers 40+ languages, and Zehn has an Urdu library with an AI chat on every book. Blinkist and Headway do not list Urdu.",
    lead="The short version, with links to the details.",
    tldr=["Three apps with Urdu summaries: Urdunya, SoBrief, Zehn.", "Full Urdu books: Rekhta and Kafka.", "Blinkist and Headway: no Urdu."],
    sections=[
        ("What fits you?", [
            ("table", ["If you want…", "Try"], [
                ["Urdu literature and biographies as short audio", "Urdunya"],
                ["Urdu nonfiction summaries, plus Hindi and English in one app", "Zehn"],
                ["Many languages in one place", "SoBrief"],
                ["Whole Urdu books and audiobooks", "Rekhta or Kafka"],
            ]),
            "We make Zehn. Facts about other apps come from their own sites, checked on 26 November 2026; sources are in the [full comparison](/en/guides/best-urdu-book-summary-apps/).",
        ]),
        ("What about Blinkist and Headway?", [
            "Blinkist lists English, German, Spanish and Portuguese, and Headway lists eleven languages without Urdu. For Urdu you need one of the apps above.",
        ]),
        ("Summary or full audiobook?", [
            "If you searched for an “urdu audio books app”, decide first whether you want the whole book or its main ideas. A full audiobook is the complete text read aloud and usually takes many hours, which suits novels, poetry and classics. A summary takes ten to twenty minutes and suits nonfiction, where the ideas matter more than the prose. Many readers use a summary to decide which books deserve the full listen.",
        ]),
        ("Are there free options?", [
            "Urdunya says it is free on iPhone and Android, SoBrief gives free users three summaries a month, and Zehn gives one free book a day without AI. Terms change, so check the current offer in each app.",
        ]),
    ],
    faq=[
        ("Which app has Urdu audio books?",
         "For full audiobooks, Kafka lists free Hindi and Urdu audiobooks. For short audio summaries, Urdunya summarises Urdu books, and SoBrief and Zehn offer Urdu audio summaries. Summaries give the main ideas in minutes; audiobooks give the whole text over hours."),
        ("Can I ask questions about a book in Urdu?",
         "Zehn has Ask AI on every book, a chat that answers from that book, and it is part of the paid plan. Urdunya, SoBrief and Rekhta do not mention a book chat on the pages we read. Check the app for the languages Ask AI supports."),
    ],
    related=["best-urdu-book-summary-apps", "is-there-a-book-summary-app-in-hindi", "can-ai-explain-a-book"],
),
}
