import streamlit as st
import datetime
import random

# ── Page config for retro terminal ──
st.set_page_config(
    page_title="LAWRENCE TERMINAL v1.0 – FEDERAL WAY COMMAND",
    page_icon="🖥️",
    layout="wide",
)

# Custom CSS: Cold War CRT terminal aesthetic
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

    body, .stApp {
        background-color: #000000 !important;
        color: #00ff41 !important;
        font-family: 'VT323', monospace !important;
        font-size: 1.4rem !important;
    }
    .stMarkdown, h1, h2, h3, p, div, span, a {
        color: #00ff41 !important;
        text-shadow: 0 0 5px #00ff41, 0 0 10px #00ff41, 0 0 15px #00ff41;
    }
    /* Scanlines */
    .stApp::before {
        content: " ";
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(
            to bottom,
            transparent 0px,
            transparent 2px,
            rgba(0,0,0,0.18) 2px,
            rgba(0,0,0,0.18) 4px
        );
        pointer-events: none;
        z-index: 9999;
    }
    /* Gentle flicker (whole screen) */
    @keyframes flicker {
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% { opacity: 1; }
        20%, 24%, 55% { opacity: 0.92; }
    }
    .crt-flicker {
        animation: flicker 10s infinite;
    }
    /* Glow + phosphor bloom */
    .glow {
        text-shadow: 
            0 0 4px #00ff41,
            0 0 8px #00ff41,
            0 0 12px #00ff41,
            0 0 20px #00ff41;
    }
    /* Blinking cursor simulation */
    @keyframes blink {
        0%, 49% { opacity: 1; }
        50%, 100% { opacity: 0; }
    }
    .cursor { 
        display: inline-block; 
        width: 12px; 
        height: 1.2em; 
        background: #00ff41; 
        animation: blink 1s step-end infinite; 
        vertical-align: middle;
    }
    /* Vignette for old CRT edges */
    .vignette {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        pointer-events: none;
        background: radial-gradient(circle at 50% 50%, transparent 40%, rgba(0,0,0,0.7) 100%);
        z-index: 9998;
    }
    hr { border-color: #004d1a; }
    a { color: #00cc33 !important; text-decoration: underline; }
    </style>
    <div class="vignette"></div>
    """, unsafe_allow_html=True)

# Wrap main content in crt-flicker class
st.markdown('<div class="crt-flicker">', unsafe_allow_html=True)

# ── Header / Boot screen style ──
st.markdown('<h1 class="glow">LAWRENCE PERSONAL TERMINAL – ACCESS GRANTED</h1>', unsafe_allow_html=True)
st.markdown('<p>USER: LAWRENCE | LOCATION: FEDERAL WAY, WA | DATE: ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M PDT") + ' <span class="cursor"></span></p>', unsafe_allow_html=True)
st.markdown("---")

# Rotating Cold War / conservative quote
quotes = [
    "MR. GORBACHEV, TEAR DOWN THIS WALL! – RONALD REAGAN, 1987",
    "WE WIN, THEY LOSE. – RONALD REAGAN",
    "FREEDOM IS NEVER MORE THAN ONE GENERATION AWAY FROM EXTINCTION. – RONALD REAGAN",
    "TRUST BUT VERIFY. – RONALD REAGAN",
]
st.markdown(f'<p class="glow">> DAILY COMMAND DIRECTIVE: "{random.choice(quotes)}" <span class="cursor"></span></p>', unsafe_allow_html=True)
st.markdown("---")

# ── Sidebar: Classified style ──
with st.sidebar:
    st.markdown('<h2 class="glow">COMMAND MENU</h2>', unsafe_allow_html=True)
    st.markdown('<p>📞 PHONE: (253) XXX-XXXX</p>')           # ← CHANGE TO YOUR REAL PHONE NUMBER
    st.markdown('<p>✉️ EMAIL: lawrence@example.com</p>')     # ← CHANGE TO YOUR REAL EMAIL
    st.markdown("---")
    st.markdown('<p class="glow">> STATUS: ONLINE | SEC LEVEL: PATRIOT</p>', unsafe_allow_html=True)

# ── Main sections in terminal style ──
st.subheader(">> SYSTEM OVERVIEW")
st.write("""
OPERATOR: Lawrence  
LOCATION: Federal Way Command Post, Washington  
MISSION: Disseminate truth via conservative intelligence feeds  
PRIMARY ASSET: THEREALNEWS with Lawrence
""")

st.subheader(">> PRIMARY LINK – LAUNCH THEREALNEWS")
st.markdown("""
<p class="glow">
<a href="https://therealnews-8q9zgdyymx83erjszxjxgb.streamlit.app/" target="_blank">
>> ACCESS THEREALNEWS TERMINAL – WAR / POLITICS / ECONOMICS ANALYSIS
</a> <span class="cursor"></span>
</p>
""", unsafe_allow_html=True)

st.subheader(">> CONTACT PROTOCOL")
st.write("Transmit message via secure channel:")
st.markdown('- PHONE: (253) XXX-XXXX')           # ← CHANGE TO YOUR REAL PHONE NUMBER
st.markdown('- EMAIL: lawrence@example.com')     # ← CHANGE TO YOUR REAL EMAIL
st.write('Acknowledge receipt within 0600 seconds. <span class="cursor"></span>', unsafe_allow_html=True)

st.markdown("---")
st.caption("TERMINAL v1.0 – BUILT WITH PYTHON / STREAMLIT – CLASSIFIED 2026 – FOR LIBERTY")

st.markdown('</div>', unsafe_allow_html=True)  # end crt-flicker
