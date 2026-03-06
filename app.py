import streamlit as st
import datetime
import random

st.set_page_config(
    page_title="Lawrence Hartman | THEREALNEWS",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Session state
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = True
if 'game_score' not in st.session_state:
    st.session_state.game_score = 0
if 'game_attempts' not in st.session_state:
    st.session_state.game_attempts = 0

# Theme toggle in sidebar
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=st.session_state.dark_mode)

# Colors – cozy mature formal dark mode
if dark_mode:
    bg = "#0f1218"
    card_bg = "#161b22"
    text = "#e0e7ff"
    muted = "#94a3b8"
    accent = "#a78bfa"      # soft violet
    accent_dark = "#7c3aed"
    header = "#c9d1d9"
    border = "#2d3748"
else:
    bg = "#f8f9fa"
    card_bg = "#ffffff"
    text = "#212529"
    muted = "#6c757d"
    accent = "#6f42c1"
    accent_dark = "#5a32a3"
    header = "#343a40"
    border = "#dee2e6"

# Smooth styling
st.markdown(f"""
    <style>
        [data-testid="stAppViewContainer"] {{
            background: linear-gradient(135deg, {bg} 0%, #111827 100%) !important;
        }}
        .stApp {{
            background-color: {bg} !important;
            color: {text} !important;
            font-family: 'Georgia', serif;
        }}
        section[data-testid="stSidebar"] {{
            background-color: {card_bg} !important;
            border-right: 1px solid {border};
        }}
        hr {{
            border-color: {border} !important;
            margin: 2.8rem 0 1.8rem 0;
        }}
        h1, h2, h3 {{
            color: {accent} !important;
        }}
        .main-card {{
            background: {card_bg};
            border: 1px solid {border};
            border-radius: 16px;
            padding: 2.8rem;
            margin: 2rem auto;
            max-width: 1000px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.45);
            transition: transform 0.25s ease;
        }}
        .main-card:hover {{
            transform: translateY(-6px);
        }}
        .news-btn {{
            display: inline-block;
            background: {accent} !important;
            color: white !important;
            padding: 1.1rem 2.8rem !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            font-size: 1.3rem !important;
            text-decoration: none !important;
            margin: 2rem 0;
            transition: all 0.25s;
        }}
        .news-btn:hover {{
            background: {accent_dark} !important;
            transform: translateY(-4px);
            box-shadow: 0 10px 30px rgba(167,139,250,0.3);
        }}
        .contact-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.8rem;
            margin: 2.5rem 0;
        }}
        .contact-item {{
            background: {card_bg};
            border: 1px solid {border};
            border-radius: 12px;
            padding: 1.8rem;
            text-align: center;
        }}
        .contact-label {{
            color: {muted};
            font-weight: 500;
            display: block;
            margin-bottom: 0.7rem;
        }}
        .footer {{
            text-align: center;
            color: {muted};
            font-size: 0.95rem;
            margin-top: 5rem;
            padding-bottom: 3rem;
        }}
        @media (max-width: 768px) {{
            .main-card {{ padding: 2rem; margin: 1.5rem 1rem; }}
            .contact-grid {{ grid-template-columns: 1fr; }}
            .news-btn {{ padding: 1rem 2.2rem !important; font-size: 1.15rem !important; }}
        }}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown(f"""
    <div class="main-card">
        <h1 style="text-align:center; margin-bottom:0.4rem;">
            Lawrence Hartman
        </h1>
        <p style="text-align:center; color:{muted}; font-size:1.35rem; margin-top:0;">
            Federal Way, Washington
        </p>
""", unsafe_allow_html=True)

st.markdown("---")

# Intro
st.markdown(f"""
    <h3 style="color:{accent}; text-align:center; margin:2rem 0 1.2rem 0;">
        Welcome
    </h3>
    <p style="font-size:1.18rem; line-height:1.8; text-align:center; max-width:720px; margin:0 auto 2rem auto;">
        I'm Lawrence — creator of THEREALNEWS, a curated news feed focused on Republican and conservative sources.
        Switch between War, Politics, and Economics modes. War mode includes probability estimates for potential next events.
    </p>
""", unsafe_allow_html=True)

# News link button
news_url = "https://your-username-therealnews.streamlit.app"  # ← CHANGE THIS to your real THEREALNEWS URL
st.markdown(
    f'<a href="{news_url}" target="_blank" class="news-btn">→ Open THEREALNEWS</a>',
    unsafe_allow_html=True
)

# Contact grid
st.markdown('<div class="contact-grid">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div class="contact-item">
            <div class="contact-label">Email</div>
            Hartmanlawrence291@gmail.com
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="contact-item">
            <div class="contact-label">Phone</div>
            (509) 552-7109
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f"""
    <div style="text-align:center; margin:2rem 0;">
        <div class="contact-label">Location</div>
        Federal Way, Washington
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close main-card

# Small interactive game in sidebar
with st.sidebar:
    st.header("Fun Game")
    st.caption("Guess the Quote")

    quotes = [
        ("Government is not the solution to our problem; government is the problem.", "Ronald Reagan"),
        ("Make America Great Again.", "Donald Trump"),
        ("Freedom is never more than one generation away from extinction.", "Ronald Reagan"),
        ("The nine most terrifying words are: I'm from the government and I'm here to help.", "Ronald Reagan")
    ]

    if 'game_quote' not in st.session_state:
        st.session_state.game_quote = random.choice(quotes)

    quote, correct_author = st.session_state.game_quote

    st.markdown(f"**Quote:** “{quote}”")
    options = [q[1] for q in quotes]
    random.shuffle(options)
    guess = st.radio("Who said it?", options, index=None, key=f"guess_{id(st.session_state.game_quote)}")

    if guess:
        if guess == correct_author:
            st.success(f"Correct! It was {correct_author}.")
            st.session_state.game_score += 1
        else:
            st.error(f"Wrong. It was {correct_author}.")
        st.session_state.game_attempts += 1

        if st.button("New Quote"):
            st.session_state.game_quote = random.choice(quotes)
            st.rerun()

    st.caption(f"Score: {st.session_state.game_score} / {st.session_state.game_attempts}")

# Footer
st.markdown(f"""
    <div class="footer">
        © {datetime.datetime.now().year} Lawrence Hartman • Built with Streamlit • Conservative perspective
    </div>
""", unsafe_allow_html=True)
