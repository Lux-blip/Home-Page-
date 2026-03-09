import streamlit as st
import datetime
import random

# ── Page config for authentic Black Ops Cold War green terminal ──
st.set_page_config(
    page_title="CIA SAFEHOUSE TERMINAL – LAWRENCE ACCESS",
    page_icon="🖥️",
    layout="wide",
)

# Custom CSS: Bright green phosphor CRT like BO Cold War safehouse terminal
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

    body, .stApp {
        background-color: #000000 !important;
        color: #00ff41 !important;  /* Bright, classic green phosphor */
        font-family: 'VT323', monospace !important;
        font-size: 1.6rem !important;
        line-height: 1.4 !important;
    }
    .stMarkdown, h1, h2, h3, p, div, span, a {
        color: #00ff41 !important;
        text-shadow: 0 0 8px #00ff41, 0 0 16px #00ff41, 0 0 24px #00cc33;
    }
    /* Crisp scanlines like game CRT */
    .stApp::before {
        content: " ";
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(
            to bottom,
            transparent 0px,
            transparent 2px,
            rgba(0,255,0,0.15) 2px,
            rgba(0,255,0,0.15) 4px
        );
        pointer-events: none;
        z-index: 9999;
    }
    /* Flicker + subtle roll for authentic CRT feel */
    @keyframes flicker {
        0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; transform: translateY(0); }
        20%, 24%, 55% { opacity: 0.92; transform: translateY(1px); }
    }
    .crt-flicker {
        animation: flicker 7s infinite;
    }
    /* Strong phosphor glow */
    .glow {
        text-shadow: 
            0 0 6px #00ff41,
            0 0 12px #00ff41,
            0 0 24px #00cc33,
            0 0 36px #009933;
    }
    /* Blinking cursor – sharp green */
    @keyframes blink {
        0%, 49% { opacity: 1; }
        50%, 100% { opacity: 0; }
    }
    .cursor { 
        display: inline-block; 
        width: 14px; 
        height: 1.3em; 
        background: #00ff41; 
        animation: blink 0.7s step-end infinite; 
        vertical-align: middle;
    }
    /* Vignette for curved CRT edges */
    .vignette {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        pointer-events: none;
        background: radial-gradient(circle at 50% 50%, transparent 35%, rgba(0,0,0,0.8) 100%);
        z-index: 9998;
    }
    hr { border-color: #003300; }
    a { color: #00cc33 !important; text-decoration: underline; }
    .alert { color: #ff0000 !important; text-shadow: 0 0 10px #ff0000; }
    </style>
    <div class="vignette"></div>
    """, unsafe_allow_html=True)

# Main wrapper
st.markdown('<div class="crt-flicker">', unsafe_allow_html=True)

# Boot screen
st.markdown('<h1 class="glow">CIA SAFEHOUSE TERMINAL – ACCESS GRANTED</h1>', unsafe_allow_html=True)
st.markdown('<p class="glow">USER: LAWRENCE | LOCATION: FEDERAL WAY WA | ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M PDT") + ' <span class="cursor"></span></p>', unsafe_allow_html=True)
st.markdown('<p class="alert">**CLASSIFIED – LEVEL PATRIOT**</p>', unsafe_allow_html=True)
st.markdown("---")

# Quote
quotes = [
    "MR GORBACHEV, TEAR DOWN THIS WALL! – REAGAN 1987",
    "WE WIN, THEY LOSE. – RONALD REAGAN",
    "FREEDOM IS NEVER MORE THAN ONE GENERATION AWAY FROM EXTINCTION. – RONALD REAGAN",
    "TRUST BUT VERIFY. – RONALD REAGAN",
]
st.markdown(f'<p class="glow">> DAILY DIRECTIVE: "{random.choice(quotes)}" <span class="cursor"></span></p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.markdown('<h2 class="glow">COMMAND INTERFACE</h2>', unsafe_allow_html=True)
    st.markdown('<p>📞 PHONE: (253) XXX-XXXX</p>')           # ← YOUR REAL PHONE NUMBER
    st.markdown('<p>✉️ EMAIL: lawrence@example.com</p>')     # ← YOUR REAL EMAIL
    st.markdown("---")
    st.markdown('<p class="glow">> STATUS: ONLINE | SEC LEVEL: PATRIOT</p>', unsafe_allow_html=True)

# Main content
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
