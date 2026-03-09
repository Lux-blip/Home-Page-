import streamlit as st
import datetime
import random

# ── Page config for Black Ops Cold War amber terminal style ──
st.set_page_config(
    page_title="CIA SAFEHOUSE TERMINAL – LAWRENCE ACCESS",
    page_icon="🖥️",
    layout="wide",
)

# Custom CSS: Amber/orangish-brown phosphor CRT look (no green)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

    body, .stApp {
        background-color: #000000 !important;
        color: #ffb700 !important;  /* Classic amber phosphor – orangish yellow-brown glow */
        font-family: 'VT323', monospace !important;
        font-size: 1.5rem !important;
        line-height: 1.4 !important;
    }
    .stMarkdown, h1, h2, h3, p, div, span, a {
        color: #ffb700 !important;
        text-shadow: 0 0 6px #ff9900, 0 0 12px #ff9900, 0 0 18px #ff6600;
    }
    /* Subtle orange-tinted scanlines */
    .stApp::before {
        content: " ";
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(
            to bottom,
            transparent 0px,
            transparent 3px,
            rgba(255,180,0,0.08) 3px,
            rgba(255,180,0,0.08) 6px
        );
        pointer-events: none;
        z-index: 9999;
    }
    /* Screen flicker + subtle roll */
    @keyframes flicker {
        0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; transform: translateY(0); }
        20%, 24%, 55% { opacity: 0.9; transform: translateY(1px); }
    }
    .crt-flicker {
        animation: flicker 8s infinite;
    }
    /* Warmer phosphor glow */
    .glow {
        text-shadow: 
            0 0 5px #ffb700,
            0 0 10px #ff9900,
            0 0 20px #ff6600,
            0 0 30px #ff5500;
    }
    /* Blinking cursor – amber */
    @keyframes blink {
        0%, 49% { opacity: 1; }
        50%, 100% { opacity: 0; }
    }
    .cursor { 
        display: inline-block; 
        width: 14px; 
        height: 1.3em; 
        background: #ffb700; 
        animation: blink 0.8s step-end infinite; 
        vertical-align: middle;
    }
    /* Vignette + slight curve feel */
    .vignette {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        pointer-events: none;
        background: radial-gradient(circle at 50% 50%, transparent 30%, rgba(0,0,0,0.85) 100%);
        z-index: 9998;
    }
    hr { border-color: #331a00; }  /* Dark brown-orange */
    a { color: #ff9900 !important; text-decoration: underline; }
    .red-alert { color: #ff3300 !important; text-shadow: 0 0 8px #ff3300; }
    </style>
    <div class="vignette"></div>
    """, unsafe_allow_html=True)

# Main content wrapper
st.markdown('<div class="crt-flicker">', unsafe_allow_html=True)

# ── Boot / Login screen vibe ──
st.markdown('<h1 class="glow">CIA SAFEHOUSE TERMINAL – ACCESS GRANTED</h1>', unsafe_allow_html=True)
st.markdown('<p class="glow">USER: LAWRENCE | LOCATION: FEDERAL WAY WA | ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + ' <span class="cursor"></span></p>', unsafe_allow_html=True)
st.markdown('<p class="red-alert">**CLASSIFIED – LEVEL PATRIOT**</p>', unsafe_allow_html=True)
st.markdown("---")

# Daily directive (Reagan quote style)
quotes = [
    "MR GORBACHEV, TEAR DOWN THIS WALL! – REAGAN 1987",
    "WE WIN, THEY LOSE. – RONALD REAGAN",
    "FREEDOM IS NEVER MORE THAN ONE GENERATION AWAY FROM EXTINCTION. – RONALD REAGAN",
    "TRUST BUT VERIFY. – RONALD REAGAN",
]
st.markdown(f'<p class="glow">> DAILY DIRECTIVE: "{random.choice(quotes)}" <span class="cursor"></span></p>', unsafe_allow_html=True)
st.markdown("---")

# ── Sidebar: Command menu ──
with st.sidebar:
    st.markdown('<h2 class="glow">COMMAND INTERFACE</h2>', unsafe_allow_html=True)
    st.markdown('<p>📞 PHONE: (253) XXX-XXXX</p>')           # ← YOUR REAL PHONE NUMBER
    st.markdown('<p>✉️ EMAIL: lawrence@example.com</p>')     # ← YOUR REAL EMAIL
    st.markdown("---")
    st.markdown('<p class="glow">> STATUS: ONLINE | SEC LEVEL: PATRIOT</p>', unsafe_allow_html=True)

# ── Main content ──
st.subheader(">> SYSTEM STATUS")
st.write("""
OPERATOR......... LAWRENCE
LOCATION......... FEDERAL WAY COMMAND POST
MISSION.......... TRUTH DISSEMINATION VIA CONSERVATIVE FEEDS
PRIMARY ASSET.... THEREALNEWS TERMINAL
""")

st.subheader(">> ACCESS PRIMARY ASSET")
st.markdown("""
<p class="glow">
> <a href="https://therealnews-8q9zgdyymx83erjszxjxgb.streamlit.app/" target="_blank">
LAUNCH THEREALNEWS – WAR/POLITICS/ECONOMICS ANALYSIS
</a> <span class="cursor"></span>
</p>
""", unsafe_allow_html=True)

st.subheader(">> CONTACT PROTOCOL")
st.write("> TRANSMIT MESSAGE VIA SECURE CHANNEL:")
st.markdown('- PHONE: (253) XXX-XXXX')           # ← YOUR REAL PHONE NUMBER
st.markdown('- EMAIL: lawrence@example.com')     # ← YOUR REAL EMAIL
st.write('> ACKNOWLEDGE RECEIPT WITHIN 0600 SECONDS. <span class="cursor"></span>', unsafe_allow_html=True)

st.markdown("---")
st.caption("TERMINAL v1.0 – STREAMLIT / PYTHON – CLASSIFIED 2026 – FOR LIBERTY")

st.markdown('</div>', unsafe_allow_html=True)
