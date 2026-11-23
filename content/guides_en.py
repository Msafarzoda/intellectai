"""English guides (wave 1). Blocks: str = paragraph, ("ul"|"ol", [..]), ("table", hdr, rows), ("tip", text),
("prompt", text), ("ui", "club"|"chat"). Inline links: [text](url)."""

UI = dict(
    nav_guides="Guides", guides_h1="Guides: reading, book clubs and learning with AI",
    guides_title="Guides on Reading, Book Clubs & AI Learning | Intellect AI",
    guides_desc="Free, practical guides: start a book club, read more books, remember what you read, learn a language with AI and compare AI models for learning.",
    guides_lead="Practical, free guides for people who want to read more, discuss books with others and learn faster with AI. Each one stands on its own; Zehn shows up only where it really helps.",
    guides_tldr=["Four topics: book clubs, reading habits, learning with AI and Zehn guides.", "Every guide has a short answer first, then steps, examples and an FAQ.", "New guides are added every week."],
    read_min="{n} min read", updated="Updated", in_cat="More in {cat}", related_h="Related guides",
    all_guides="All guides", cta_default_h="Try it in the Zehn app",
    cta_default_p="Zehn has 10,000+ book summaries of 15–20 minutes, Ask AI on every book, an AI Chat with nine coaches and a Book Club tab.",
    quiz_nav="What to read?", ui_cap_club="Zehn Book Club tab, rebuilt from the real app. Example post.",
    home_guides_h="Guides and tools", home_guides_p="Start with one of these.",
    social_h="Follow Zehn", about="About",
    club_member="Example post",
    club_post=("Is \u201cDeep Work\u201d realistic with two kids?", "Loved the idea of 90-minute focus blocks. Has anyone made it work at home?"),
)

DATE = "23 November 2026"

CATS = {
    "book-clubs": ("Book clubs", "Start a club, run better discussions and keep busy members reading."),
    "reading-habits": ("Reading habits", "Read more, remember more and make reading a daily habit."),
    "learn-with-ai": ("Learn with AI", "Use AI tutors and coaches to learn faster, without the hype."),
    "zehn-guides": ("Zehn guides", "What Zehn is and how people use it in a normal day."),
}

GUIDES = {
# ---------------------------------------------------------------- book clubs
"how-to-start-a-book-club": dict(
    cat="book-clubs",
    title="How to Start a Book Club: Step-by-Step Guide | Intellect AI",
    desc="How to start a book club that lasts: size, roles, schedule, rules, picking books and running the first meeting. Works online and in person.",
    h1="How to start a book club that lasts",
    lead="Most book clubs don't fail because of the books. They fail because nobody knows when the next meeting is, the group is too big to talk, or half the members stop reading by month two. Here is a simple setup that avoids all three.",
    tldr=["Start small: 4–8 people who actually want to read.", "Fix one rhythm (for example the first Sunday of every month) and one place before you pick a book.", "Give the club three simple rules and rotate who hosts and who chooses the book."],
    sections=[
        ("What is the first step to starting a book club?", [
            "Decide what kind of club you want before you invite anyone. Write one sentence: who it's for, what you'll read and how often you'll meet, for example “friends from work, one nonfiction book a month, online on the first Sunday”. That sentence makes inviting people easy and keeps the club from drifting later.",
            ("ul", ["**Theme:** nonfiction, novels, one genre, or books in a language you're learning.", "**Format:** in person (homes, a café, a library room) or online (video call or a group chat).", "**Pace:** one book a month suits most adults. Busy groups can pick shorter books or use summaries to keep up."]),
        ]),
        ("How many people should be in a book club?", [
            "Four to eight active members is the sweet spot. Fewer than four and one cancellation kills the meeting; more than ten and quieter people stop talking. If interest grows, split into two clubs rather than one big one. Invite about twice as many people as you want, since not everyone will say yes.",
        ]),
        ("How do you set the schedule and the rules?", [
            "Pick one fixed rhythm and stick to it: same weekday, same week of the month, same time. A fixed slot beats a poll every month, because polls are where clubs die. Then agree on three short rules in the first meeting and write them in the group chat.",
            ("ol", ["**Come even if you haven't finished.** Partial readers keep the club alive; just say where you stopped.", "**Spoilers are fine after the meeting date is set.** Or agree on the opposite. The point is to decide.", "**Everyone speaks once before anyone speaks twice.** It's the simplest way to keep one voice from taking over."]),
        ]),
        ("How do you choose the books?", [
            "Rotate the choice. Each month a different member brings three options and the group votes, or the host simply decides. Limit the length (for example under 350 pages) so working members can finish. Mixing one “serious” book with one lighter book in turn keeps energy up.",
            ("tip", "Not sure a book will spark a discussion? Read a 15-minute summary first. If the summary alone gives you three questions to ask, the full book will work for a group."),
        ]),
        ("Who does what in a book club?", [
            ("table", ["Role", "What they do", "Rotate?"], [
                ["Organiser", "Keeps the calendar, sends one reminder a week before", "Rarely"],
                ["Host", "Offers the place or the video link, opens and closes the meeting", "Every meeting"],
                ["Picker", "Brings 2–3 book options for the next month", "Every meeting"],
                ["Question lead", "Prepares 5–8 questions for the discussion", "Every meeting"],
            ]),
            "In small clubs one person can hold two roles. What matters is that the reminder and the questions are someone's job, not everyone's.",
        ]),
        ("How do you run the first meeting?", [
            ("ol", ["**10 minutes:** introductions and why each person joined.", "**5 minutes:** agree on the three rules and the meeting rhythm.", "**40 minutes:** discuss the first book with 5–8 prepared questions (see our [book club discussion questions](/en/guides/book-club-discussion-questions/)).", "**5 minutes:** vote on the next book and confirm the date."]),
            "Keep the whole thing to about an hour. Ending on time while people still want to talk is the best advert for the next meeting.",
        ]),
        ("How do you keep an online book club going?", [
            "Online clubs need more structure than in-person ones, because nobody bumps into each other between meetings. Post one small prompt a week in the group chat (“Which chapter surprised you?”), keep video calls to 60 minutes and record nothing unless everyone agrees. A shared note with the book list and dates saves endless “what are we reading?” messages.",
            "If you'd rather not build a group chat at all, readers in the Zehn app can join topic clubs in the [Zehn Book Club](/en/zehn/book-club/) tab and post their take on a book there.",
        ]),
    ],
    faq=[
        ("How often should a book club meet?",
         "Once a month works for most adult book clubs, because it gives working people enough time to read a normal-length book. Groups that read shorter books or summaries sometimes meet every two weeks. Whatever you choose, keep the same rhythm and time so nobody has to check a poll before every meeting."),
        ("What if members don't finish the book?",
         "Make it normal. Ask everyone to come anyway and say where they stopped, then discuss the parts most people read. Some clubs share a 15-minute summary so late readers can follow the conversation. Shorter books and a fixed reading plan of a few chapters a week also help more people finish on time."),
        ("Can a book club work online?",
         "Yes. Online clubs work well for friends in different cities and for people with small children. Use one video link that never changes, keep calls to about an hour, and post one short question in the group chat each week. A shared list of books and dates keeps everyone on the same page."),
        ("How do you choose a name for a book club?",
         "Pick a name that says who the club is for or what it reads, such as the city, the genre or a shared joke. Short names are easier to use in group chats and invitations. Avoid names that limit the club too much if you might change themes later, and let members vote on two or three options."),
    ],
    related=["book-club-discussion-questions", "book-club-with-summaries", "read-more-books"],
),
"book-club-discussion-questions": dict(
    cat="book-clubs",
    title="Book Club Discussion Questions for Any Book | Intellect AI",
    desc="Ready-to-use book club discussion questions for nonfiction and novels, plus how to use an AI coach to write questions for any book in minutes.",
    h1="Book club discussion questions for any book",
    lead="Good questions turn a polite summary round into a real conversation. Below are question sets you can use for almost any book, how to order them, and a quick way to generate questions for a specific title with AI.",
    tldr=["Open with personal questions, move to the ideas, end with “what will you do differently?”.", "Six to eight questions are enough for an hour.", "AI can draft questions for any book in a minute; a human should pick the best ones."],
    sections=[
        ("What makes a good book club question?", [
            "A good question has no single right answer and connects the book to the reader's own life. “Did you like it?” ends in a yes or no. “Which idea would you actually try at work, and what would stop you?” gets people telling stories, disagreeing politely and remembering the book weeks later.",
        ]),
        ("Questions for any nonfiction book", [
            ("ol", ["What was the one idea you underlined or remembered first?", "Which claim in the book did you not believe? Why?", "Where does the author's advice not fit your life, job or culture?", "If you had to explain the book to a 12-year-old in two sentences, what would you say?", "Which example or story from the book stayed with you?", "What would the opposite of this book's main idea look like? Is it ever true?", "Which small thing will you do differently this month because of the book?", "Who should not read this book?"]),
        ]),
        ("Questions for any novel", [
            ("ol", ["Which character would you most like to meet, and which would you avoid?", "When did your opinion of a character change?", "What did the setting add to the story? Could it happen anywhere else?", "Which scene would you cut, and which would you make longer?", "What do you think happens to the main character after the last page?", "Did the ending feel earned or rushed?", "What question would you ask the author?"]),
        ]),
        ("Warm-up and closing questions", [
            ("ul", ["**Warm-up:** Where and when did you read most of it? Did you finish, and if not, where did you stop?", "**Rating round:** Out of 5, and in one word, why?", "**Closing:** What will you remember about this book in a year? Would you recommend it to the club's next new member?"]),
            "Use the rating round last, not first, so early scores don't steer the conversation.",
        ]),
        ("How do you use AI to write questions for a specific book?", [
            "An AI coach can draft questions for any book in a minute, which saves the question lead an evening. Give it the title, the author, your group and the tone you want, then ask for more questions than you need and pick the best six. Always check that the questions match what is actually in the book.",
            ("prompt", "Act as a book club host. Our group of [number] [describe members] read [title] by [author]. Write 12 discussion questions: 3 warm-up, 6 about the main ideas, 3 that connect the book to our own lives. Make them open-ended and avoid spoilers before question 7."),
            ("prompt", "Here are our notes from the last meeting: [notes]. Suggest 3 follow-up questions for the next session that build on what we disagreed about."),
            "You can paste these into any AI chat. In Zehn, the [Ask AI](https://thezehnapp.com/en/ask-ai/) button on each book page answers questions about that specific book, which helps when you want to check what a chapter actually says.",
        ]),
        ("How should the host run the discussion?", [
            ("ul", ["Ask a question, then wait five seconds before rescuing the silence.", "Invite a quiet member by name with an easy question (“what did you think of chapter 2?”).", "If two people debate for too long, ask a third person which side they're on.", "Stop at the agreed time, even mid-conversation. Leftover energy carries into next month."]),
        ]),
    ],
    faq=[
        ("How many questions does a book club need?",
         "Six to eight good questions usually fill a one-hour meeting, because the best ones lead to follow-ups and stories. Prepare ten or twelve so the host can skip the ones that don't land. Start with one easy warm-up, spend most of the time on ideas and finish with a question about what members will actually do."),
        ("Who should prepare the discussion questions?",
         "Rotate the job. A different member prepares the questions each month, usually the person who picked the book or the host. Rotation spreads the work and gives every meeting a slightly different flavour. The organiser can keep a shared document of past questions that worked well, so nobody starts from zero."),
        ("Can AI write good book club questions?",
         "AI is good at drafting many open-ended questions quickly, especially for well-known books. It can also make mistakes about plot details or invent things the book doesn't say. Ask for more questions than you need, delete anything you can't confirm, and keep the ones that connect to your group's real lives."),
        ("What if nobody talks at the meeting?",
         "Start with a round where everyone answers the same easy question, such as one sentence about where they read the book. Then ask for opinions, not facts. Personal questions like “where did the book not fit your life?” get quieter members talking. If the group is very quiet, try smaller breakout pairs for five minutes."),
    ],
    related=["how-to-start-a-book-club", "book-club-with-summaries", "remember-what-you-read"],
),
"book-club-with-summaries": dict(
    cat="book-clubs",
    title="Book Club With Summaries: Keep Busy Members Reading",
    desc="How busy book clubs use 15–20 minute summaries so everyone can join the discussion, when summaries help and when to read the whole book.",
    h1="Running a book club with summaries",
    lead="The most common reason people quit a book club is time, not interest. Summaries won't replace reading for a book lover, but they can keep a busy member in the conversation. Here is how to use them without turning the club into a summary club.",
    tldr=["Use summaries as a bridge for members who fall behind, or to choose the next book.", "Agree in advance what counts as “coming prepared”.", "Keep the discussion about ideas and your own lives, not about who read every page."],
    sections=[
        ("Is it OK to use summaries in a book club?", [
            "Yes, if the group agrees on how. Summaries help members who are short on time follow the discussion and contribute, which is better than them skipping the meeting. They are not a full replacement for the book: you lose the author's examples, tone and detail. Decide openly what your club expects.",
        ]),
        ("Three ways clubs use summaries", [
            ("table", ["Model", "How it works", "Best for"], [
                ["Bridge", "Most people read the book; anyone behind reads a 15–20 min summary before the meeting", "Mixed groups, parents, shift workers"],
                ["Pick-first", "The club reads summaries of 3 candidate books, then votes and reads the winner in full", "Clubs that often pick books nobody finishes"],
                ["Summary sprint", "Everyone reads or listens to one summary a week and meets briefly to discuss one idea", "Work teams, study groups, very busy friends"],
            ]),
        ]),
        ("How do you keep the discussion deep?", [
            "Ask questions about application and disagreement, not plot details. “Where would this idea fail in our city?” works whether someone read 300 pages or a summary. Encourage members who read the full book to bring one example the summary left out; that turns them into guides rather than judges.",
            ("ul", ["Ask each member for one idea they would test this month.", "Ask what the author would say about a real situation in the group.", "Ask full readers: “What did the whole book add that a summary can't?”"]),
        ]),
        ("How does the Zehn Book Club tab help?", [
            "In the Zehn app, the Book Club tab has topic clubs, such as Calm Club in Mindfulness & Happiness. Each club has a description, rules, a “What's on your mind today?” box and Posts and Challenges tabs. You post your take on a book like a short social post, others reply in the comments, and you can take part in club challenges.",
            ("ui", "club"),
            "A practical rhythm for a busy group: everyone listens to the 15–20 minute summary of the month's book in Zehn, posts one takeaway in the club during the week, and the people who want more read the full book before the live meeting. More about the tab on our [Zehn Book Club](/en/zehn/book-club/) page.",
        ]),
        ("When should the club read the whole book?", [
            ("ul", ["**Novels and memoirs:** the story, voice and emotion are the point. Summaries spoil without delivering.", "**Books you'll argue about:** you need the author's actual evidence, not a compressed version.", "**Books the club chose for pleasure:** don't optimise fun away."]),
            "A good rule: summaries for screening and catching up, full books for the titles the club cares most about.",
        ]),
        ("A sample month with summaries", [
            ("ol", ["**Week 1:** the picker shares three candidate books; everyone listens to their summaries and votes.", "**Week 2:** members start the winning book; anyone short on time listens to its summary.", "**Week 3:** each member posts one idea and one question in the group or club feed.", "**Week 4:** the meeting, with questions built from those posts."]),
        ]),
    ],
    faq=[
        ("Do summaries spoil the book?",
         "For nonfiction, a summary rarely spoils anything, because the value is in applying the ideas and the examples, not in surprise. For novels and memoirs, summaries do give away the story and remove most of the experience. Many clubs use summaries for nonfiction only and read fiction in full."),
        ("How long are Zehn summaries?",
         "Zehn summaries take 15 to 20 minutes per book and come in audio and text, with the text synced to the audio. The library has more than 10,000 books. That length makes it realistic for a busy member to catch up on the club's book during a commute or a lunch break before the meeting."),
        ("Is it fair if some members only read the summary?",
         "It's fair if the group agrees in advance. Many clubs say that coming prepared means reading the book or a summary, and that everyone is welcome regardless. Full readers can add examples the summary left out. The aim is a good conversation, and a member who stays in the club is better than one who quits."),
        ("Can a book club meet only inside an app?",
         "Yes. Some groups run entirely in an app: members post their thoughts, reply to each other and take part in challenges without a live meeting. It suits people in different time zones. Many clubs combine both: a feed during the month and a short video or in-person meeting at the end."),
    ],
    related=["how-to-start-a-book-club", "book-club-discussion-questions", "read-more-books"],
    cta=("Read the club's book in 15–20 minutes", "Zehn has 10,000+ book summaries in audio and text and a Book Club tab where readers post and reply. Free plan: 1 book a day."),
),
# ---------------------------------------------------------------- reading habits
"read-more-books": dict(
    cat="reading-habits",
    title="How to Read More Books When You Have No Time",
    desc="Practical ways to read more books with a busy schedule: small daily slots, audio on the move, quitting bad books and using summaries to choose.",
    h1="How to read more books when you have no time",
    lead="Most people who “don't have time to read” have 20–40 minutes a day in small pieces: commutes, queues, lunch breaks, the last minutes before sleep. Reading more is mostly about using those pieces on purpose and wasting fewer of them on books you don't enjoy.",
    tldr=["Find three small daily slots instead of waiting for a free evening.", "Use audio for the slots where your eyes are busy.", "Quit books that bore you and use summaries to decide what's worth a full read."],
    sections=[
        ("How can I read more books with a busy schedule?", [
            "Stop waiting for long free blocks and read in the small ones you already have. Fifteen minutes on the commute, ten at lunch and ten before bed add up to about four hours a week, enough for roughly one average nonfiction book. Keep a book, an e-reader or an audio app ready for each slot.",
        ]),
        ("Find your hidden reading time", [
            "For three days, note every gap of five minutes or more. Most people find more than they expect.",
            ("table", ["Moment", "Typical time", "Best format"], [
                ["Commute (bus, metro)", "15–40 min", "E-book or audio"],
                ["Driving, walking, gym", "15–60 min", "Audio only"],
                ["Lunch break", "10–20 min", "Paper or e-book"],
                ["Waiting (queues, appointments)", "5–15 min", "Phone e-book or summary"],
                ["Before sleep", "10–20 min", "Paper (no bright screen)"],
            ]),
        ]),
        ("Does listening count as reading?", [
            "For most nonfiction, listening and reading lead to similar understanding for general ideas; reading tends to win for dense, technical material you need to study. Treat audio as a way to turn dead time into reading time, not as a lesser version. Switch to text for books you want to underline and reread.",
        ]),
        ("Seven habits that add books to your year", [
            ("ol", ["**Always carry the next page.** Put your current book on your phone's home screen.", "**Read two books at once:** one demanding, one easy, so tiredness doesn't stop you.", "**Use the 50-page rule:** if a book hasn't earned your attention by page 50, quit it without guilt.", "**Pick shorter books** when life is busy; you can return to the 700-page classic later.", "**Replace one scroll session a day** with a chapter. Same phone, different app.", "**Track what you finish.** A simple list on your phone is motivating.", "**Talk about books.** A [book club](/en/guides/how-to-start-a-book-club/) or one friend who reads gives you a reason to finish."]),
        ]),
        ("Use summaries to choose, not to collect", [
            "A 15–20 minute summary is a fast way to decide whether a book deserves ten hours of your life. Many readers listen to a few summaries a week and pick one title to read in full. Summaries are also useful for books you only need the main ideas of. They are not the same as reading the whole book, so count them separately if you track your reading.",
            "This is how many people use Zehn: listen to summaries on the commute, then ask the book's [Ask AI](https://thezehnapp.com/en/ask-ai/) chat how one idea applies to their own situation.",
        ]),
        ("What should I do if I fall asleep reading?", [
            "Move your reading earlier. Bed is fine for light books but poor for demanding ones. Try reading the harder book on the commute or with your morning coffee and keep an easy novel for bedtime. If you read on a phone at night, lower the brightness and use a warm or dark mode.",
        ]),
    ],
    faq=[
        ("How many books can I read in 15 minutes a day?",
         "At an average reading speed of about 250 words per minute, 15 minutes a day is around 3,750 words, so roughly one 250-page book every four to five weeks, or about ten to twelve books a year. Adding audio during commutes or walks can easily double that without finding any new free time."),
        ("Is it OK to quit a book halfway?",
         "Yes. Quitting a book that bores you leaves time for one you'll enjoy and remember. Many keen readers use a rule like 50 pages or two chapters: if the book hasn't earned their attention by then, they stop. You can always come back later, when your interests or circumstances have changed."),
        ("Are book summaries a good way to read more?",
         "Summaries help you cover more ideas and choose better books, but they are not the same as reading the full book. Use them to screen titles, refresh a book you already read, or get the main ideas of books you only need for work. Read in full the books you care about most."),
        ("What is the best time of day to read?",
         "The best time is whenever you can protect it regularly. Mornings suit demanding books because your attention is fresh. Commutes suit audio. Evenings suit lighter reading, ideally on paper or with a dim screen. Linking reading to an existing habit, like the first coffee, makes it much easier to keep."),
    ],
    related=["remember-what-you-read", "52-books-a-year-reading-challenge", "book-club-with-summaries"],
),
"remember-what-you-read": dict(
    cat="reading-habits",
    title="How to Remember What You Read: 7 Proven Methods",
    desc="Why we forget books and seven methods that help you remember what you read: retrieval practice, spacing, notes, teaching and quizzing yourself with AI.",
    h1="How to remember what you read",
    lead="If you finish a book and can't explain it a month later, you're normal. Memory research has a clear answer to this: re-reading doesn't help much, but pulling the ideas back out of your head does. Here is how to do it in a few minutes per book.",
    tldr=["We forget most of what we read within days unless we use it.", "Testing yourself beats rereading; spread short reviews over weeks.", "Write three takeaways, explain one to someone, and quiz yourself with AI."],
    sections=[
        ("Why do I forget what I read?", [
            "Forgetting is the brain's default. In the 1880s Hermann Ebbinghaus showed that newly learned material fades fast in the first days and then more slowly. Reading feels like learning because the ideas make sense while you read them, but recognising an idea is not the same as being able to recall it later.",
        ]),
        ("What is the best way to remember a book?", [
            "Practise recalling it. In a well-known 2006 study, Roediger and Karpicke found that students who tested themselves remembered much more a week later than students who reread the same text. For books, that means closing the book and writing or saying what you remember, then checking what you missed.",
        ]),
        ("Seven methods that work", [
            ("ol", ["**Three-takeaway rule.** After each reading session, write three sentences from memory: what you learned, one example, and one question.", "**Spaced reviews.** Look at your takeaways again after one day, one week and one month. Each review takes two minutes.", "**Teach it.** Explain one idea to a friend, partner or colleague in under a minute. Gaps become obvious immediately.", "**Use it within 48 hours.** Turn one idea into an action: a new rule for your inbox, a question in a meeting.", "**Connect it.** Ask: which other book or experience does this agree or disagree with?", "**Take notes in your own words.** Copying quotes feels productive but is mostly recognition.", "**Quiz yourself with AI.** Ask an AI to test you on the book, then answer without looking."]),
        ]),
        ("How do I quiz myself on a book with AI?", [
            "Ask an AI chat to act as a strict teacher for the book and to give you one question at a time, waiting for your answer before giving feedback. Short, honest answers work best. Do this the day after you finish and again a week later; it takes five minutes and turns a passive read into active recall.",
            ("prompt", "I just finished [title] by [author]. Quiz me with 5 questions, one at a time, from easy to hard. Wait for my answer, then tell me what I got right, what I missed and one detail to remember."),
            ("prompt", "Here are my three takeaways from [title]: [takeaways]. What important idea did I miss, and how would I use each takeaway at [my job / in my life]?"),
            "In Zehn, every book page has an [Ask AI](https://thezehnapp.com/en/ask-ai/) chat that knows that book, so you can run this quiz right after listening to the summary. You can also use the [Science Explainer](/en/science-explainer/) coach for any topic.",
        ]),
        ("A simple note template", [
            ("table", ["Field", "Example"], [
                ["Book and date", "Deep Work, 12 March"],
                ["Main idea in one sentence", "Focused, distraction-free work produces more value than scattered busy work."],
                ["One example", "Block two 90-minute sessions without messages."],
                ["One action this week", "Phone in another room until 11:00."],
                ["One question", "How does this work in a job full of meetings?"],
            ]),
        ]),
        ("Do summaries help you remember?", [
            "They can, as a review tool. Reading or listening to a summary a week after finishing the book is a quick spaced review. Starting with a summary also gives you a map, so the details in the full book have somewhere to stick. A summary alone, without recall practice, fades just as fast as a book.",
        ]),
    ],
    faq=[
        ("How much of a book do people usually remember?",
         "There is no single number, because it depends on the book, the reader and what counts as remembering. What research consistently shows is that most new information fades quickly without review, and that testing yourself and spacing reviews over days and weeks greatly improves long-term memory compared with rereading."),
        ("Is highlighting a good way to remember?",
         "Highlighting on its own helps less than it feels, because it relies on recognition rather than recall. It is useful as a way to mark passages to return to. The memory benefit comes later, when you close the book and try to explain the highlighted ideas in your own words."),
        ("How long should I spend reviewing a book?",
         "A few minutes is enough: about five minutes right after finishing to write takeaways, then two minutes each after one day, one week and one month. That is under fifteen minutes in total for a book you spent hours on, and it makes the difference between forgetting it and actually using it."),
        ("Can AI help me remember books?",
         "Yes, as a quiz partner. Ask an AI to question you about a book one question at a time and to correct your answers. Check anything surprising against the book itself, since AI can be wrong about details. The value comes from you retrieving the ideas, not from the AI explaining them again."),
    ],
    related=["read-more-books", "52-books-a-year-reading-challenge", "book-club-discussion-questions"],
),
"52-books-a-year-reading-challenge": dict(
    cat="reading-habits",
    title="52 Books a Year Reading Challenge: Plan and Tracker",
    desc="Can you read 52 books in a year? The real maths, a weekly plan, a simple tracker and honest rules about audiobooks and summaries.",
    h1="The 52 books a year reading challenge",
    lead="A book a week sounds impossible until you do the maths. For many people it is about an hour a day, often less with audio. Here is how much time it really takes, a plan that survives busy weeks, and a tracker you can copy.",
    tldr=["52 average books is roughly 300–400 hours a year, about an hour a day.", "Mix lengths and formats, and plan for bad weeks from the start.", "Count full books and summaries separately, and set your own honest target."],
    sections=[
        ("How long does it take to read 52 books in a year?", [
            "An average nonfiction book has about 60,000–80,000 words. At 250 words per minute that is four to five and a half hours per book, so 52 books need roughly 220–290 hours of reading a year. That is about 40 to 50 minutes a day. Longer books, slower reading or notes push it towards an hour or more.",
        ]),
        ("Is 52 books a year the right goal for you?", [
            "Only if it makes you read more, not if it makes you choose short books you don't care about. Many people do better with 24 books (one every two weeks) or 12 books plus summaries. The right goal is the largest number you can reach without dreading your reading time.",
            ("table", ["Goal", "Books a month", "Time a day (approx.)"], [
                ["12 books", "1", "15–20 min"],
                ["24 books", "2", "25–35 min"],
                ["52 books", "4–5", "45–60 min"],
            ]),
        ]),
        ("A weekly plan that survives busy weeks", [
            ("ol", ["**Mon–Fri:** 20 minutes on the commute (audio or e-book) and 15 minutes before bed.", "**Saturday:** one longer session of 60–90 minutes to catch up.", "**Sunday:** finish, write three takeaways, choose next week's book.", "**Buffer:** plan for 46 books and treat the last six weeks as catch-up time."]),
            ("tip", "Keep one short book (under 200 pages) on standby for the weeks when life explodes. It keeps the streak alive without lowering your standards."),
        ]),
        ("Do audiobooks and summaries count?", [
            "Audiobooks of the full book count for most challengers: you're taking in the same text. Summaries are different: a 15–20 minute summary gives you the main ideas, not the book. A fair approach is to track them in two columns, “books” and “summaries”, and use summaries to choose which books to read in full.",
        ]),
        ("Copy this tracker", [
            ("table", ["#", "Title", "Format", "Pages / hours", "Finished on", "One takeaway"], [
                ["1", "", "Paper / e-book / audio", "", "", ""],
                ["2", "", "", "", "", ""],
                ["3", "", "", "", "", ""],
            ]),
            "Add a separate list for summaries with the same columns. At the end of each month, look at your takeaways and pick one to act on.",
        ]),
        ("How do I keep going after week 10?", [
            "Most challenges stall in the spring, when novelty is gone. Read with someone: a friend doing the same challenge, a [book club](/en/guides/how-to-start-a-book-club/), or a reading community. Reward streaks, not perfection. Choose at least one book a month purely for fun. And use what you read: [remembering it](/en/guides/remember-what-you-read/) makes the next book feel worth it.",
            "Zehn's daily streaks and topic clubs in the [Book Club tab](/en/zehn/book-club/) give the same push, and the free plan includes one book summary a day.",
        ]),
    ],
    faq=[
        ("Is reading 52 books a year realistic?",
         "For many adults, yes, if they read about 45 to 60 minutes a day and use audio during commutes or exercise. It is hard with long or technical books and a full-time job plus family. A goal of 24 books, or 12 books plus regular summaries, is more realistic for most people and still a big step up."),
        ("Do short books count in a reading challenge?",
         "It's your challenge, so you decide, but the most useful rule is to read what you would have read anyway and not pick books only because they are short. Mixing a few short books into busy months is fine. If every book is under 150 pages, the number grows but the benefit doesn't."),
        ("Should I count book summaries as books read?",
         "Most readers track summaries separately, because a 15 to 20 minute summary gives the main ideas but not the examples and depth of the full book. Summaries are still valuable: they help you choose which books to read in full and revisit books you already finished. Two columns keep the count honest."),
        ("What if I fall behind in the challenge?",
         "Don't try to catch up all at once. Pick one or two shorter books, add a weekend reading session, and lower the target if it has become a chore. The goal is to read more than last year and enjoy it. Falling behind in May is normal; quitting the whole habit is the only real failure."),
    ],
    related=["read-more-books", "remember-what-you-read", "how-to-start-a-book-club"],
),
# ---------------------------------------------------------------- learn with AI
"learn-a-language-with-ai": dict(
    cat="learn-with-ai",
    title="How to Learn a Language With an AI Tutor (2026 Guide)",
    desc="How to learn a language with an AI tutor: a daily 15-minute routine, the best prompts for speaking, writing and vocabulary, and what AI can't do for you.",
    h1="How to learn a language with an AI tutor",
    lead="AI tutors are patient, available at any hour and happy to correct the same mistake fifty times. They won't do the learning for you, but used well they give you something most learners never get: daily conversation practice at your level. Here is a routine that works.",
    tldr=["Use AI for practice and feedback; use real audio and people for listening and speaking.", "A daily 15-minute routine beats a weekly hour.", "Ask for corrections after each message and for words you'll actually use."],
    sections=[
        ("Can you really learn a language with AI?", [
            "AI can take you a long way in vocabulary, grammar and writing, and it is excellent conversation practice for beginners and intermediate learners who are shy or have no partner. You still need to hear real native speech and, eventually, talk to real people. Think of the AI tutor as your daily gym, not the whole sport.",
        ]),
        ("A 15-minute daily routine", [
            ("table", ["Minutes", "What to do", "Example prompt"], [
                ["0–3", "Review yesterday's 5 words", "“Quiz me on these words: …”"],
                ["3–10", "Short conversation on a real topic", "“Chat with me about my weekend, correct me after each message.”"],
                ["10–13", "Fix your mistakes", "“List my 3 most important mistakes and how to avoid them.”"],
                ["13–15", "Five new words for tomorrow", "“Give me 5 words I needed today, with examples.”"],
            ]),
        ]),
        ("The best prompts for language practice", [
            ("prompt", "Be my [language] tutor. My level is [level]; my native language is [language]. Chat with me about [topic] using short sentences. After each of my messages, correct my mistakes in one line, then continue the conversation."),
            ("prompt", "Role-play a [situation, e.g. job interview, doctor's appointment] in [language]. You are the [role]. Speak naturally but slowly, and wait for my answer."),
            ("prompt", "Correct this text and explain each mistake in one short sentence. Then rewrite it the way a native speaker would: [text]"),
            ("prompt", "Make a list of the 20 words I need most for [my job / my trip / my exam], with an example sentence for each, then quiz me on 5 of them."),
            "More ready-made prompts are on our [AI Language Tutor](/en/language-tutor/) page.",
        ]),
        ("How do I practise speaking with AI?", [
            "Read every reply out loud, and repeat each corrected sentence two or three times. If your chat app has a microphone button, dictate your answers instead of typing: it forces you to produce the sounds and shows you which words the app can't understand. Record yourself once a week to hear progress.",
        ]),
        ("What can't an AI tutor do?", [
            ("ul", ["**Hear your real pronunciation the way a teacher does.** Dictation helps, but a human ear is better.", "**Guarantee correctness.** AI can make mistakes, especially with rare words, slang and dialects. Check surprising claims.", "**Keep you motivated.** Streaks, a study buddy or a class help more than any app.", "**Replace real listening.** Podcasts, films and audiobooks train your ear for real speed and accents."]),
        ]),
        ("Combine the tutor with reading and listening", [
            "Listening to short, interesting content in your target language is one of the most effective ways to grow vocabulary. Book summaries are a good fit: 15–20 minutes, clear language, topics you care about. In Zehn you can listen to a summary in one language with synced text, then ask the Language Tutor coach in the AI Chat tab about the words you didn't know.",
        ]),
    ],
    faq=[
        ("Is an AI tutor better than a human teacher?",
         "They do different jobs. An AI tutor is cheaper, always available and endlessly patient, which makes it ideal for daily practice and corrections. A good human teacher notices pronunciation problems, plans your learning, keeps you accountable and understands culture and context. Many learners get the best results by combining a weekly class with daily AI practice."),
        ("How long does it take to learn a language with AI?",
         "It depends on the language, your native language and your daily time, not on the tool. Reaching basic conversation usually takes several months of regular practice. AI can speed up the parts that need repetition and feedback, such as vocabulary and writing, if you practise every day and also listen to real speakers."),
        ("Which AI model is best for learning languages?",
         "Most modern models handle widely spoken languages well. Differences show up in tone, explanation style and rare languages or dialects. The practical test is to give two models the same prompt and keep the one whose corrections you understand best. Our [comparison of Claude, Gemini, DeepSeek and Grok for learning](/en/guides/claude-vs-gemini-vs-deepseek-vs-grok/) covers how to test them."),
        ("Can AI help me learn English for work?",
         "Yes. Ask the tutor to role-play the situations you face at work, such as meetings, emails, calls with clients or a job interview, and to correct you after each message. Ask for vocabulary from your field with example sentences. Practise a few minutes every day and save the corrected phrases to review later."),
    ],
    related=["claude-vs-gemini-vs-deepseek-vs-grok", "remember-what-you-read", "read-more-books"],
),
"claude-vs-gemini-vs-deepseek-vs-grok": dict(
    cat="learn-with-ai",
    title="Claude vs Gemini vs DeepSeek vs Grok for Learning",
    desc="Which AI model is best for learning? Claude, Gemini, DeepSeek and Grok compared for explanations, languages, maths and study, and how to test them.",
    h1="Claude vs Gemini vs DeepSeek vs Grok for learning",
    lead="There is no single “best” AI model for learning. The four big names are all capable, and they keep changing every few months. What differs is how they explain, how they sound and how they handle your particular subject. Here is a fair way to compare them for your own learning.",
    tldr=["All four can explain, quiz and correct you well; differences are about style and specific tasks.", "Test them with the same prompt on a topic you already know.", "Use two models on important questions and check facts in a trusted source."],
    sections=[
        ("Which AI is best for learning?", [
            "The best model is the one whose explanations you understand and can check. For most students and self-learners, any of Claude, Gemini, DeepSeek or Grok will explain a concept, write practice questions and correct an essay well. Run the same prompt through two of them and compare clarity, accuracy and how well they adapt to your level.",
        ]),
        ("A quick overview", [
            "Model makers update their models often, so treat this as a starting point (November 2026), not a ranking.",
            ("table", ["Model", "Made by", "Often chosen for", "Watch out for"], [
                ["Claude", "Anthropic", "Clear, careful long explanations; writing feedback; step-by-step reasoning", "Can be cautious or long; ask for a shorter answer"],
                ["Gemini", "Google", "Broad general knowledge; mixing text with images in Google's apps", "Check details of very recent facts"],
                ["DeepSeek", "DeepSeek (China)", "Maths and coding practice; step-by-step problem solving", "Style can be terse; ask for more examples"],
                ["Grok", "xAI", "A casual, direct conversation style; quick back-and-forth", "Tone may not suit every topic; ask it to be neutral"],
            ]),
            ("tip", "Inside a third-party app, a model may behave differently from its maker's own app (for example web search or file uploads may not be available). Judge the answers you actually get."),
        ]),
        ("How do I test AI models for my subject?", [
            ("ol", ["**Pick a topic you already know well.** You can only judge accuracy where you know the answer.", "**Use one identical prompt** for every model, including your level and the format you want.", "**Score four things from 1–5:** accuracy, clarity, fit to your level, and useful follow-up questions.", "**Ask a follow-up that tests understanding**, such as “Where does this explanation break down?”", "**Repeat with your real study topic** and keep the model that won both rounds."]),
            ("prompt", "Explain [topic] for someone at [level]. Use one everyday analogy, then 3 key points, then 2 questions to check my understanding. Keep it under 200 words."),
        ]),
        ("Which model for which task?", [
            ("table", ["Task", "What to ask", "Tip"], [
                ["Understanding a concept", "Explain simply, then in more depth", "Compare two models' analogies"],
                ["Language practice", "Chat and correct me after each message", "Pick the model whose corrections you understand"],
                ["Maths and logic", "Solve step by step, then give me a similar problem", "Ask it to check its own answer"],
                ["Essay feedback", "Point out the 3 biggest weaknesses", "Never submit AI-written text as your own"],
                ["Exam revision", "Quiz me one question at a time", "Answer without looking; then check notes"],
            ]),
        ]),
        ("Can I trust what AI tells me when I study?", [
            "Mostly for well-established basics, less for numbers, recent research and niche topics. All models can state something wrong with total confidence. Ask for reasoning and sources, cross-check important facts in a textbook or official site, and be extra careful with health, law and money. Using two models on the same question catches many errors.",
        ]),
        ("Using all four in one place", [
            "Switching between four different apps is tiring. Zehn's AI Chat tab has a model picker at the top, so you can ask the same question to Claude, Gemini, DeepSeek or Grok and compare. The yearly plan includes all four models; the monthly plan includes the AI Chat with one model. The same chat also has coaching personas like the [Language Tutor](/en/language-tutor/) and the [Science Explainer](/en/science-explainer/).",
            ("ui", "chat"),
        ]),
    ],
    faq=[
        ("Is Claude or Gemini better for students?",
         "Both are strong for students. Many people like Claude's careful, structured explanations and writing feedback, while Gemini is popular for broad general knowledge and inside Google's apps. The honest answer is to test both on a topic you know with the same prompt and keep the one whose answers are clearest and most accurate for you."),
        ("Is DeepSeek good for learning maths?",
         "DeepSeek is widely used for maths, logic and coding practice because it works through problems step by step. Like any model, it can make mistakes, so ask it to check its own answer or verify with a second model. For learning, ask for a similar practice problem after each solution rather than only reading answers."),
        ("Can I use AI for homework without cheating?",
         "Yes, if you use it as a tutor rather than a ghostwriter. Ask it to explain concepts, quiz you, check your reasoning and point out weaknesses, then write the answers yourself. Follow your school's rules on AI, and never submit AI-generated text as your own work. Learning happens when you do the thinking."),
        ("Which AI models does the Zehn app include?",
         "The Zehn AI Chat tab has a model picker with Claude, Gemini, DeepSeek and Grok. The yearly plan, $36 a year with a 7-day free trial, includes all four. The monthly plan, $9.99 a month, includes the AI Chat with one model. The free plan includes one book summary a day without AI features."),
    ],
    related=["learn-a-language-with-ai", "remember-what-you-read", "read-more-books"],
),
}

# ---------------------------------------------------------------- Zehn guides (served under /zehn/)
ZEHN = {
"what-is-zehn": dict(
    cat="zehn-guides", path="zehn/",
    title="What Is Zehn? The Book Summary App With AI, Explained",
    desc="What Zehn is, who makes it and what it does: 15–20 minute book summaries, Ask AI on every book, an AI Chat with coaches, Book Club, languages and plans.",
    h1="What is Zehn?",
    lead="Zehn (pronounced “Zen”) is a book-summary app with built-in AI. You listen to or read the key ideas of a nonfiction book in 15–20 minutes, ask an AI questions about that book, and talk to AI coaches about your own problems. It is made by Safari Group, a company founded in Dubai in 2005.",
    tldr=["Zehn: 10,000+ book summaries of 15–20 minutes, in audio and text, for iPhone and Android.", "AI features: Ask AI on every book, and an AI Chat tab with nine coaches and a choice of four models.", "Free plan: 1 book a day without AI; Zehn Pro: $9.99/month or $36/year with a 7-day free trial."],
    sections=[
        ("What does the Zehn app do?", [
            "Zehn turns nonfiction books into 15–20 minute summaries you can read or listen to, with the text synced to the audio. Each book has an Ask AI chat that knows that book. A separate AI Chat tab offers nine coaching personas, and a Book Club tab lets readers discuss books in topic clubs.",
        ]),
        ("Zehn at a glance", [
            ("table", ["", "Zehn"], [
                ["What it is", "Book-summary app with AI features"],
                ["Library", "10,000+ books, mostly nonfiction"],
                ["Length", "15–20 minutes a book, audio and synced text"],
                ["AI", "Ask AI on every book; AI Chat with 9 coaches; models: Claude, Gemini, DeepSeek, Grok"],
                ["Community", "Book Club tab with topic clubs, posts and challenges"],
                ["Platforms", "iPhone (App Store) and Android (Google Play)"],
                ["Made by", "Safari Group, founded in Dubai in 2005"],
                ["Readers", "50,000+"],
            ]),
        ]),
        ("Who is Zehn for?", [
            "Zehn is built for people who want the ideas from good books but have little time, and especially for readers who prefer their own language. Many book-summary apps focus on English; Zehn's library and app experience are built for non-English speakers too, including Russian and Arabic readers, with Arabic narration in Modern Standard Arabic.",
        ]),
        ("What can you do with Ask AI and the AI Chat?", [
            ("ul", ["**Ask AI (on every book):** ask how an idea applies to your job, get an example, or have it quiz you on the book.", "**AI Chat tab:** general AI chat with a model picker at the top, for everyday questions.", "**Nine coaches in the AI Chat:** [Business Mentor](/en/business-mentor/), [Money Coach](/en/money-coach/), [Productivity Coach](/en/productivity-coach/), [Mindfulness Guide](/en/mindfulness-guide/), [Psychologist](/en/psychologist/), [Negotiator](/en/negotiator/), [Language Tutor](/en/language-tutor/), [Leadership Mentor](/en/leadership-mentor/) and [Science Explainer](/en/science-explainer/)."]),
            ("ui", "chat"),
        ]),
        ("How much does Zehn cost?", [
            "Zehn has a free plan and a paid plan called Zehn Pro. Prices can vary by country, as Zehn uses regional pricing in 30+ countries; the standard prices are below.",
            ("table", ["Plan", "Price", "What you get"], [
                ["Free", "$0", "1 book summary a day, no AI"],
                ["Pro monthly", "$9.99/month", "Unlimited books, offline listening, Ask AI, AI Chat with 1 model"],
                ["Pro yearly", "$36/year, 7-day free trial", "Unlimited books, offline listening, Ask AI, AI Chat with all 4 models"],
            ]),
        ]),
        ("How is Zehn different from other summary apps?", [
            "Two things stand out: it is built for non-English speakers as well as English ones, and AI is part of every book rather than a separate add-on. A detailed comparison with Blinkist and Headway lives on Zehn's own website. Zehn also has a Book Club tab, daily streaks and a dark mode.",
        ]),
        ("How do I get started?", [
            ("ol", ["Download Zehn from the App Store or Google Play.", "Pick your language and a few topics you care about.", "Listen to your first 15–20 minute summary on the free plan.", "If you want the AI features, start the 7-day free trial of the yearly plan."]),
            "Zehn's website is [thezehnapp.com](https://thezehnapp.com/en/).",
        ]),
    ],
    faq=[
        ("How do you pronounce Zehn?",
         "Zehn is pronounced like “Zen”. The name is written Zehn in Latin letters in every language, and in Arabic it is written زن. It is the name of the book-summary app made by Safari Group, and of its website, thezehnapp.com. Intellect AI, this site, is a free AI-coach guide made by the same team."),
        ("Is Zehn free?",
         "Zehn has a free forever plan with one book summary a day and no AI features. Zehn Pro unlocks unlimited books, offline listening and the AI features. It costs $9.99 a month with the AI Chat on one model, or $36 a year with all four models and a 7-day free trial. Prices may vary by country."),
        ("Who makes Zehn?",
         "Zehn is made by Safari Group, a company founded in 2005 in Dubai, United Arab Emirates. The founder is Muhammad Safarzoda. Safari Group also runs Intellect AI, this free guide to AI coaching, which is a separate website with its own content and links to the Zehn app."),
        ("What languages is Zehn available in?",
         "Zehn's library includes book summaries in several languages, including English, Russian, Arabic, Hindi and Urdu, and the app is designed for non-English speakers as well as English ones. Arabic summaries are narrated in Modern Standard Arabic. The AI features answer in the language you write in."),
    ],
    related=["how-zehn-makes-your-day-easier", "zehn-book-club", "read-more-books"],
    cta=("Get Zehn", "Free plan: 1 book a day. Zehn Pro: $9.99/month or $36/year with a 7-day free trial."),
),
"how-zehn-makes-your-day-easier": dict(
    cat="zehn-guides", path="zehn/daily/",
    title="How Zehn Makes Your Day Easier: 7 Real Moments",
    desc="Seven everyday moments where Zehn helps: the commute, lunch, a meeting, a hard conversation, language practice, Sunday planning and winding down.",
    h1="How Zehn makes your day easier",
    lead="Apps promise to change your life; this page is more modest. Here are seven ordinary moments in a day where Zehn's summaries, Ask AI and AI coaches save time or make something easier, with exactly what to tap and what to type.",
    tldr=["Turn dead time (commute, queue) into one 15–20 minute book.", "Use Ask AI to apply one idea to your real situation.", "Use the AI coaches for meetings, money, languages and calm."],
    sections=[
        ("1. The commute: one book, door to door", [
            "A 15–20 minute summary fits a typical bus or metro ride. Pick a book in the morning, listen on the way and arrive with one new idea. Offline listening on the paid plan helps on the underground. On the free plan you get one book a day, which is exactly one commute.",
            ("tip", "Keep the text open while you listen. The synced text highlights along with the audio, which helps if the book is in a language you're learning."),
        ]),
        ("2. Lunch break: apply one idea to your job", [
            "Open the book you listened to and tap Ask AI. It knows that book, so you can ask how a specific idea applies to your situation.",
            ("prompt", "I work as [job]. Which idea from this book could I try this week, and what would the first step be?"),
        ]),
        ("3. Before a meeting: five minutes with the Negotiator", [
            "Asking for a raise, a discount or a deadline change? Open the AI Chat tab, pick the Negotiator and rehearse. Ask it to play the other side and push back, then give you feedback. More prompts on the [AI Negotiator](/en/negotiator/) page.",
        ]),
        ("4. After a hard conversation: think it through", [
            "When a talk with a colleague or family member went badly, the Psychologist persona can help you put it into words and plan what to say next. It is a self-help tool, not therapy; for anything serious, talk to a professional, and in an emergency call your local emergency number. See the [Psychologist persona](/en/psychologist/) page.",
        ]),
        ("5. Evening: ten minutes of language practice", [
            "Pick the Language Tutor and chat about your day in the language you're learning, asking for corrections after each message. Ten minutes a day adds up. Our guide on [learning a language with AI](/en/guides/learn-a-language-with-ai/) has a full routine.",
        ]),
        ("6. Sunday: plan the week and the money", [
            ("ul", ["**Productivity Coach:** paste everything on your mind and ask for this week's three priorities and two focus blocks.", "**Money Coach:** check the week's spending against your budget and plan one small saving. Not financial advice; check big decisions with a professional."]),
        ]),
        ("7. Before sleep: wind down", [
            "Swap the last scroll for a short practice with the Mindfulness Guide (a 5-minute body scan works well), or post your thoughts on the day's book in a [Book Club](/en/zehn/book-club/) topic club. Dark mode keeps the screen gentle at night.",
        ]),
        ("What a full day looks like", [
            ("table", ["Time", "Moment", "Zehn feature", "Minutes"], [
                ["08:00", "Commute", "Book summary (audio)", "15–20"],
                ["13:00", "Lunch", "Ask AI on the book", "5"],
                ["16:30", "Before a meeting", "AI Chat: Negotiator", "5"],
                ["20:00", "Evening", "AI Chat: Language Tutor", "10"],
                ["22:30", "Bedtime", "Mindfulness Guide or Book Club", "5"],
            ]),
            "About 40 minutes, most of it in time you would otherwise lose. You don't need all of it; one moment a day is a good start.",
        ]),
    ],
    faq=[
        ("Do I need the paid plan for these moments?",
         "The commute moment works on the free plan, which includes one book summary a day. Ask AI and the AI Chat coaches need Zehn Pro: $9.99 a month with the AI Chat on one model, or $36 a year with all four models and a 7-day free trial. Offline listening is also part of the paid plans."),
        ("How long does each Zehn summary take?",
         "Each Zehn summary takes 15 to 20 minutes and comes in audio and text, with the text synced to the audio. That length fits most commutes, a walk or a lunch break. The library has more than 10,000 books, so there is usually a summary for whatever problem you're working on that week."),
        ("Which AI coach should I start with?",
         "Start with the coach that matches your most annoying problem this week. If your days feel chaotic, try the Productivity Coach. If money is stressful, the Money Coach. If you have a difficult talk coming up, the Negotiator. Each coach page on this site has twelve prompts you can copy straight into the AI Chat."),
        ("Can I use Zehn in my own language?",
         "Yes. Zehn is designed for non-English speakers as well as English ones, with book summaries in several languages including English, Russian, Arabic, Hindi and Urdu. The AI features reply in the language you write in, so you can talk to the coaches in Russian, Arabic or English."),
    ],
    related=["what-is-zehn", "zehn-book-club", "read-more-books"],
),
"zehn-book-club": dict(
    cat="zehn-guides", path="zehn/book-club/",
    title="Zehn Book Club: Topic Clubs, Posts and Challenges",
    desc="How the Book Club tab in the Zehn app works: join topic clubs, post your take on a book, reply to other readers and take part in club challenges.",
    h1="The Zehn Book Club, explained",
    lead="Book Club is one of the five tabs in the Zehn app. Instead of meeting on a fixed date, readers join topic clubs and talk in a feed: you post your take on a book or simply what's on your mind, others reply in the comments, and clubs run challenges.",
    tldr=["Join topic clubs, such as Calm Club in Mindfulness & Happiness.", "Post your take on a book, reply to others and take club challenges.", "Each club has its own description and rules; read them before posting."],
    sections=[
        ("What is the Zehn Book Club?", [
            "The Zehn Book Club is a tab in the Zehn app where readers discuss books in topic clubs. Each club has a theme, a short description, its own rules, a “What's on your mind today?” box for new posts, and Posts and Challenges tabs. It works like a small, focused social feed about books.",
            ("ui", "club"),
        ]),
        ("How do I join a club and post?", [
            ("ol", ["Open the Zehn app and tap the **Book Club** tab at the bottom.", "Browse the topic clubs and open one that fits you (for example Calm Club).", "Read the club's description and rules.", "Tap **What's on your mind today?**, give your post a title and write your take.", "Reply to other members' posts in the comments.", "Open **Challenges** to see what the club is working on."]),
        ]),
        ("What should I post?", [
            "The best posts are short and specific: one idea from a book, why you agree or disagree, and a question for others. You don't have to post about books only; clubs are also a place to just talk about the club's theme. Keep to the club's rules and be kind in replies.",
            ("ul", ["“I tried the 2-minute rule from a habits book for a week. Here's what happened…”", "“Is this book's advice realistic for parents with small kids?”", "“One line from today's summary that I can't stop thinking about.”"]),
        ]),
        ("What are club challenges?", [
            "Challenges give a club a shared goal, such as reading on certain topics or trying an idea for a few days, so members have a reason to come back and post. Open the Challenges tab in a club to see what's running. Each club also has a leaderboard, shown by the trophy icon at the top.",
        ]),
        ("How is it different from a classic book club?", [
            ("table", ["", "Classic book club", "Zehn Book Club"], [
                ["When", "A fixed meeting, often monthly", "Any time, in a feed"],
                ["Who", "Friends or a local group", "Readers interested in the same topic"],
                ["Format", "Live conversation", "Posts, comments and challenges"],
                ["Preparation", "Read the whole book", "Read the book or its 15–20 min summary"],
            ]),
            "Many people use both: a club in the app for everyday discussion, and a live group for deeper monthly talks. Our guide on [running a book club with summaries](/en/guides/book-club-with-summaries/) shows how to combine them.",
        ]),
        ("Club etiquette", [
            ("ul", ["Read the club rules before your first post.", "Disagree with ideas, not people.", "Mark big spoilers if you post about a novel.", "Don't share personal data such as phone numbers or addresses in posts."]),
        ]),
    ],
    faq=[
        ("Is the Zehn Book Club free?",
         "The Book Club is a tab inside the Zehn app, which has a free plan with one book summary a day. For the current access rules for posting and challenges, check the app itself. The paid Zehn Pro plan adds unlimited books, offline listening and the AI features, and costs $9.99 a month or $36 a year."),
        ("Can I talk about things other than books?",
         "Yes. Clubs are organised around topics, such as mindfulness and happiness, so members also talk about the topic itself, not only specific books. Each club has its own description and rules, which describe what fits. When in doubt, connect your post to an idea from a book or ask a question others can answer."),
        ("What are Zehn club challenges?",
         "Challenges are shared goals inside a club that give members a reason to read and post, for example around a topic or an idea to try. You find them in the Challenges tab of each club, next to the Posts tab. Each club also has a leaderboard, opened with the trophy icon at the top."),
        ("Do I need to finish a book before posting?",
         "No. Many members post after listening to the 15 to 20 minute summary, and some post while they are still reading. Say how far you got so others know what to expect. Questions and half-formed thoughts are welcome; they often start the most useful conversations in a club."),
    ],
    related=["book-club-with-summaries", "how-to-start-a-book-club", "what-is-zehn"],
    cta=("Join a club in the Zehn app", "Download Zehn, open the Book Club tab and pick a topic club. Free plan: 1 book a day."),
),
}

ABOUT = dict(
    title="About Intellect AI: Free AI Coach Guides by Zehn",
    desc="Intellect AI is a free guide to AI coaches, reading and learning with AI, made by the team behind the Zehn book-summary app (Safari Group, Dubai).",
    h1="About Intellect AI",
    tldr=["Intellect AI is a free guide to AI coaching, reading habits and learning with AI.", "It is made by the team behind Zehn, a book-summary app by Safari Group.", "No accounts, no ads, no tracking cookies."],
    body=[
        ("What is Intellect AI?", "Intellect AI is a free website with guides, copy-ready prompts and example conversations for nine AI coaches, plus practical guides on reading, book clubs and learning with AI. Everything on the site is free to read and use, and the prompts work in any AI chat."),
        ("Who makes it?", "Intellect AI is made by the team behind Zehn, a book-summary app with 10,000+ books, Ask AI on every book and an AI Chat with nine coaching personas. Both are projects of Safari Group, a company founded in Dubai in 2005. The founder is Muhammad Safarzoda."),
        ("How we write", "We write original guides for people, not search engines. We only state facts we can stand behind, label example conversations as examples, and say clearly where AI is not a substitute for a professional: health, mental health, law and large money decisions. When we mention Zehn, we say so."),
        ("Contact", "Questions, corrections or ideas for a guide: contact@safarigrp.com."),
    ],
)

QUIZ = dict(
    title="What Should I Read Next? Free 30-Second Book Quiz",
    desc="Answer three quick questions and get three nonfiction book picks that fit your goal and mood, each with a 15–20 minute summary in the Zehn app.",
    h1="What should I read next?",
    lead="Three quick questions, three book picks. No sign-up, nothing is sent anywhere: the quiz runs in your browser.",
    tldr=["Answer 3 questions about your goal, mood and time.", "Get 3 real nonfiction books that fit, with their summary length.", "Each pick links to its summary on Zehn."],
    q1="What do you want from your next book?",
    goals=[("focus", "Get more done, focus better"), ("money", "Sort out my money"), ("calm", "Feel calmer"), ("people", "Handle people and conversations"),
           ("business", "Start or grow a business"), ("lead", "Lead a team"), ("mind", "Understand myself"), ("science", "Understand how the world works")],
    q2="How do you feel about reading right now?",
    moods=[("light", "Give me something easy to start"), ("deep", "I'm ready for something deep")],
    q3="When will you read or listen?",
    times=[("commute", "On the commute"), ("evening", "In the evening"), ("weekend", "At the weekend")],
    show="Show my books", again="Start again",
    result_h="Your next reads",
    tip_commute="Tip: listen to the summary on your way in, then read the full book if it grabs you.",
    tip_evening="Tip: read the text version in the evening with dark mode on.",
    tip_weekend="Tip: start with the summary, then use the weekend for the full book.",
    open="Open summary", minutes="{n} min summary",
    more_h="Why these books?",
    more_p="Picks come from Zehn's library and match the goal you chose. Easy picks start with the shortest summaries. Summaries take 15–20 minutes; Ask AI on each book can tell you how an idea applies to you.",
    faq=[
        ("How does the book quiz choose books?",
         "The quiz matches your main goal to a topic in Zehn's library, such as productivity, money or psychology, and shows three well-known nonfiction books from that topic. If you want something easy, it starts with the shortest summaries. Everything runs in your browser, and nothing you choose is stored or sent anywhere."),
        ("Are the recommended books available in Zehn?",
         "Yes. Every book the quiz suggests is in Zehn's library, and each result links to the book's page on thezehnapp.com, where you can see the summary length and author. Zehn summaries take 15 to 20 minutes, in audio and text. The free plan includes one book summary a day."),
        ("Should I read the summary or the full book?",
         "Start with the 15 to 20 minute summary to see whether the book's ideas speak to you. If they do, read or listen to the full book for the examples and depth a summary can't include. Summaries are a good filter, and a good refresher after you finish a book."),
    ],
)
