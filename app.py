import streamlit as st
import feedparser
from datetime import datetime, timedelta
import random
import time

st.set_page_config(page_title="Lawrence Hartman | THEREALNEWS", page_icon="📰", layout="wide")

# ────────────────────────────────────────────────
# Session state & defaults
# ────────────────────────────────────────────────
defaults = {
    'dark_mode': True,
    'font_size': "Medium",
    'auto_refresh': False,
    'favorite_sources': set(),
    'read_stories': set(),
    'saved_stories': [],
    'search_history': [],
    'loaded_count': 15,
    'x_menu_open': False,
    'sort_option': "Newest first",
    'game_score': 0,
    'game_attempts': 0
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ────────────────────────────────────────────────
# RSS feeds (only conservative/Republican sources)
# ────────────────────────────────────────────────
RSS_FEEDS = {
    "Fox News": ["https://moxie.foxnews.com/google-publisher/latest.xml"],
    "Breitbart": ["https://feeds.feedburner.com/breitbart"],
    "Newsmax": ["https://www.newsmax.com/rss/newsfront/16"],
    "Daily Wire": ["https://www.dailywire.com/feeds/rss.xml"],
    "The Federalist": ["https://thefederalist.com/feed/"],
    "Epoch Times": ["https://www.theepochtimes.com/feed"],
    "OANN": ["https://www.oann.com/category/newsroom/feed/"],
    "Washington Examiner": ["https://www.washingtonexaminer.com/feed"],
    "National Review": ["https://www.nationalreview.com/feed"],
    "The Blaze": ["https://www.theblaze.com/feeds/feed.rss"]
}

# ────────────────────────────────────────────────
# Mode colors & theme
# ────────────────────────────────────────────────
mode_colors = {
    "All": {"accent": "#e2e8f0", "header": "#f1f5f9", "bg": "#0f1218", "card": "#1e293b", "text": "#e2e8f0", "muted": "#94a3b8"},
    "War": {"accent": "#ef4444", "header": "#f87171", "bg": "#0f1218", "card": "#1e293b", "text": "#e2e8f0", "muted": "#94a3b8"},
    "Politics": {"accent": "#3b82f6", "header": "#60a5fa", "bg": "#0f1218", "card": "#1e293b", "text": "#e2e8f0", "muted": "#94a3b8"},
    "Economics": {"accent": "#d97706", "header": "#fbbf24", "bg": "#0f1218", "card": "#1e293b", "text": "#e2e8f0", "muted": "#94a3b8"}
}

mode = st.selectbox("News Mode", ["All", "War", "Politics", "Economics"], index=0)
colors = mode_colors[mode]

# ────────────────────────────────────────────────
# Smooth, cozy, mature styling
# ────────────────────────────────────────────────
st.markdown(f"""
    <style>
        [data-testid="stAppViewContainer"] {{
            background: linear-gradient(135deg, #0f1218 0%, #111827 100%) !important;
        }}
        .stApp {{
            color: {colors['text']} !important;
            font-family: 'Georgia', serif;
        }}
        section[data-testid="stSidebar"] {{
            background: #1e293b !important;
            border-right: 1px solid #334155;
        }}
        .card {{
            background: {colors['card']};
            border: 1px solid #334155;
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 1.8rem;
            box-shadow: 0 6px 20px rgba(0,0,0,0.45);
            transition: all 0.25s ease;
        }}
        .card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 32px rgba(0,0,0,0.55);
        }}
        .gradient-overlay {{
            position: absolute;
            bottom: 0; left: 0; right: 0;
            padding: 6rem 1.4rem 1.4rem;
            background: linear-gradient(to top, rgba(15,18,24,0.94) 0%, rgba(30,41,59,0.7) 100%);
        }}
        .card-title {{ font-size: {fs['title']}; font-weight: 700; line-height: 1.35; margin: 0 0 0.5rem 0; }}
        .card-meta {{ font-size: {fs['meta']}; color: {colors['muted']}; margin-bottom: 0.8rem; }}
        .summary {{ font-size: {fs['summary']}; color: #cbd5e1; line-height: 1.6; }}
        .btn {{
            background: {colors['accent']} !important;
            color: white !important;
            border: none !important;
            padding: 0.65rem 1.4rem !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            margin: 0.4rem 0.6rem 0.4rem 0 !important;
            transition: all 0.18s;
        }}
        .btn:hover {{ background: {colors['accent_dark']} !important; transform: translateY(-1px); }}
        .badge {{ padding: 0.35rem 0.8rem; border-radius: 1rem; font-size: 0.82rem; color: white; margin-left: 0.6rem; background: {colors['accent']}; }}
        .x-float-btn {{
            position: fixed; right: 1.6rem; bottom: 2rem; z-index: 999;
            background: {colors['accent']}; color: white;
            border-radius: 50%; width: 3.6rem; height: 3.6rem;
            font-size: 1.8rem; box-shadow: 0 6px 20px rgba(0,0,0,0.5);
            cursor: pointer; display: flex; align-items: center; justify-content: center;
            transition: all 0.22s;
        }}
        .x-float-btn:hover {{ transform: scale(1.12); }}
        @media (max-width: 768px) {{
            .card {{ margin-bottom: 1.6rem; }}
            .gradient-overlay {{ padding: 5.5rem 1.2rem 1.2rem; }}
            .card-title {{ font-size: calc({fs['title']} * 0.9); }}
            .btn {{ padding: 0.6rem 1.2rem !important; font-size: 0.92rem !important; }}
            .x-float-btn {{ right: 1.2rem; bottom: 1.6rem; width: 3rem; height: 3rem; font-size: 1.6rem; }}
        }}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown(f"""
    <h1 style="text-align:center; color:{colors['header']}; margin:0.8rem 0 0.3rem 0;">
        Lawrence Hartman
    </h1>
    <p style="text-align:center; color:#94a3b8; font-size:1.3rem; margin-top:0;">
        Federal Way, Washington
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# Intro & news link
st.markdown(f"""
    <div style="max-width:800px; margin:0 auto; text-align:center;">
        <h3 style="color:{colors['accent']}; margin-bottom:1.2rem;">
            Welcome
        </h3>
        <p style="font-size:1.1rem; line-height:1.7; color:#cbd5e1;">
            I'm Lawrence — creator of THEREALNEWS, a curated feed of Republican and conservative sources.
            Switch between War, Politics, and Economics modes — War mode includes probability estimates for what might happen next.
        </p>
        <a href="https://yourusername-therealnews.streamlit.app" target="_blank" style="
            display:inline-block; background:{colors['accent']}; color:white; padding:1rem 2.2rem;
            border-radius:10px; font-weight:600; font-size:1.2rem; text-decoration:none; margin:1.5rem 0;
            transition:all 0.2s;">
            → Open THEREALNEWS
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Contact section
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Email**")
    st.markdown("Hartmanlawrence291@gmail.com")

with col2:
    st.markdown("**Phone**")
    st.markdown("(509) 552-7109")

st.markdown("**Location**")
st.markdown("Federal Way, Washington")

# Small fun game in sidebar
with st.sidebar:
    st.header("Quick Game")
    st.caption("Guess the Conservative Quote")

    quotes = [
        ("Government is not the solution to our problem; government is the problem.", "Ronald Reagan"),
        ("Make America Great Again.", "Donald Trump"),
        ("Freedom is never more than one generation away from extinction.", "Ronald Reagan")
    ]

    if 'game_quote' not in st.session_state:
        st.session_state.game_quote = random.choice(quotes)

    quote, author = st.session_state.game_quote

    st.markdown(f"**Quote:** \"{quote}\"")
    guess = st.radio("Who said it?", [q[1] for q in quotes if q[1] != author] + [author], index=None)

    if guess:
        if guess == author:
            st.success(f"Correct! It's {author}.")
            st.session_state.game_score += 1
        else:
            st.error(f"Wrong. It was {author}.")
        st.session_state.game_attempts += 1
        if st.button("New Quote"):
            st.session_state.game_quote = random.choice(quotes)
            st.rerun()

    st.caption(f"Score: {st.session_state.game_score} / {st.session_state.game_attempts}")

# Footer
st.markdown("---")
st.caption("© 2026 Lawrence Hartman • THEREALNEWS • Conservative perspective • Built with Streamlit")
