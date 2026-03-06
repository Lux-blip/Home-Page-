import streamlit as st
import datetime

st.set_page_config(
    page_title="Lawrence Hartman | THEREALNEWS",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Session state for dark mode toggle
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = True

# Cozy, mature, formal dark theme
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=st.session_state.dark_mode)

if dark_mode:
    bg_color       = "#0f1218"
    card_bg        = "#161b22"
    text_color     = "#e0e7ff"
    muted_text     = "#94a3b8"
    accent         = "#a78bfa"      # soft violet – warm & professional
    accent_dark    = "#7c3aed"
    header_color   = "#c9d1d9"
    border_color   = "#2d3748"
    gradient_start = "rgba(15,18,24,0.94)"
    gradient_end   = "rgba(22,27,34,0.7)"
else:
    bg_color       = "#f8f9fa"
    card_bg        = "#ffffff"
    text_color     = "#212529"
    muted_text     = "#6c757d"
    accent         = "#6f42c1"
    accent_dark    = "#5a32a3"
    header_color   = "#343a40"
    border_color   = "#dee2e6"
    gradient_start = "rgba(248,249,250,0.94)"
    gradient_end   = "rgba(255,255,255,0.7)"

# Full styling
st.markdown(f"""
    <style>
        /* Base */
        [data-testid="stAppViewContainer"] {{
            background: linear-gradient(135deg, {bg_color} 0%, #111827 100%) !important;
        }}
        .stApp {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
            font-family: 'Georgia', 'Times New Roman', serif;
        }}
        section[data-testid="stSidebar"] {{
            background-color: {card_bg} !important;
            border-right: 1px solid {border_color};
        }}
        hr {{
            border-color: {border_color} !important;
            margin: 2.8rem 0 1.8rem 0;
        }}

        /* Headings */
        h1, h2, h3 {{
            color: {accent} !important;
            font-weight: 600;
        }}

        /* Main card */
        .main-card {{
            background: {card_bg};
            border: 1px solid {border_color};
            border-radius: 16px;
            padding: 2.5rem;
            margin: 2rem auto;
            max-width: 900px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.45);
            transition: transform 0.22s ease;
        }}
        .main-card:hover {{
            transform: translateY(-6px);
        }}

        /* Link button */
        .news-btn {{
            display: inline-block;
            background: {accent} !important;
            color: white !important;
            padding: 1rem 2.5rem !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            font-size: 1.25rem !important;
            text-decoration: none !important;
            margin: 2rem 0;
            transition: all 0.22s;
        }}
        .news-btn:hover {{
            background: {accent_dark} !important;
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(167,139,250,0.35);
        }}

        /* Contact grid */
        .contact-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.8rem;
            margin: 2rem 0;
        }}
        .contact-item {{
            background: {card_bg};
            border: 1px solid {border_color};
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
        }}
        .contact-label {{
            color: {muted_text};
            font-weight: 500;
            display: block;
            margin-bottom: 0.6rem;
        }}

        /* Footer */
        .footer {{
            text-align: center;
            color: {muted_text};
            font-size: 0.95rem;
            margin-top: 5rem;
            padding-bottom: 3rem;
        }}

        /* Mobile */
        @media (max-width: 768px) {{
            .contact-grid {{
                grid-template-columns: 1fr;
            }}
            .main-card {{
                padding: 1.8rem;
                margin: 1.5rem 0.8rem;
            }}
            .news-btn {{
                padding: 0.9rem 2rem !important;
                font-size: 1.1rem !important;
            }}
        }}
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Main content
# ────────────────────────────────────────────────
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown(f"""
    <h1 style="text-align:center; margin-bottom:0.5rem;">
        Lawrence Hartman
    </h1>
    <p style="text-align:center; color:{muted_text}; font-size:1.3rem; margin-top:0;">
        Federal Way, Washington
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown(f"""
    <h3 style="color:{accent}; text-align:center; margin:2rem 0 1.2rem 0;">
        Welcome
    </h3>
    <p style="font-size:1.15rem; line-height:1.8; text-align:center; max-width:700px; margin:0 auto;">
        I'm Lawrence — creator of THEREALNEWS, a curated news feed built around Republican and conservative sources.
        Switch between War, Politics, and Economics modes. War mode includes probability estimates for what might happen next.
    </p>
""", unsafe_allow_html=True)

# Big news site button
news_url = "https://yourusername-therealnews.streamlit.app"  # ← CHANGE THIS to your real news URL
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

# Footer
st.markdown(f"""
    <div class="footer">
        © {datetime.now().year} Lawrence Hartman • Built with Streamlit • Conservative perspective
    </div>
""", unsafe_allow_html=True)
