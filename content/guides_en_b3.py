"""Batch 3 (EN): reading statistics page from public sources."""

SRC = [
    ("Arab Reading Index 2016, MBRF & UNDP (PDF)", "https://knowledge4all.com/pdf/Arab%20Reading%20Index/Arab%20Reading%20Index%202016_Eng.pdf", "published Dec 2016"),
    ("VTsIOM survey on reading, via TASS", "https://tass.com/society/2117373", "survey 7–8 Mar 2026"),
    ("VTsIOM, “The most reading country: monitoring”", "https://wciom.ru/analytical-reviews/analiticheskii-obzor/samaja-chitajushchaja-strana-monitoring", "17 Apr 2023"),
    ("Pew Research Center, book reading short read", "https://www.pewresearch.org/short-reads/2026/04/09/americans-still-opt-for-print-books-over-digital-or-audio-versions-few-are-in-book-clubs", "survey Oct 2025, published 9 Apr 2026"),
    ("Pew Research Center topline (PDF)", "https://www.pewresearch.org/wp-content/uploads/sites/20/2026/04/S_26.04.09_books_topline.pdf", "Oct 2025"),
    ("National Literacy Trust, Children and young people's reading in 2026", "https://literacytrust.org.uk/research-services/research-reports/children-and-young-peoples-reading-in-2026/", "Jun 2026"),
    ("UNESCO, International Literacy Day 2025 factsheet (PDF)", "https://www.unesco.org/sites/default/files/medias/fichiers/2025/09/ild-2025-factsheet.pdf", "Sep 2025"),
    ("World Bank / UNESCO UIS, adult literacy rate", "https://data.worldbank.org/indicator/SE.ADT.LITR.ZS", "latest year 2024"),
]

GUIDES = {
"reading-statistics": dict(
    cat="reading-habits", date="2026-11-24", date_h="24 November 2026",
    title="Reading Statistics 2026: Arab, Russian & English Readers",
    desc="How much do people read in 2026? Cited figures for Arab, Russian, US and UK readers from the Arab Reading Index, VTsIOM, Pew, the NLT and UNESCO.",
    h1="How people read in 2026: Arab, Russian and English-speaking readers",
    lead="Reading statistics travel fast and are often wrong. This page collects figures from the original surveys only, with links, so you can quote them with confidence: how much Arab, Russian, American and British readers read, in what formats, and what stops them reading more.",
    tldr=["Arab readers averaged 16 books and 35 hours a year in the largest regional survey (148,000 people); the famous “6 minutes a year” has no documented source.", "In Russia, 52% say they often read books; lack of time is the top barrier (58%).", "In the US, 75% of adults read a book in the past year; audiobooks rose from 11% (2011) to 26% (2025)."],
    sections=[
        ("How much do Arabs read? The “six minutes a year” myth", [
            "The Arab Reading Index 2016, run by the Mohammed bin Rashid Al Maktoum Foundation with UNDP and answered by about 148,000 people in 22 countries, found an Arab average of 16.08 books and 35.24 hours of reading a year. The often-repeated claim that Arabs read six minutes a year has no identified original source, as the report itself notes.",
            ("table", ["Arab Reading Index 2016", "Figure"], [
                ["Average books read per year", "16.08 (range 1.74 to 28.67 by country)"],
                ["Average reading hours per year", "35.24 (range 7.78 in Somalia to 63.85 in Egypt)"],
                ["Countries above the Arab average (books)", "Lebanon, Morocco, Egypt, UAE, Tunisia, Jordan, Saudi Arabia, Qatar, Bahrain, Palestine, Algeria, Oman"],
                ["Respondents", "About 148,000 across 22 countries"],
            ]),
            "Two cautions: the survey was online, so it over-represents connected readers, and it dates from 2016. It is still the largest measured study of reading in the region, which makes it a far better source than unsourced numbers.",
        ]),
        ("How much do Russians read?", [
            "In a VTsIOM telephone survey of 1,600 adults in March 2026, 52% of Russians said they often read books and 48% said they usually don't. Among readers, 33% read one to five books a year, 25% read six to ten and 29% read more than eleven. The main barrier named was lack of time (58%), well ahead of book prices (18%).",
            ("table", ["VTsIOM", "Figure"], [
                ["Often read books (2026)", "52%"],
                ["Readers who read daily or several times a week (2026)", "71%"],
                ["Read for pleasure / to learn (2026)", "57% / 43%"],
                ["Barrier: lack of time / book prices (2026)", "58% / 18%"],
                ["Read a book in the last 3 months (2013 → 2023)", "47% → 57%"],
                ["Have a home library (2023)", "87%"],
            ]),
        ]),
        ("How much do Americans read, and in what format?", [
            "Pew Research Center's survey of 8,046 US adults in October 2025 found that 75% read at least part of a book in the past year. Print still leads at 64%, but e-books (31%) and audiobooks (26%) have grown steadily since 2011, when they were 17% and 11%. Only 7% of adults took part in a book club.",
            ("table", ["Pew Research Center", "2011", "2025"], [
                ["Read a print book", "72%", "64%"],
                ["Read an e-book", "17%", "31%"],
                ["Listened to an audiobook", "11%", "26%"],
            ]),
            ("table", ["Books read in the past 12 months (2025)", "Share of US adults"], [
                ["None", "25%"], ["1 to 5", "37%"], ["6 to 20", "23%"], ["More than 20", "14%"],
            ]),
        ]),
        ("Are children reading less?", [
            "In the UK, the National Literacy Trust's 2026 survey of 125,375 children and young people found that 36.1% of 8–18-year-olds enjoy reading in their free time, up from 32.7% in 2025, the lowest level in twenty years. Only 20.3% read something daily in their free time. Enjoyment was 58.6% in 2016, so the long-term decline remains large.",
        ]),
        ("How many people can read at all?", [
            "UNESCO reports that the global adult literacy rate rose from 86% in 2015 to 88% in 2024, with youth literacy at 93%, yet 739 million adults still lack basic literacy skills. In World Bank data drawn from UNESCO, the adult literacy rate for the Arab World was 79% in 2024, with wide differences between countries.",
        ]),
        ("What the numbers say about reading habits", [
            ("ul", ["**Time, not interest, is the main barrier.** Russian readers name lack of time far more than price or lack of interesting books.", "**Formats are diversifying.** Audiobooks more than doubled in the US since 2011; readers fit books into commutes and chores.", "**Myths outlive data.** The “six minutes” figure keeps circulating years after a 148,000-person survey contradicted it.", "**Reading is social for few.** Only 7% of US adults were in a book club, even though discussing books helps people finish them."]),
            "If time is your barrier, our guide on [how to read more books when you have no time](/en/guides/read-more-books/) has practical steps, and 15–20 minute summaries in apps like Zehn are one way to fit books into a commute.",
        ]),
        ("Sources", [
            ("sources", SRC),
            "You may quote these figures with a link to the original source; a link to this page is appreciated. Found a newer survey? Write to contact@safarigrp.com.",
        ]),
    ],
    faq=[
        ("Is it true that Arabs read only six minutes a year?",
         "No reliable source supports it. The Arab Reading Index 2016 notes that the figure has no clear documented origin, and its own survey of about 148,000 people found an average of 16 books and 35 hours of reading a year. Reading levels vary widely by country, from under 2 books in some to almost 29 in Lebanon."),
        ("What percentage of Russians read books?",
         "In VTsIOM's March 2026 survey, 52% of Russian adults said they often read books and 48% said they usually don't. In VTsIOM's 2023 monitoring, 57% had read a book in the previous three months, up from 47% in 2013. Lack of time was the most common reason for not reading more."),
        ("How many Americans read books?",
         "Pew Research Center found that 75% of US adults read at least part of a book in the 12 months before its October 2025 survey. Print was most common at 64%, followed by e-books at 31% and audiobooks at 26%. A quarter of adults read no books in that period."),
        ("Are audiobooks growing?",
         "Yes, at least in the United States. Pew's data show the share of adults who listened to an audiobook in the past year rose from 11% in 2011 to 26% in 2025, more than doubling, while print reading fell slightly from 72% to 64%. Growth has slowed since 2021."),
    ],
    related=["read-more-books", "52-books-a-year-reading-challenge", "best-book-summary-apps"],
),
}
