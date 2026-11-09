# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 23:18:22 2026

@author: nikun
"""

import streamlit as st

"""
From Goa to Ames
A personal narrative multimodal remix built with Python and Streamlit.


"""

from pathlib import Path
import streamlit as st

# ------------------------------------------------------------
# Page setup
# ------------------------------------------------------------
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"

st.set_page_config(
    page_title="From Goa to Ames | A Personal Journey",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------
# Visual styling
# ------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Playfair+Display:wght@400;500;600&display=swap');

    :root {
        --ink: #172522;
        --muted: #65716d;
        --cream: #f5f2eb;
        --green: #284b40;
        --gold: #c28d4b;
    }

    .stApp {
        background: var(--cream);
        color: var(--ink);
    }

    [data-testid="stHeader"] {
        background: rgba(245, 242, 235, 0.92);
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 1rem;
    }

    h1, h2, h3 {
        font-family: 'Playfair Display', Georgia, serif !important;
        color: var(--ink) !important;
        font-weight: 400 !important;
    }

    p, li, .stMarkdown {
        font-family: 'DM Sans', Arial, sans-serif;
        color: #46534e;
        line-height: 1.8;
    }

    .hero-kicker {
        color: #e6c99e;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.75rem;
        letter-spacing: 0.24em;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }

    .hero-title {
        color: white;
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(3.4rem, 8vw, 6.8rem);
        line-height: 0.98;
        margin: 0;
        font-weight: 400;
    }

    .hero-subtitle {
        color: #f2eee6;
        font-family: 'DM Sans', sans-serif;
        font-size: 1.1rem;
        max-width: 700px;
        margin-top: 1.4rem;
        line-height: 1.8;
    }

    .hero-panel {
        background: linear-gradient(110deg, rgba(13, 28, 24, .94), rgba(13, 28, 24, .48));
        padding: clamp(2rem, 6vw, 5rem);
        border-radius: 4px;
        min-height: 360px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin-bottom: 2rem;
    }

    .intro {
        text-align: center;
        max-width: 820px;
        margin: 2.8rem auto 3rem auto;
    }

    .eyebrow {
        color: #a9793f;
        font-family: 'DM Sans', sans-serif;
        letter-spacing: .2em;
        text-transform: uppercase;
        font-size: .72rem;
        margin-bottom: .6rem;
    }

    .chapter-number {
        color: var(--gold);
        font-family: 'DM Sans', sans-serif;
        letter-spacing: .16em;
        text-transform: uppercase;
        font-size: .72rem;
        margin-bottom: .8rem;
    }

    .chapter-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(2rem, 4vw, 3rem);
        line-height: 1.1;
        color: var(--ink);
        margin-bottom: 1rem;
    }

    .chapter-copy {
        font-size: 1.02rem;
        line-height: 1.9;
        color: #46534e;
        overflow-wrap: anywhere;
        word-break: normal;
    }

    [data-testid="stHorizontalBlock"] {
        align-items: flex-start;
        min-width: 0;
    }

    [data-testid="column"] {
        min-width: 0 !important;
        overflow-wrap: anywhere;
    }

    .chapter-title, .pullquote {
        overflow-wrap: anywhere;
        max-width: 100%;
    }

    .pullquote {
        border-left: 3px solid var(--gold);
        padding: .5rem 0 .5rem 1.1rem;
        margin: 1.4rem 0;
        color: var(--green);
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.25rem;
        font-style: italic;
    }

    .photo-caption {
        color: var(--muted);
        font-family: 'DM Sans', sans-serif;
        font-size: .72rem;
        letter-spacing: .08em;
        text-transform: uppercase;
        margin-top: -.35rem;
        margin-bottom: 1.2rem;
    }

    .story-divider {
        border: 0;
        border-top: 1px solid #ddd8cc;
        margin: 2.5rem 0;
    }

    .quote-band {
        background: var(--green);
        color: white;
        padding: 3.5rem 2rem;
        text-align: center;
        border-radius: 3px;
        margin: 3rem 0;
    }

    .quote-band p {
        color: white !important;
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(1.6rem, 3.8vw, 2.8rem);
        line-height: 1.25;
        max-width: 850px;
        margin: auto;
    }

    .quote-band small {
        display: block;
        color: #d7c6a8;
        font-family: 'DM Sans', sans-serif;
        letter-spacing: .18em;
        text-transform: uppercase;
        margin-top: 1rem;
    }

    .closing {
        background: #e9e4d8;
        padding: 4rem 2rem;
        text-align: center;
        border-radius: 3px;
        margin-top: 3rem;
    }

    .closing-line {
        color: var(--green);
        font-family: 'Playfair Display', Georgia, serif;
        font-style: italic;
        font-size: clamp(1.25rem, 2.5vw, 1.8rem);
        max-width: 850px;
        margin: 1.5rem auto;
        line-height: 1.5;
    }

    .credits {
        color: var(--muted);
        font-family: 'DM Sans', sans-serif;
        font-size: .78rem;
        line-height: 1.8;
        margin-top: 2.5rem;
    }

    footer {
        background: #172522;
        color: #d5ddd8;
        padding: 1.5rem;
        text-align: center;
        font-family: 'DM Sans', sans-serif;
        font-size: .75rem;
        letter-spacing: .08em;
        margin-top: 2rem;
        border-radius: 3px;
    }

    [data-testid="stImage"] img {
        border-radius: 3px;
    }

    @media (max-width: 760px) {
        [data-testid="stMainBlockContainer"] {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        .hero-panel {
            min-height: 300px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Image helper
# ------------------------------------------------------------
def show_photo(filename: str, caption: str, use_container_width: bool = True):
    """Display a local photo from the images folder, with a helpful message if missing."""
    image_path = IMAGE_DIR / filename
    if image_path.exists():
        st.image(str(image_path), use_container_width=use_container_width)
        st.markdown(f'<div class="photo-caption">{caption}</div>', unsafe_allow_html=True)
    else:
        st.warning(
            f"Photo not found: images/{filename}. "
            "Check that the file is inside the project's images folder and that its name matches exactly."
        )


def chapter_text(number: str, label: str, title: str, paragraphs: list[str], quote: str | None = None):
    st.markdown(f'<div class="chapter-number">{number} · {label}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chapter-title">{title}</div>', unsafe_allow_html=True)
    for paragraph in paragraphs:
        st.markdown(f'<p class="chapter-copy">{paragraph}</p>', unsafe_allow_html=True)
    if quote:
        st.markdown(f'<div class="pullquote">“{quote}”</div>', unsafe_allow_html=True)


def divider():
    st.markdown('<hr class="story-divider">', unsafe_allow_html=True)


# ------------------------------------------------------------
# Hero / opening
# ------------------------------------------------------------
# Opening is text-only: the Iowa State campus photo is intentionally not used here.
st.markdown(
    """
    <div class="hero-panel">
        <div class="hero-kicker">A story of distance, friendship & beginning again</div>
        <div class="hero-title">From Goa<br>to Ames</div>
        <div class="hero-subtitle">
            Leaving a familiar life behind, crossing the world, and learning
            how to make a new place feel like home.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="intro">
        <div class="eyebrow">The journey</div>
        <h2>Sometimes starting over means learning to feel at home twice.</h2>
        <p>
            This is my story of moving from BITS Goa to Iowa State University.
            The places changed quickly. Feeling at home took longer.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Chapter 1 - BITS / life I knew
# ------------------------------------------------------------
left, right = st.columns([1.05, 1], gap="large")
with left:
    show_photo("BITS_GOA_Panorama_1-1-.jpg", "01 / BITS Pilani, K. K. Birla Goa Campus")
    show_photo("sunset.jpg", "A sunset at BITS Goa · Personal photograph")
with right:
    chapter_text(
        "Chapter one",
        "The life I knew",
        "A place full of familiar faces.",
        [
            "Growing up, I never really thought about how easy it was to take friends for granted. At BITS Goa, my friends and I were almost always together. Meals meant crowded tables, jokes, and conversations that could go on for hours.",
            "I never had to wonder whether there was a place for me. I could just pull up a chair and make space.",
        ],
        "My entire routine was built around the same people.",
    )

divider()

# ------------------------------------------------------------
# Chapter 2 - Goodbye
# ------------------------------------------------------------
left, right = st.columns([1.05, 1], gap="large")
with left:
    chapter_text(
        "Chapter two",
        "The goodbye",
        "One last night together.",
        [
            "Just before I left for Iowa State, my closest friends and I rented a villa one last time. Late that night, we spent time together and shared our favorite memories.",
            "There were late-night study sessions, random jokes, and all the ridiculous things we did when we were supposed to be studying. That night made me realize how much of my life was tied up in those friendships.",
        ],
    )
with right:
    show_photo("goodbye.jpg", "02 / One last celebration before leaving · Personal photograph")

divider()

# ------------------------------------------------------------
# Chapter 3 - Moving into the dorm with known roommate
# ------------------------------------------------------------
left, right = st.columns([1.05, 1], gap="large")
with left:
    show_photo("dorm.jpg", "03 / Moving into our dorm together · Personal photograph")
with right:
    chapter_text(
        "Chapter three",
        "A new beginning",
        "Twenty-seven hours later.",
        [
            "Then came the airport goodbye. After twenty-seven straight hours of flights and running through terminals, my roommate and I finally made it to Ames.",
            "I already knew my roommate before we arrived, so we were making this move together. We carried our luggage into our new dorm room and started settling in. We were excited to finally be in America, but also tired and a little overwhelmed. We had made it across the world, and now it was time to build a new routine.",
        ],
    )

divider()

# ------------------------------------------------------------
# Chapter 4 - Everything felt different
# ------------------------------------------------------------
left, right = st.columns([1.05, 1], gap="large")
with left:
    # Keep the campus photo out of this chapter; use the personal Ames surroundings photo only.
    show_photo("newenv.jpg", "The view of my surroundings in Ames · Personal photograph")
with right:
    chapter_text(
        "Chapter four",
        "Culture shock",
        "Everything felt different.",
        [
            "The culture shock started immediately. At BITS, campus could still feel alive at two or three in the morning. In Ames, a regular weekday evening could feel completely quiet.",
            "The cold, the wide roads, and the unfamiliar routines made me feel far away from home.",
        ],
        "The places changed. The feeling of belonging had to catch up.",
    )

st.markdown(
    """
    <div class="quote-band">
        <p>“I couldn't just pick up my phone and get instant reassurance. I had to learn to sit with my own problems.”</p>
        <small>The quiet part of moving away</small>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Chapter 5 - First meal alone
# ------------------------------------------------------------
left, right = st.columns([1.05, 1], gap="large")
with left:
    show_photo("mess.jpg", "05 / Seasons Marketplace, Maple Willow Larch Commons · Personal photograph")
with right:
    chapter_text(
        "Chapter five",
        "The empty table",
        "The first meal alone.",
        [
            "One of the hardest moments was going to the dining hall alone for the first time. I walked in carrying a tray, looking for somewhere to sit.",
            "The room was bright and clean, but it felt strangely quiet compared with the crowded mess hall I was used to. I found a small table by the window and sat down by myself.",
        ],
    )

divider()

# ------------------------------------------------------------
# Chapter 6 - Finding my feet
# ------------------------------------------------------------
left, right = st.columns([1.05, 1], gap="large")
with left:
    show_photo("isu.jpg", "06 / Iowa State University campus")
with right:
    chapter_text(
        "Chapter six",
        "Finding my feet",
        "Making room for something new.",
        [
            "Slowly, things started to shift. I began going to club meetings, talking to people in my engineering lectures, and exchanging numbers with classmates to work on homework.",
            "In mechanics and physics, the equations were familiar. The symbols and vectors were the same in Ames as they had been in Goa. Little by little, I started building a new routine.",
        ],
    )

# ------------------------------------------------------------
# Closing
# ------------------------------------------------------------
st.markdown(
    """
    <div class="closing">
        <div class="eyebrow">The lesson I carried with me</div>
        <h2>It took time to fill the table again.</h2>
        <p>
            The friends I had at BITS did not become close in a day. It took shared
            meals, late nights, and years of memories. Moving across the world meant
            starting that process again—and learning to be patient with it.
        </p>
        <div class="closing-line">
            “Independence isn't about having everything figured out right away.
            It's about having the patience to sit at an empty table until you take
            the steps to fill it up again.”
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Photo credits / footer
# ------------------------------------------------------------
st.markdown(
    """
    <div class="credits">
        <strong>Photo notes</strong><br>
        Personal photographs supplied for this project are used for the villa goodbye,
        dorm move-in, BITS sunset, Ames neighborhood, and Seasons Marketplace scenes.
        The BITS Goa and Iowa State campus images are supplied separately in the images folder.
        The written narration is adapted from the personal narrative.
    </div>
    <footer>
        FROM GOA TO AMES · A PERSONAL NARRATIVE MULTIMODAL REMIX
    </footer>
    """,
    unsafe_allow_html=True,
)
