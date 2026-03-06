# =============================================================================
# THEREALNEWS + Personal Homepage
# Lawrence Hartman – Federal Way, WA
# Email: Hartmanlawrence291@gmail.com
# Built with Streamlit – March 2026
# =============================================================================

import streamlit as st
import feedparser
from datetime import datetime, timedelta
import random
import time
import hashlib

# ────────────────────────────────────────────────
# Page config & session state
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="Lawrence Hartman | THEREALNEWS",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Persistent user preferences
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
    'show_intro': True
}

for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ────────────────────────────────────────────────
# Color scheme – cozy mature formal dark mode
# ────────────────────────────────────────────────
COLORS = {
    'bg': "#0f1218",
    'card_bg': "#161b22",
    'text': "#e0e7ff",
    'text_muted': "#94a3b8",
    'accent': "#a78bfa",     # soft violet – mature & warm
    'accent_dark': "#7c3aed",
    'red': "#f87171",
    'gold': "#fbbf24",
    'blue': "#60a5fa",
    'border': "#2d3748",
    'gradient_start': "rgba(15,18,24,0.92)",
    'gradient_end': "rgba(22,27,34,0.65)"
}

# Responsive typography
font_sizes = {
    "Small":  {"title": "1.25rem", "meta": "0.875rem", "summary": "0.9375rem"},
    "Medium": {"title": "1.5rem",  "meta": "0.9375rem", "summary": "1rem"},
    "Large":  {"title": "1.75rem", "meta": "1.0625rem", "summary": "1.125rem"}
}
fs = font_sizes[st.session_state.font_size]

# ────────────────────────────────────────────────
# Global styling – cozy, mature, formal
# ────────────────────────────────────────────────
st.markdown(f"""
    <style>
        /* Base */
        [data-testid="stAppViewContainer"] {{
            background-color: {COLORS['bg']} !important;
            background-image: radial-gradient(circle at 25% 25%, rgba(167,139,250,0.03) 0%, transparent 50%);
        }}
        .stApp {{
            background-color: {COLORS['bg']} !important;
            color: {COLORS['text']} !important;
            font-family: 'Georgia', serif;
        }}
        section[data-testid="stSidebar"] {{
            background-color: {COLORS['card_bg']} !important;
            border-right: 1px solid {COLORS['border']};
        }}
        hr {{
            border-color: {COLORS['border']} !important;
            margin: 2.5rem 0 1.8rem 0;
        }}

        /* Cards */
        .card {{
            background: {COLORS['card_bg']};
            border: 1px solid {COLORS['border']};
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 2.2rem;
            box-shadow: 0 6px 20px rgba(0,0,0,0.45);
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }}
        .card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 32px rgba(0,0,0,0.55);
        }}
        .gradient-overlay {{
            position: absolute;
            bottom: 0; left: 0; right: 0;
            padding: 7rem 1.5rem 1.5rem;
            background: linear-gradient(to top, {COLORS['gradient_start']} 0%, {COLORS['gradient_end']} 100%);
            color: white;
        }}
        .card-title {{
            font-size: {fs['title']};
            font-weight: 700;
            line-height: 1.32;
            margin: 0 0 0.5rem 0;
        }}
        .card-meta {{
            font-size: {fs['meta']};
            color: {COLORS['text_muted']};
            margin-bottom: 0.75rem;
        }}
        .summary {{
            font-size: {fs['summary']};
            color: #cbd5e1;
            line-height: 1.55;
            margin: 0.6rem 0 1.2rem 0;
        }}

        /* Buttons */
        .btn {{
            background: {COLORS['accent']} !important;
            color: white !important;
            border: none !important;
            padding: 0.65rem 1.25rem !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            margin: 0.4rem 0.6rem 0.4rem 0 !important;
            transition: all 0.18s;
        }}
        .btn:hover {{
            background: {COLORS['accent_dark']} !important;
            transform: translateY(-1px);
        }}

        /* Badges */
        .badge {{
            padding: 0.35rem 0.75rem;
            border-radius: 1rem;
            font-size: 0.78rem;
            color: white;
            margin-left: 0.6rem;
            background: {COLORS['accent']};
        }}

        /* Floating buttons */
        .x-float-btn {{
            position: fixed; right: 1.8rem; bottom: 2.2rem; z-index: 999;
            background: {COLORS['accent']}; color: white;
            border: none; border-radius: 50%;
            width: 3.8rem; height: 3.8rem; font-size: 1.8rem;
            box-shadow: 0 6px 20px rgba(0,0,0,0.5);
            cursor: pointer; display: flex; align-items: center; justify-content: center;
            transition: all 0.22s;
        }}
        .x-float-btn:hover {{ transform: scale(1.12); }}

        /* Mobile adjustments */
        @media (max-width: 768px) {{
            .card {{ margin-bottom: 1.8rem; }}
            .gradient-overlay {{ padding: 6rem 1.2rem 1.2rem; }}
            .card-title {{ font-size: calc({fs['title']} * 0.92); }}
            .summary {{ font-size: calc({fs['summary']} * 0.95); }}
            .btn {{ padding: 0.6rem 1.1rem !important; font-size: 0.92rem !important; margin: 0.3rem 0.5rem 0.3rem 0 !important; }}
            .x-float-btn {{ right: 1.2rem; bottom: 1.6rem; width: 3.2rem; height: 3.2rem; font-size: 1.6rem; }}
        }}
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Header & intro
# ────────────────────────────────────────────────
st.markdown(f"""
    <h1 style="text-align:center; color:{colors['header']}; margin-bottom:0.4rem; letter-spacing:-1px;">
        Lawrence Hartman
    </h1>
    <p style="text-align:center; color:#94a3b8; font-size:1.25rem; margin-top:0;">
        Federal Way, Washington
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# Personal intro section
col_intro1, col_intro2 = st.columns([2, 1])
with col_intro1:
    st.markdown("""
    ### Welcome
    I'm Lawrence — creator of **THEREALNEWS**, a curated feed of Republican and conservative news sources.

    The site lets you filter by topic (**War**, **Politics**, **Economics**) and shows real-time probability estimates in War mode.

    I built it to cut through noise and give a clearer view of what matters from a right-leaning perspective.
    """)

with col_intro2:
    st.markdown(f"""
    <div style="text-align:center; padding:1.5rem; background:{COLORS['card_bg']}; border-radius:12px; border:1px solid {COLORS['border']};">
        <h3 style="margin:0 0 0.8rem 0; color:{COLORS['accent']};">Quick Links</h3>
        <a href="#news-feed" style="display:block; margin:0.8rem 0; color:{COLORS['accent']}; text-decoration:none;">→ Go to News Feed</a>
        <a href="mailto:Hartmanlawrence291@gmail.com" style="display:block; margin:0.8rem 0; color:{COLORS['accent']}; text-decoration:none;">→ Email me</a>
        <p style="margin:1.2rem 0 0.6rem 0; font-size:0.95rem; color:#94a3b8;">Federal Way, WA</p>
    </div>
    """, unsafe_allow_html=True)

# ────────────────────────────────────────────────
# News feed section
# ────────────────────────────────────────────────
st.markdown('<div id="news-feed"></div>', unsafe_allow_html=True)
st.header("THEREALNEWS Feed")

# Sidebar controls
with st.sidebar:
    st.header("Controls")
    st.session_state.dark_mode = st.toggle("Dark Mode", value=st.session_state.dark_mode)
    st.session_state.font_size = st.selectbox("Text Size", ["Small", "Medium", "Large"], index=["Small","Medium","Large"].index(st.session_state.font_size))
    st.session_state.auto_refresh = st.checkbox("Auto-refresh every 5 min", value=st.session_state.auto_refresh)

    st.subheader("Favorite Sources")
    sources = list(RSS_FEEDS.keys())
    selected = st.multiselect("", sources, default=list(st.session_state.favorite_sources))
    st.session_state.favorite_sources = set(selected)

    st.subheader("Contact")
    st.markdown("**Email**")
    st.markdown("Hartmanlawrence291@gmail.com")

# Feed display logic (abbreviated – same as before)
# ... (add your full news fetching, filtering, card rendering code here)

st.caption("THEREALNEWS with Lawrence • Conservative perspective • March 2026")
