"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

# ── Criterion 1: my own writing ──────────────────────────────────────────────
# Seven pieces I wrote myself (school essays, a personal statement, a proposal,
# a résumé summary). Pasted as written — typos and all.

MY_WRITING = [
    """The fish caught by Messrs. Sauvage and Morrisot can be interpreted as a symbol of innocent people killed or suffered in the wars. The two friends versus the bag of fish is like the soldiers who participate in the war versus the implicated people. After the two friends who get caught while fishing are killed, the Prussian officer demanded the soldiers to cook the fish. Similarly, when a war happens, innocent soldiers die in the battles and the family of the soldiers or the implicated people also suffer.""",
    """I consider him to be a cruel character because he tells jokes which might hurt others’ feelings or trigger disputes of others to entertain himself. It seems like he keeps hurting others’ dignity and doesn’t care to harm them. For example, he writes a postcard to a husband with words which might makes the husband question his wife’s loyalty. Absolutely, making mischief between a couple is not humorous at all. In addition, Jim usually fools around Paul Dickson, the poor guy who harmed his head by falling out a tree at the age of ten. Jim never thinks about his feelings, and keeps teasing at him and playing jokes on him.""",
    """Reality television should not be banned. One of the reasons is that there are many people watching it, which makes it commercially successful. Also, banning reality television is like restricting the freedom and the right of the people, which might triggers discontent and dispute. Moreover, the reality television sometimes acts as the reflection of real life and probably provides a function of caution.""",
    """The experience sparked my interest in getting involved in various activities later in high school. The experience of founding and leading the swimming club and the rock band, the team speech competition, and several clubs in which I had never thought I would have joined, all taught me crucial life lessons. Express yourself to gain assistance through sharing and building relationship. Think independently because opportunity comes when you are brave enough to venture upon a new undertaking.""",
    """To resist fear of failure, embrace your weaknesses and always remind yourself of your strengths. In that way, you know what you should work on to improve and what traits of you make you possess the potential. I appreciate these experiences along the journey. “You are the creator of your own journey”. This is no longer merely a quote that appears on a photo of beautiful coastline, but a compass that will guide me to pursue my next great journey.""",
    """Ideally, a student lounge includes one or two sofas. It would also be good to have a refrigerator or cupboard where students can temporarily store their food. We should also have a clock so students can always check the time and make sure they have enough time to go to the next class. Since there’s no water dispenser on the first floor of K building and it is a student lounge, it will also be nice to have a water dispenser in the lounge. There is already a sofa in the senior lounge region of student lounge, and I think it would be more convenient if there’s a small coffee table in front of the sofa. We can also buy some plants for decoration. I believe that would make the atmosphere more relaxed and more like an actual lounge.""",
    """During my internship at Brilltek, a Taiwanese company specializing in automation and enterprise resource planning, I focused on developing the backend and frontend of web apps using JavaScript and Preact, a framework built on top of React. These apps served as integrated platforms for managing business resources, allowing clients and their customers to manage their product lines, machines, etc., in real-time, as well as tracking the progress of their employees and upstream suppliers. Working in a smaller company provided me with opportunities to work cross-functionally on different projects, strengthening my communication, time management, teamwork, and adaptability skills. Aside from web development, I have also collaborated with my friends to design and implement an Android app using Figma and Kotlin, aiming to facilitate meal prep and reduce food waste through recipe searching/saving and ingredient management by keeping track of the expiration dates.""",
]


# ── Criterion 2: clearly-AI samples ──────────────────────────────────────────
# Generated by an AI assistant (Claude) from one-line prompts like "write a
# paragraph about remote work". Unedited.

AI_TEXTS = [
    """Remote work has fundamentally reshaped the modern workplace, offering employees greater flexibility and autonomy while presenting new challenges for organizations. By eliminating daily commutes, remote work can improve work-life balance and boost overall productivity. However, it also requires clear communication, reliable technology, and intentional efforts to maintain team cohesion. As companies continue to adapt, hybrid models that combine the benefits of in-person collaboration with the flexibility of remote work are emerging as a popular and effective solution.""",
    """Regular physical activity is one of the most important things people can do to improve their overall health and well-being. Exercise strengthens the heart, improves circulation, and helps maintain a healthy weight. In addition to its physical benefits, it also plays a crucial role in supporting mental health by reducing stress, anxiety, and symptoms of depression. Experts recommend at least 150 minutes of moderate aerobic activity each week, combined with strength training exercises on two or more days.""",
    """Climate change represents one of the most pressing challenges facing humanity in the twenty-first century. Rising global temperatures, driven primarily by the burning of fossil fuels, are contributing to more frequent extreme weather events, rising sea levels, and significant disruptions to ecosystems. Addressing this complex issue requires a coordinated global effort, including transitioning to renewable energy sources, improving energy efficiency, and implementing policies that encourage sustainable practices across all sectors of society.""",
    """Reading offers numerous benefits that extend far beyond simple entertainment. It enhances vocabulary, improves concentration, and stimulates critical thinking skills. Furthermore, reading fiction has been shown to increase empathy by allowing readers to experience the world from different perspectives. Whether through traditional books, e-readers, or audiobooks, cultivating a consistent reading habit can contribute significantly to personal growth, lifelong learning, and overall cognitive health.""",
    """Effective time management is an essential skill for achieving both personal and professional success. By prioritizing tasks, setting clear goals, and minimizing distractions, individuals can maximize their productivity and reduce stress. Techniques such as the Pomodoro method, time blocking, and maintaining a daily to-do list can help people stay organized and focused. Ultimately, mastering time management allows individuals to make the most of their time and maintain a healthier work-life balance.""",
]


# ── Criterion 2: clearly-human samples ───────────────────────────────────────
# Five posts from online forums, written by other people (not me), so criteria
# 1 and 2 don’t share data. Casual, personal, and pasted as written.

HUMAN_TEXTS = [
    """This is a really helpful insight and it’s also applicable to other things. I go to the gym very frequently (in the evening no less) but do not dedicate any will power to it. The way I frame it in my mind is that I “get” to go to the gym, not I “have” to go to the gym. Have you noticed how you miss breathing through your nose when you are congested? We often don’t realize that our health/youth allows us the freedom to move our bodies and to physically challenge ourselves. Don’t wait until your knees, hips, back, etc prohibit you from moving freely.""",
    """Just an FYI, this isn’t specifically scientifically supported but more of a very general guideline. A habit can take anywhere from two weeks to 60+ days to build, depending on its complexity. Some habits are much simpler and capable of being done much faster.""",
    """I am an emotional person by nature; however, I’m working on creating tougher skin. This is what brings me here. If you are/have been a teaching assistant in a STEM related class, have you ever had students complain about your grading style/rubric? If so, what do you do to not take it personally?

For context, I graded an exam and I was very satisfied with how I graded. I triple checked every exam to be as consistent as possible. Of course, some students still had something to say (funny enough, these are the ones that scored the highest, too). It’s so frustrating. I feel like I can’t do anything right!! I want to be a professor so bad so I want to get this quirk smoothed out as soon as possible…""",
    """I am so broke. I have a work study job and I'm interviewing for another part time job, but I only got $4k for the semester in loans after it went to tuition and stuff. I've never been more broke in my life - not even when I did AmeriCorps.

I want to get on food stamps but I'm so ashamed to. Has anyone else here gone on food stamps to get through grad school?""",
    """So I think it would be useful to better understand economics. I like social sciences.

To the point, I want to get a solid to intermediate understanding of how things like stocks, money, socio-economic systems, "work", + basics in economic theory. Going to school is not an option for me for the foreseeable future.

I ' m looking for book lists/resource lists, free courses/classes, specific and general subjects, videos, open source studies, anything. Also perhaps advice on order in which to learn.

Thanks all""",
]


SCENARIOS = [
    {"name": "c1 own writing", "criterion": 1, "texts": MY_WRITING},
    {"name": "c2 spread AI", "criterion": 2, "texts": AI_TEXTS},
    {"name": "c2 spread human", "criterion": 2, "texts": HUMAN_TEXTS},
    {
        # 12 samples across the range: the 5 AI, the 5 human, and 2 of my more
        # formal pieces (the lounge proposal and the internship summary), which
        # I expect to land in between.
        "name": "c3 label coverage",
        "criterion": 3,
        "texts": AI_TEXTS + HUMAN_TEXTS + MY_WRITING[5:7],
    },
    # Criterion 4 (appeals) can't be tested by sending text alone — it needs a
    # submission and then an appeal on the content_id that came back. That's
    # run_appeals.py.
    {
        "name": "c5 bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},                   # no text field
            {"text": "", "creator_id": "eval_bad_empty"},         # empty text
            {"text": "a" * 100000, "creator_id": "eval_bad_huge"},  # 100,000 chars
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
