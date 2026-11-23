"""Batch 1 (EN): honest book-summary-app roundups + question pages.
Competitor facts: each app's own site or official store listing, checked 23 Nov 2026 (sources listed on each page).
Rules: alphabetical order, no rankings or scores, Zehn disclosed as ours, real limits for Zehn too."""

UI = dict(sources_h="Sources (checked 23 November 2026)", answer_h="Short answer")

CATS = {
    "summary-apps": ("Book summary apps", "Honest, criteria-based comparisons of book summary apps, including ours."),
    "quick-answers": ("Quick answers", "Short, direct answers to common questions about reading apps and AI."),
}

DISCLOSE = "Disclosure: Intellect AI is made by the team behind Zehn, one of the apps below. We list apps alphabetically, give no scores and state each app's facts from its own website or store page, so you can judge for yourself."

S_BLINKIST = ("blinkist.com", "https://www.blinkist.com/", "23 Nov 2026")
S_HEADWAY = ("makeheadway.com", "https://makeheadway.com/", "23 Nov 2026")
S_SHORTFORM = ("shortform.com", "https://www.shortform.com/", "23 Nov 2026")
S_12MIN = ("12min.com", "https://12min.com/", "23 Nov 2026")
S_STORYSHOTS = ("getstoryshots.com", "https://www.getstoryshots.com/", "23 Nov 2026")
S_GETABSTRACT = ("getabstract.com", "https://www.getabstract.com/en/", "23 Nov 2026")
S_WAJEEZ = ("wajeez.com and its Google Play listing", "https://wajeez.com/about-us", "23 Nov 2026")
S_DURAR = ("Durar on Google Play", "https://play.google.com/store/apps/details?id=com.durar.books", "23 Nov 2026")
S_EJAZ = ("getejaz.com", "https://getejaz.com/", "23 Nov 2026")
S_SMART = ("smartreading.ru", "https://smartreading.ru/", "23 Nov 2026")
S_SUMLIB = ("summarylib.ru", "https://summarylib.ru/", "23 Nov 2026")
S_MYBOOK = ("mybook.ru", "https://mybook.ru/payments/", "23 Nov 2026")
S_ZEHN = ("thezehnapp.com", "https://thezehnapp.com/en/", "23 Nov 2026")

CRITERIA = ("ol", [
    "**Languages:** can you read and listen in your own language, with summaries written for it rather than machine-translated?",
    "**Library size and focus:** how many titles, and are they the kind of books you actually want (business, psychology, history, fiction)?",
    "**Length and depth:** a 5-minute overview, a 15-minute summary or a 45-minute deep guide are different products.",
    "**Format:** audio, text, or both; offline listening for commutes and flights.",
    "**AI and extras:** can you ask questions about a book, test yourself, discuss with others?",
    "**Free option and price:** is there a free tier or trial, and does the price fit how often you will really use it?",
])

GUIDES = {
"best-book-summary-apps": dict(
    cat="summary-apps",
    title="Best Book Summary Apps in 2026: An Honest Comparison",
    desc="Book summary apps compared on languages, library size, length, format, AI and free options: Blinkist, Headway, Shortform, 12min, StoryShots, Zehn and more.",
    h1="The best book summary apps in 2026: an honest comparison",
    lead="There is no single best book summary app, only the best one for your language, your time and how deep you want to go. This page compares the main apps on six criteria, using facts each app publishes about itself, and says plainly where each one is the better choice.",
    tldr=["Want depth and commentary? Shortform's long guides go furthest.", "Want quick English summaries with a big library? Blinkist, Headway and 12min.", "Read in Arabic, Russian, Hindi or Urdu, or want AI on every book? That is where Zehn is strongest."],
    sections=[
        ("How should you choose a book summary app?", [
            "Choose by language first, then by depth. An app with 12,000 titles is useless if none are in the language you think in, and a 5-minute overview won't satisfy you if you want the author's arguments. Then check format, extras like AI or quizzes, and whether a free option lets you test it.",
            DISCLOSE,
            CRITERIA,
        ]),
        ("The apps at a glance", [
            ("table", ["App", "Summary languages", "Library (as stated)", "Length and format", "Free option"], [
                ["Blinkist", "English, German, Spanish, Portuguese", "9,000+ book and podcast summaries", "About 15 min, audio and text", "Trial; after it, 1 pre-selected book a day"],
                ["Headway", "11 languages incl. English, Spanish, French, German", "1,700+ summaries", "About 15 min, audio and text", "Trial"],
                ["12min", "English, Spanish, Portuguese", "3,500+ titles", "About 12 min, audio and text", "Start without a card"],
                ["Shortform", "English, Spanish, German, Brazilian Portuguese", "12,000+ books", "Long guides with commentary, audio, PDF", "Free trial"],
                ["StoryShots", "English (per its site)", "Large library; AI can add missing books", "Free 5-min versions; 15-min and 45-min for Premium", "A few books a day free"],
                ["Zehn", "English, Arabic, Russian, Hindi, Urdu, Tajik", "10,000+ books", "15–20 min, audio with synced text", "1 book a day free, no AI"],
            ]),
            "getAbstract (15-minute summaries, 8 site languages) now focuses on companies and AI tools rather than individual readers, so it isn't in the table.",
        ]),
        ("Which app is best for depth?", [
            "Shortform is built for depth: its guides add commentary and connections to other books, with exercises and community discussions, and they are longer than a typical 15-minute summary. If you want to understand an author's argument rather than collect key points, it is the strongest of the group, at a higher price.",
        ]),
        ("Which app is best for quick English summaries?", [
            "Blinkist, Headway and 12min all do short English summaries well. Blinkist has the largest library of the three and adds podcast summaries; Headway leans on habit features like streaks and spaced repetition; 12min keeps things to about 12 minutes and adds a quiz at the end. Try each free option and keep the one you open daily.",
        ]),
        ("Which app is best if English isn't your first language?", [
            "Most big apps write mainly for English readers, with a few European languages. Zehn has libraries in Arabic, Russian, Hindi, Urdu and Tajik as well as English, with Arabic narrated in Modern Standard Arabic. Arabic-first apps like Wajeez and Russian-first services like Smart Reading are also strong; see our [best Arabic](/en/guides/best-arabic-book-summary-apps/) and [best Russian](/en/guides/best-russian-book-summary-apps/) lists.",
        ]),
        ("Which apps use AI, and how?", [
            ("ul", ["**Blinkist AI** (Pro plan) summarises your own videos, podcasts, documents and articles.", "**StoryShots AI** writes a summary of a book that isn't in its library yet.", "**Zehn** has Ask AI on every book (a chat that answers from that book) plus an AI Chat tab with nine coaching personas and a choice of Claude, Gemini, DeepSeek or Grok.", "**Shortform, Headway, 12min:** focus on human-written summaries; their sites don't list a per-book AI chat."]),
        ]),
        ("Zehn: strengths and limits", [
            "We make Zehn, so here is what it does well and where another app may suit you better.",
            ("table", ["Strengths", "Limits"], [
                ["Libraries in six languages, not just English", "Mobile apps only (iPhone, iPad, Android); no web reader"],
                ["Ask AI on every book, AI Chat with nine coaches", "AI features need a paid plan"],
                ["Audio with synced text; offline listening on paid plans", "No podcast summaries"],
                ["Free plan: 1 book a day; Pro from $9.99/month or $36/year with a 7-day trial", "A newer app, so fewer reviews to judge it by"],
            ]),
        ]),
        ("Sources", [
            ("sources", [S_BLINKIST, S_HEADWAY, S_12MIN, S_SHORTFORM, S_STORYSHOTS, S_GETABSTRACT, S_ZEHN]),
            "Apps change their libraries and features often. If you spot something out of date, write to contact@safarigrp.com and we will correct it.",
        ]),
    ],
    faq=[
        ("Are book summary apps worth it?",
         "They are worth it if you use them to choose what to read, to revisit books you finished, or to get main ideas from books you only need for work. They are not a replacement for reading the books you care about most. Use the free option for two weeks and check how often you actually open the app."),
        ("Which book summary app has the most books?",
         "By the numbers each app publishes, Shortform states 12,000+ books, Zehn 10,000+ books and Blinkist 9,000+ book and podcast summaries, followed by 12min with 3,500+ titles and Headway with 1,700+. Counts change often and are counted differently, so compare the topics you need rather than the total alone."),
        ("Is there a free book summary app?",
         "Several apps have free options. Zehn's free plan includes one book summary a day, StoryShots offers free five-minute versions of a few books a day, and Blinkist leaves one pre-selected book a day after a trial ends. Fully unlimited access usually needs a paid plan or trial on every app."),
        ("Which book summary app is best for Arabic or Russian?",
         "For Arabic, the main options are Arabic-first apps like Wajeez, bilingual Arabic-English apps like Durar and Ejaz, and Zehn, which has an Arabic library plus AI. For Russian, Smart Reading and SummaryLib are Russian services, and Zehn has a Russian library. Our language-specific lists compare them in detail."),
    ],
    related=["book-summary-apps-for-non-english-speakers", "best-arabic-book-summary-apps", "best-russian-book-summary-apps"],
),
"best-arabic-book-summary-apps": dict(
    cat="summary-apps",
    title="Best Arabic Book Summary Apps (2026): Wajeez, Durar & More",
    desc="Book summary apps in Arabic compared: Wajeez, Durar, Ejaz and Zehn. Library, audio, English option, AI and free plans, from each app's own pages.",
    h1="Book summary apps in Arabic: an honest comparison",
    lead="If you want to read or listen to book summaries in Arabic, the big English-first apps don't help much: none of Blinkist, Headway, Shortform or 12min lists Arabic. Here are the apps that do, compared on what each says about itself.",
    tldr=["Biggest Arabic audio library: Wajeez, with summaries, podcasts, novels and full audiobooks.", "Arabic and English side by side: Durar and Ejaz.", "Arabic plus an AI chat on every book: Zehn."],
    sections=[
        ("Is there a book summary app in Arabic?", [
            "Yes, several. Wajeez is the largest Arabic audio library, with thousands of book summaries plus podcasts and novels. Durar and Ejaz offer summaries in both Arabic and English. Zehn has an Arabic library narrated in Modern Standard Arabic, with an AI chat on every book. Big English-first apps don't list Arabic.",
            DISCLOSE,
        ]),
        ("Arabic book summary apps compared", [
            ("table", ["App", "Languages", "What's inside (as stated)", "Length and format", "Free option"], [
                ["Durar", "Arabic and English, audio in both", "18 subjects of nonfiction", "About 15 min, audio and text", "1 free summary a day; 14-day trial on monthly"],
                ["Ejaz (HBKU Press)", "Arabic and English", "Hundreds of summaries, fiction and nonfiction", "Text and audio", "Free start"],
                ["Wajeez", "Arabic", "12,000 titles incl. 3,000+ book summaries, podcasts, novels, full audiobooks", "15-min summaries, audio and text", "Subscription"],
                ["Zehn", "Arabic, English, Russian, Hindi, Urdu, Tajik", "10,000+ books across its libraries", "15–20 min, audio with synced text", "1 book a day free, no AI"],
            ]),
        ]),
        ("Which one should you pick?", [
            ("ul", ["**You want the most Arabic audio, including novels and podcasts:** Wajeez.", "**You are learning English, or switch between Arabic and English:** Durar or Ejaz, which offer both languages for the same summary.", "**You want to ask questions about a book and get answers from it, or talk to AI coaches:** Zehn.", "**You read mainly classic and literary works:** Ejaz covers fiction as well as nonfiction."]),
        ]),
        ("What to check before you subscribe", [
            ("ol", ["Search the app for three books you actually want; library sizes mean little if your topics are missing.", "Listen to one summary: is the narration Modern Standard Arabic or a dialect, and do you like the voice?", "Check offline listening if you commute underground or travel.", "Check whether the price shown in your country differs; several apps use regional pricing."]),
        ]),
        ("Narration, dialects and reading direction", [
            "Most Arabic summary apps narrate in Modern Standard Arabic, which every Arabic speaker understands, rather than a regional dialect. That makes them usable from Morocco to Oman, but the voice, pace and style still differ a lot between apps, so listen to a full sample before paying. Text should display right to left with proper Arabic fonts; a quick look at one summary page tells you whether an app was built for Arabic or translated into it later.",
        ]),
        ("How we compared these apps", [
            "We read each app's own website or official store listing on 23 November 2026 and copied only what the app states about itself: languages, library size, summary length, format and free options. We did not score or rank the apps, because the right choice depends on what you read and how. Where an app doesn't state something, we leave it out rather than guess.",
            "We make Zehn, which is why its strengths and limits are listed separately and in the same plain terms as the others. If you know of an app we missed or a fact that has changed, tell us and we'll check it.",
        ]),
        ("Zehn in Arabic: strengths and limits", [
            ("table", ["Strengths", "Limits"], [
                ["Arabic library narrated in Modern Standard Arabic", "Fewer Arabic-only titles than Wajeez; many books are translated nonfiction"],
                ["Ask AI on every book answers in Arabic", "AI features need a paid plan ($9.99/month or $36/year)"],
                ["Book Club tab to discuss books with other readers", "No podcast summaries or full audiobooks"],
            ]),
            "More on the app on our [What is Zehn?](/en/zehn/) page.",
        ]),
        ("Sources", [
            ("sources", [S_WAJEEZ, S_DURAR, S_EJAZ, S_ZEHN]),
        ]),
    ],
    faq=[
        ("What is the best app for Arabic book summaries?",
         "It depends on what you need. Wajeez has the largest Arabic audio library, including podcasts and novels. Durar and Ejaz suit readers who want Arabic and English side by side. Zehn suits readers who want an AI chat on every book and libraries in several languages. Try the free option of two apps before choosing."),
        ("Are there free Arabic book summaries?",
         "Yes. Durar offers one free summary every day, and Zehn's free plan includes one book summary a day without AI features. Other apps offer trials. Full access to a whole library usually needs a subscription, and prices may differ by country because several apps use regional pricing."),
        ("Are Arabic book summaries in Modern Standard Arabic?",
         "Most Arabic summary apps use Modern Standard Arabic (fusha) for narration, because it works across all Arabic-speaking countries. Zehn's Arabic summaries are narrated in Modern Standard Arabic. Listen to a sample in each app before subscribing, since voices and styles differ between apps."),
        ("Can I learn English with an Arabic book summary app?",
         "Bilingual apps help. Durar and Ejaz offer the same summary in Arabic and English, so you can read in one language and listen in the other. Zehn has separate English and Arabic libraries with synced text, plus a Language Tutor coach in its AI Chat for practising the words you meet."),
    ],
    related=["best-book-summary-apps", "is-there-a-book-summary-app-in-arabic", "book-summary-apps-for-non-english-speakers"],
),
"best-russian-book-summary-apps": dict(
    cat="summary-apps",
    title="Best Russian Book Summary Apps (2026): Honest Comparison",
    desc="Book summary apps in Russian compared: Smart Reading, SummaryLib, Zehn, and MyBook for full books. Library, audio, trials and AI, from their own pages.",
    h1="Book summary apps in Russian: an honest comparison",
    lead="Russian readers have fewer summary apps to choose from than English readers, and most big international apps don't offer Russian at all. Here are the services that do, plus one full-book library worth knowing about.",
    tldr=["Largest Russian-only summary library: Smart Reading (1,090+ summaries).", "Smaller, focused library: SummaryLib (400+).", "Russian plus AI on every book and other languages: Zehn."],
    sections=[
        ("Which apps summarise books in Russian?", [
            "Smart Reading is the best-known Russian summary service, with over a thousand summaries in text, audio and infographics. SummaryLib is a smaller Russian library. Zehn has a Russian library with an AI chat on every book. For whole books rather than summaries, MyBook is a large Russian subscription library.",
            DISCLOSE,
        ]),
        ("Russian book summary apps compared", [
            ("table", ["Service", "Type", "Library (as stated)", "Length and format", "Free option"], [
                ["MyBook", "Full e-books and audiobooks", "1,137,000 books, 566,000 audiobooks", "Full books", "14 days free on Premium"],
                ["Smart Reading", "Summaries", "1,090+ summaries", "About 20 min, text, audio, infographics, tests", "7 days free"],
                ["SummaryLib", "Summaries", "400+ books", "About 20 min, text and audio", "7 days free on 6- and 12-month plans"],
                ["Zehn", "Summaries + AI", "10,000+ books across its libraries", "15–20 min, audio with synced text", "1 book a day free, no AI"],
            ]),
        ]),
        ("Which one should you pick?", [
            ("ul", ["**You want depth, tests and infographics in Russian:** Smart Reading, whose summaries keep examples and add commentary.", "**You want to read whole books, not summaries:** MyBook.", "**You want to ask questions about a book, use AI coaches, or also read in English, Arabic, Hindi or Urdu:** Zehn.", "**You want a small curated library at a lower commitment:** SummaryLib."]),
        ]),
        ("What to check before you subscribe", [
            ("ol", ["Search for three books you actually want.", "Check how long a summary is: 15 minutes and 20 pages of text are different experiences.", "Check payment options in your country; some services only accept certain cards.", "Check offline mode for travel and the metro."]),
        ]),
        ("Summaries or full books?", [
            "A summary gives you the main ideas of a nonfiction book in fifteen to twenty minutes; a full book gives you the author's evidence, stories and nuance over several hours. Many Russian readers combine both: a summary service to choose what to read and to revisit books they finished, and a full-book library such as MyBook for the titles that deserve the time. If you only want novels, a full-book or audiobook service is the better fit, since summaries mostly cover nonfiction.",
        ]),
        ("How we compared these apps", [
            "We read each app's own website or official store listing on 23 November 2026 and copied only what the app states about itself: languages, library size, summary length, format and free options. We did not score or rank the apps, because the right choice depends on what you read and how. Where an app doesn't state something, we leave it out rather than guess.",
            "We make Zehn, which is why its strengths and limits are listed separately and in the same plain terms as the others. If you know of an app we missed or a fact that has changed, tell us and we'll check it.",
        ]),
        ("Zehn in Russian: strengths and limits", [
            ("table", ["Strengths", "Limits"], [
                ["Ask AI on every book, answers in Russian", "AI features need a paid plan ($9.99/month or $36/year)"],
                ["AI Chat with nine coaches, e.g. a Language Tutor", "No infographics or built-in tests like Smart Reading"],
                ["Same app also has English, Arabic, Hindi and Urdu libraries", "Mobile apps only; no web reader"],
            ]),
        ]),
        ("Sources", [
            ("sources", [S_SMART, S_SUMLIB, S_MYBOOK, S_ZEHN]),
        ]),
    ],
    faq=[
        ("What is the best app for book summaries in Russian?",
         "Smart Reading has the largest Russian-only summary library, with text, audio, infographics and tests. Zehn suits readers who want an AI chat on every book or several languages in one app. SummaryLib is a smaller library. If you want full books rather than summaries, MyBook is a large Russian subscription library."),
        ("Are there free book summaries in Russian?",
         "Most Russian services offer a trial: Smart Reading gives seven days free, SummaryLib a seven-day trial on longer plans, and MyBook fourteen days on Premium. Zehn's free plan includes one book summary a day without AI. Check current terms in each app, since offers change."),
        ("How long are Russian book summaries?",
         "Smart Reading and SummaryLib describe their summaries as about twenty minutes, and Smart Reading notes that summaries of serious books can reach twenty pages. Zehn summaries take fifteen to twenty minutes in audio with synced text. Longer summaries keep more examples; shorter ones fit a commute."),
        ("Do Blinkist or Headway have Russian summaries?",
         "Neither lists Russian among its summary languages on its own website. Blinkist lists English, German, Spanish and Portuguese, and Headway lists eleven languages without Russian. Russian readers usually choose a Russian service like Smart Reading or a multilingual app like Zehn."),
    ],
    related=["best-book-summary-apps", "which-app-summarises-books-in-russian", "book-summary-apps-for-non-english-speakers"],
),
"book-summary-apps-for-non-english-speakers": dict(
    cat="summary-apps",
    title="Book Summary Apps for Non-English Speakers (2026)",
    desc="Which book summary apps work in your language? Arabic, Russian, Hindi, Urdu, Spanish, German and more, compared by the languages each app actually offers.",
    h1="Book summary apps for non-English speakers",
    lead="Most book summary apps are built for English readers first. If you think in Arabic, Russian, Hindi, Urdu or Spanish, the right app depends almost entirely on which languages it really covers. This page sorts the main apps by language.",
    tldr=["Spanish, German, Portuguese: Blinkist, Shortform, 12min and Headway all cover some of these.", "Arabic: Wajeez, Durar, Ejaz and Zehn. Russian: Smart Reading, SummaryLib and Zehn.", "Hindi and Urdu: few options; Zehn has libraries in both."],
    sections=[
        ("Are there book summary apps in other languages?", [
            "Yes, but coverage is uneven. European languages like Spanish, German and Portuguese are covered by several big apps. Arabic and Russian have their own local apps. Hindi and Urdu have very few options. Zehn is one of the few apps with libraries in Arabic, Russian, Hindi and Urdu as well as English.",
            DISCLOSE,
        ]),
        ("Which app covers which language?", [
            ("table", ["Language", "Apps that list it (on their own pages)"], [
                ["Spanish", "Blinkist, Headway, Shortform, 12min"],
                ["German", "Blinkist, Headway, Shortform"],
                ["Portuguese", "Blinkist, Headway, Shortform (Brazilian), 12min"],
                ["French, Italian, Polish, Japanese", "Headway"],
                ["Arabic", "Wajeez, Durar, Ejaz, Zehn"],
                ["Russian", "Smart Reading, SummaryLib, Zehn"],
                ["Hindi, Urdu", "Zehn"],
            ]),
        ]),
        ("Why native-language summaries matter", [
            "Reading in your strongest language is faster and you remember more, especially for ideas you want to apply. A summary written for your language also picks examples and wording that make sense to you, which a machine translation of an English summary often doesn't. If you are learning English, bilingual apps let you compare.",
            ("ul", ["**Check the narration:** a natural human or high-quality voice in your language matters for audio.", "**Check the library in your language,** not the app's total: many apps have far fewer titles outside English.", "**Check the app interface:** some apps translate only the summaries, not the menus."]),
        ]),
        ("If you are learning English", [
            "Summaries are a useful step between textbooks and full books: short, clear, on topics you care about. Bilingual apps like Durar and Ejaz show the same summary in Arabic and English. In Zehn you can listen to an English summary with synced text and ask the Language Tutor coach about new words. Our guide on [learning a language with AI](/en/guides/learn-a-language-with-ai/) has a daily routine.",
        ]),
        ("Test an app in your language in ten minutes", [
            ("ol", ["Switch the app to your language and search for three books you actually want.", "Open one summary and read the first screen: does it sound natural, or like a translation?", "Play the audio for two minutes: is the voice clear at normal speed?", "Check whether menus, search and support are in your language too.", "Look up the price in your country; several apps adjust prices by region."]),
            "If an app passes all five checks, use its free option for a week before paying.",
        ]),
        ("How we compared these apps", [
            "We read each app's own website or official store listing on 23 November 2026 and copied only what the app states about itself: languages, library size, summary length, format and free options. We did not score or rank the apps, because the right choice depends on what you read and how. Where an app doesn't state something, we leave it out rather than guess.",
            "We make Zehn, which is why its strengths and limits are listed separately and in the same plain terms as the others. If you know of an app we missed or a fact that has changed, tell us and we'll check it.",
        ]),
        ("Zehn for non-English speakers: strengths and limits", [
            ("table", ["Strengths", "Limits"], [
                ["Libraries in English, Arabic, Russian, Hindi, Urdu and Tajik", "No Spanish, German or other European-language library"],
                ["AI answers in the language you write in", "AI features need a paid plan"],
                ["Prices adjusted in 30+ countries", "Mobile apps only"],
            ]),
        ]),
        ("Sources", [
            ("sources", [S_BLINKIST, S_HEADWAY, S_SHORTFORM, S_12MIN, S_WAJEEZ, S_DURAR, S_EJAZ, S_SMART, S_SUMLIB, S_ZEHN]),
        ]),
    ],
    faq=[
        ("Which book summary app supports the most languages?",
         "On their own pages, Headway lists eleven summary languages, mostly European plus Japanese. Zehn lists six, including Arabic, Russian, Hindi and Urdu. Blinkist, Shortform and 12min list three or four European languages each. The best app is the one that covers your language with a good library, not the longest list."),
        ("Is there a book summary app in Hindi or Urdu?",
         "Options are limited. Zehn has libraries in both Hindi and Urdu alongside English, Arabic, Russian and Tajik, with audio and synced text. The large English-first apps don't list Hindi or Urdu on their websites. Search the app store in Latin script too, as many people search for 'hindi books' or 'urdu books'."),
        ("Can I use an English summary app with a translator?",
         "You can, but it's slower and loses nuance, especially for audio, and machine translation often misses idioms and examples. If an app offers your language natively, the experience is usually much better. If not, reading English summaries can also be good language practice when you are at an intermediate level."),
        ("Do non-English libraries have the same books?",
         "Usually not. Most apps have their largest library in their main language and fewer titles in others. Before subscribing, search for three books you want in your language, not in English. Local-first apps often include regional authors that international apps don't have."),
    ],
    related=["best-book-summary-apps", "best-arabic-book-summary-apps", "best-russian-book-summary-apps"],
),
# ------------------------------------------------------------------ question pages
"is-there-a-book-summary-app-in-arabic": dict(
    cat="quick-answers", kind="qa",
    title="Is There a Book Summary App in Arabic? Yes: Here Are 4",
    desc="Yes. Wajeez, Durar, Ejaz and Zehn offer book summaries in Arabic, with audio. What each one is best for, in two minutes.",
    h1="Is there a book summary app in Arabic?",
    answer="Yes. Wajeez has the largest Arabic audio library, including book summaries, podcasts and novels. Durar and Ejaz offer the same summaries in Arabic and English. Zehn has an Arabic library narrated in Modern Standard Arabic, with Ask AI on every book. Big English apps like Blinkist and Headway don't list Arabic.",
    lead="Here is the quick version, with links to the details.",
    tldr=["Four apps with Arabic summaries: Wajeez, Durar, Ejaz, Zehn.", "Pick by what you need: most audio, bilingual, or AI.", "Full comparison on our best Arabic book summary apps page."],
    sections=[
        ("Which one fits you?", [
            ("table", ["If you want…", "Try"], [
                ["The most Arabic audio, with podcasts and novels", "Wajeez"],
                ["Arabic and English for the same summary", "Durar or Ejaz"],
                ["To ask questions about the book in Arabic", "Zehn"],
            ]),
            "We make Zehn. Facts about the other apps come from their own websites and store pages, checked 23 November 2026. The [full comparison](/en/guides/best-arabic-book-summary-apps/) has sources and what to check before paying.",
        ]),
        ("What about Blinkist, Headway and Shortform?", [
            "The big international apps publish their summary languages on their own websites, and none of them lists Arabic. They are strong choices if you read in English or a major European language, but for Arabic you will get a better experience from an app that writes and narrates summaries in Arabic from the start.",
        ]),
        ("Are any of them free?", [
            "Durar gives one free summary every day, and Zehn's free plan includes one book summary a day without AI. The others offer trials or subscriptions. Prices can differ by country.",
        ]),
    ],
    faq=[
        ("Is there an Arabic version of Blinkist?",
         "Blinkist's own website lists English, German, Spanish and Portuguese, not Arabic. Arabic readers usually use an Arabic-first app such as Wajeez, a bilingual app such as Durar or Ejaz, or Zehn, which has an Arabic library with Ask AI on every book."),
        ("Which Arabic book summary app has AI?",
         "Zehn has Ask AI on every book, a chat that answers questions from that book, plus an AI Chat with coaching personas, and it replies in Arabic. The AI features are part of Zehn's paid plans; the free plan includes one book summary a day without AI."),
    ],
    related=["best-arabic-book-summary-apps", "best-book-summary-apps", "book-summary-apps-for-non-english-speakers"],
),
"which-app-summarises-books-in-russian": dict(
    cat="quick-answers", kind="qa",
    title="Which App Summarises Books in Russian? 3 Options",
    desc="Smart Reading, SummaryLib and Zehn summarise books in Russian; MyBook has full books. What each one is best for, in two minutes.",
    h1="Which app summarises books in Russian?",
    answer="Smart Reading is the largest Russian summary service, with over 1,000 summaries in text, audio and infographics. SummaryLib is a smaller Russian library of about 400 books. Zehn has a Russian library with Ask AI on every book. For full books instead of summaries, MyBook is a large Russian subscription library.",
    lead="Here is the quick version, with links to the details.",
    tldr=["Three summary options in Russian: Smart Reading, SummaryLib, Zehn.", "MyBook for whole books.", "Full comparison on our best Russian book summary apps page."],
    sections=[
        ("Which one fits you?", [
            ("table", ["If you want…", "Try"], [
                ["The biggest Russian summary library, with tests and infographics", "Smart Reading"],
                ["A small curated library", "SummaryLib"],
                ["To ask questions about a book, or several languages in one app", "Zehn"],
                ["Complete books and audiobooks", "MyBook"],
            ]),
            "We make Zehn. Facts about the other services come from their own websites, checked 23 November 2026. The [full comparison](/en/guides/best-russian-book-summary-apps/) has sources.",
        ]),
        ("What about Blinkist, Headway and Shortform?", [
            "The big international apps publish their summary languages on their own websites, and none of them lists Russian. They are strong choices if you read in English or a major European language, but for Russian you will get a better experience from an app that writes and narrates summaries in Russian from the start.",
        ]),
        ("Are any of them free?", [
            "Smart Reading and SummaryLib offer seven-day trials, MyBook fourteen days on Premium, and Zehn's free plan includes one summary a day without AI.",
            "Before paying, search each service for three books you want and check payment options in your country, since some services accept only certain cards.",
        ]),
    ],
    faq=[
        ("Does Blinkist have Russian summaries?",
         "Blinkist's website lists English, German, Spanish and Portuguese, not Russian. Russian readers usually choose a Russian service such as Smart Reading or SummaryLib, or a multilingual app such as Zehn, which has a Russian library and an AI chat on every book."),
        ("How long is a Russian book summary?",
         "Smart Reading and SummaryLib describe their summaries as about twenty minutes, and some Smart Reading summaries of serious books reach twenty printed pages. Zehn summaries take fifteen to twenty minutes as audio with synced text, which fits a typical commute."),
    ],
    related=["best-russian-book-summary-apps", "best-book-summary-apps", "book-summary-apps-for-non-english-speakers"],
),
"can-ai-explain-a-book": dict(
    cat="quick-answers", kind="qa",
    title="Can AI Explain a Book to Me? Yes, With Some Limits",
    desc="Yes: AI can explain a book's ideas, answer questions and quiz you. How to ask well, what it gets wrong, and apps that put AI on every book.",
    h1="Can AI explain a book to me?",
    answer="Yes. An AI chat can explain a book's main ideas, define terms, give examples and quiz you, which helps with hard books. It works best when it has the book's text or a summary to work from; from memory alone it can mix up details or invent them. Check anything important against the book itself.",
    lead="How to get a useful explanation, and what to watch out for.",
    tldr=["AI explains well, but can be confidently wrong about details.", "Give it the chapter or a summary, then ask specific questions.", "Apps like Zehn put an AI chat on each book that answers from that book."],
    sections=[
        ("How do I ask AI to explain a book?", [
            "Be specific. Name the book and author, say your level and what confuses you, and ask for an everyday example. Paste a passage if you can.",
            ("prompt", "Explain the main idea of chapter [number] of [title] by [author] in simple words, with one everyday example. Then ask me two questions to check I understood."),
            ("prompt", "Here is a passage from [title]: [passage]. What is the author arguing, and what is the strongest objection to it?"),
        ]),
        ("What can go wrong?", [
            ("ul", ["**Invented details:** quotes, page numbers or examples that aren't in the book.", "**Blended books:** mixing up two books with similar ideas.", "**Flattening:** reducing a nuanced argument to a slogan."]),
            "Ask for the reasoning, check surprising claims against the text, and treat the AI as a study partner rather than a source. Our guide on [remembering what you read](/en/guides/remember-what-you-read/) shows how to use AI to quiz yourself.",
        ]),
        ("Apps with AI on every book", [
            "In Zehn, every book has Ask AI, a chat that answers from that book's summary, so it stays on topic. It is part of the paid plans ($9.99/month or $36/year with a 7-day trial). The [Science Explainer](/en/science-explainer/) coach on this site has more prompts for understanding hard ideas.",
        ]),
    ],
    faq=[
        ("Is it cheating to use AI to understand a book?",
         "Using AI to understand ideas, check your reasoning or quiz yourself is studying, not cheating. Submitting AI-written text as your own work is different and usually breaks school rules. Read the book or its summary yourself, use AI to clarify, and write your own answers."),
        ("Can AI read a whole book for me?",
         "Some tools can process long files you upload, but you should only upload books you have the rights to. Book summary apps offer summaries written for that purpose, and some, like Zehn, add an AI chat that answers from each book's summary."),
    ],
    related=["remember-what-you-read", "claude-vs-gemini-vs-deepseek-vs-grok", "best-book-summary-apps"],
),
"app-to-discuss-books-with-other-readers": dict(
    cat="quick-answers", kind="qa",
    title="Is There an App to Discuss Books With Other Readers?",
    desc="Yes: reading communities, book club apps and summary apps with discussion features. Which kind fits you, and how Zehn's Book Club tab works.",
    h1="Is there an app to discuss books with other readers?",
    answer="Yes. Reading communities let you review books and join groups, and some book summary apps have discussion built in: Shortform has community discussions on its guides, and Zehn has a Book Club tab where you join topic clubs, post your take on a book and reply to others. A small book club still gives the deepest conversations.",
    lead="Which kind of discussion fits you, in two minutes.",
    tldr=["Reading communities: reviews and groups around full books.", "Summary apps with discussion: Shortform (community discussions), Zehn (Book Club tab).", "A small book club gives the deepest talks."],
    sections=[
        ("Three ways to discuss books", [
            ("table", ["Option", "Best for"], [
                ["Reading community apps and websites", "Reviews, ratings and large groups around full books"],
                ["Summary apps with discussion", "Busy readers who want to talk about ideas after a 15-minute summary"],
                ["Your own book club, in person or online", "Deeper, regular conversations with people you know"],
            ]),
        ]),
        ("How does the Zehn Book Club work?", [
            "In the Zehn app, the Book Club tab has topic clubs, such as Calm Club in Mindfulness & Happiness. Each club has a description, rules, a “What's on your mind today?” box and Posts and Challenges tabs. You post like a short social post and others reply in the comments. Details on our [Zehn Book Club](/en/zehn/book-club/) page.",
        ]),
        ("Starting your own club", [
            "If you'd rather talk face to face or on video, our guide on [how to start a book club](/en/guides/how-to-start-a-book-club/) covers size, rules and the first meeting, and our [discussion questions](/en/guides/book-club-discussion-questions/) work for any book.",
        ]),
    ],
    faq=[
        ("Can I discuss a book if I only read the summary?",
         "Yes, especially for nonfiction, where the discussion is usually about ideas and how to apply them. Say that you read the summary so others know. Many busy readers join discussions after a 15 to 20 minute summary and read the full book later if the conversation hooks them."),
        ("Is the Zehn Book Club free?",
         "The Book Club is a tab inside the Zehn app, which has a free plan with one book summary a day. Check the app for current access to posting and challenges. The paid Zehn Pro plan adds unlimited books, offline listening and the AI features."),
    ],
    related=["how-to-start-a-book-club", "book-club-with-summaries", "best-book-summary-apps"],
),
}
