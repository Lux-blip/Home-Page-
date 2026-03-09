import streamlit as st
import datetime
import random

# ── Page config ──
st.set_page_config(
    page_title="CIA SAFEHOUSE TERMINAL – LAWRENCE ACCESS",
    page_icon="🖥️",
    layout="wide",
)

# Custom CSS: Authentic Black Ops Cold War safehouse terminal (ARPANET green phosphor CRT)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
    body, .stApp { background-color: #000 !important; }
    .bezel {
        background: #111;
        border-radius: 25px;
        padding: 30px;
        box-shadow: 
            inset 0 0 50px rgba(0,0,0,0.8),
            0 0 100px rgba(0,255,65,0.3),
            inset 0 0 200px rgba(0,0,0,0.5);
        margin: 20px auto;
        max-width: 1400px;
        position: relative;
    }
    .screen {
        background: #000;
        border-radius: 20px;
        padding: 40px;
        font-family: 'VT323', monospace !important;
        font-size: 1.8rem !important;
        color: #0f0 !important;
        line-height: 1.5;
        text-shadow: 0 0 10px #0f0, 0 0 20px #0f0, 0 0 30px #0a0;
        position: relative;
        overflow: hidden;
    }
    .scanlines::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(
            0deg, transparent, transparent 2px,
            rgba(0,255,0,0.05) 2px, rgba(0,255,0,0.05) 4px
        );
        pointer-events: none;
    }
    @keyframes flicker { 0%,95%{opacity:1;} 96%,99%{opacity:0.95;} 100%{opacity:1;} }
    .screen { animation: flicker 0.15s infinite; }
    .glow { text-shadow: 0 0 15px #0f0, 0 0 30px #0f0, 0 0 45px #0a0 !important; }
    @keyframes blink { 0%,50%{opacity:1;} 51%,100%{opacity:0;} }
    .cursor { display: inline-block; width: 16px; height: 1.4em; background: #0f0; 
              animation: blink 1s step-end infinite; vertical-align: middle; }
    .alert { color: #f00 !important; text-shadow: 0 0 15px #f00 !important; }
    a { color: #0cc !important; text-decoration: none; }
    a:hover { text-shadow: 0 0 20px #0cc !important; }
    </style>
    """, unsafe_allow_html=True)

# CRT Bezel wrapper
st.markdown('<div class="bezel"><div class="screen scanlines">', unsafe_allow_html=True)

# ARPANET Boot Screen (from screenshot)
st.markdown('<div class="glow">ARPANET INFORMATION SYSTEMS</div>', unsafe_allow_html=True)
st.markdown('<div class="glow">C.I.A.-DOD-VT-100-11320</div>', unsafe_allow_html=True)
st.markdown('<div class="glow">02/18/12 24:81</div>', unsafe_allow_html=True)

st.markdown("""
<div class="glow">
This system is the property of the United States Government.
Unauthorized access is prohibited.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Login
st.markdown('<div class="glow">LOGIN: LAWRENCE<span class="cursor"></span></div>', unsafe_allow_html=True)
st.markdown('<div class="glow">PASS: ***** ACCESS GRANTED<span class="cursor"></span></div>', unsafe_allow_html=True)

st.markdown('<div class="alert">**CLASSIFIED – PATRIOT LEVEL**</div>', unsafe_allow_html=True)
st.markdown("---")

# Help commands like in game
st.markdown('<div class="glow">> HELP</div>', unsafe_allow_html=True)
st.markdown("""
<div class="glow">
DIR  ... displays this help information
CAT  ... displays contents of file or directory
LOGIN  ... displays current login session
RLOGIN  ... attempts login session on remote system
WHO  ... lists users that have accounts on current system
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="glow">SORCERER  TYNE  NHG  PHOBOS</div>', unsafe_allow_html=True)
st.markdown('<div class="glow">ZORK1  ZORK2  ZORK3  WOMBAT</div>', unsafe_allow_html=True)

st.markdown("---")

# Daily directive
quotes = [
    "MR GORBACHEV TEAR DOWN THIS WALL REAGAN 1987",
    "WE WIN THEY LOSE RONALD REAGAN",
    "TRUST BUT VERIFY RONALD REAGAN",
]
st.markdown(f'<div class="glow">> DAILY DIRECTIVE: {random.choice(quotes)}<span class="cursor"></span></div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar commands
with st.sidebar:
    st.markdown('<div class="glow">> COMMAND MENU</div>', unsafe_allow_html=True)
    st.markdown("📞 PHONE: (253) XXX-XXXX")  # YOUR PHONE
    st.markdown("✉️ EMAIL: lawrence@example.com")  # YOUR EMAIL
    st.markdown("---")
    st.markdown('<div class="glow">STATUS: ONLINE</div>', unsafe_allow_html=True)

# Main commands
st.markdown('<div class="glow">> DIR</div>', unsafe_allow_html=True)
st.markdown("""
<div class="glow">
LAWRENCE.PROFILE
THEREALNEWS.EXE
CONTACT.DAT
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="glow">> CAT LAWRENCE.PROFILE<span class="cursor"></span></div>', unsafe_allow_html=True)
st.write("""
OPERATOR: LAWRENCE
LOCATION: FEDERAL WAY COMMAND POST WA
MISSION: CONSERVATIVE TRUTH FEEDS
PRIMARY: THEREALNEWS TERMINAL
""")

st.markdown('<div class="glow">> RUN THEREALNEWS.EXE</div>', unsafe_allow_html=True)
st.markdown("""
<div class="glow">
> <a href="https://therealnews-8q9zgdyymx83erjszxjxgb.streamlit.app/" target="_blank">
LAUNCH WAR/POLITICS/ECONOMICS ANALYSIS
</a><span class="cursor"></span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="glow">> CAT CONTACT.DAT</div>', unsafe_allow_html=True)
st.markdown('- PHONE: (253) XXX-XXXX')  # YOUR PHONE
st.markdown('- EMAIL: lawrence@example.com')  # YOUR EMAIL
st.markdown('<div class="glow">> ACKNOWLEDGE WITHIN 0600 SEC<span class="cursor"></span></div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("TERMINAL v1.0 STREAMLIT PYTHON CLASSIFIED 2026 LIBERTY")

st.markdown('</div></div>', unsafe_allow_html=True)
