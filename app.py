import streamlit as st
import datetime
import random

st.set_page_config(
    page_title="CIA SAFEHOUSE TERMINAL – LAWRENCE ACCESS",
    page_icon="🖥️",
    layout="wide",
)

# Enhanced CSS: Smooth, immersive Black Ops Cold War CRT (green phosphor + polish)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

    body, .stApp {
        background: #000 !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
    }

    .crt-container {
        max-width: 1400px;
        margin: 30px auto;
        background: #0a0a0a;
        border-radius: 28px;
        padding: 35px;
        box-shadow: 
            inset 0 0 80px rgba(0,255,80,0.15),
            0 0 120px rgba(0,255,80,0.25),
            inset 0 0 200px rgba(0,0,0,0.9);
        border: 12px solid #111;
        position: relative;
    }

    .crt-screen {
        background: #000;
        border-radius: 18px;
        padding: 45px 50px;
        font-family: 'VT323', monospace !important;
        font-size: 1.9rem !important;
        color: #00ff41 !important;
        line-height: 1.55;
        text-shadow: 0 0 12px #00ff41, 0 0 24px #00cc33, 0 0 36px #009922;
        position: relative;
        overflow: hidden;
        min-height: 70vh;
    }

    /* Smooth scanlines */
    .scanlines::before {
        content: '';
        position: absolute;
        inset: 0;
        background: repeating-linear-gradient(
            to bottom,
            transparent 0px,
            transparent 3px,
            rgba(0,255,65,0.08) 3px,
            rgba(0,255,65,0.08) 6px
        );
        pointer-events: none;
        z-index: 10;
    }

    /* Gentle, smooth flicker + pulse glow */
    @keyframes soft-flicker {
        0%, 92%, 94%, 96%, 100% { opacity: 1; }
        93%, 95% { opacity: 0.96; }
    }
    .crt-screen { animation: soft-flicker 12s infinite; }

    @keyframes glow-pulse {
        0%, 100% { text-shadow: 0 0 12px #00ff41, 0 0 24px #00cc33; }
        50% { text-shadow: 0 0 18px #00ff41, 0 0 36px #00cc33, 0 0 48px #009922; }
    }
    .glow { animation: glow-pulse 6s infinite ease-in-out; }

    /* Blinking cursor – smooth & sharp */
    @keyframes blink-smooth {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0; }
    }
    .cursor {
        display: inline-block;
        width: 18px;
        height: 1.5em;
        background: #00ff41;
        margin-left: 4px;
        animation: blink-smooth 1.1s step-end infinite;
        vertical-align: middle;
    }

    /* Vignette for curved CRT edges */
    .vignette {
        position: absolute;
        inset: 0;
        background: radial-gradient(circle at 50% 50%, transparent 45%, rgba(0,0,0,0.75) 100%);
        pointer-events: none;
        z-index: 5;
    }

    hr { border: none; border-top: 2px solid #003300; margin: 25px 0; }

    a {
        color: #00ccff !important;
        text-decoration: none;
        transition: all 0.3s;
    }
    a:hover {
        text-shadow: 0 0 25px #00ccff, 0 0 40px #0099cc;
        color: #00ffff !important;
    }

    .alert { color: #ff0044 !important; text-shadow: 0 0 15px #ff0044; }
    </style>
    """, unsafe_allow_html=True)

# CRT frame
st.markdown('<div class="crt-container"><div class="crt-screen scanlines"><div class="vignette"></div>', unsafe_allow_html=True)

# Boot sequence – smooth & cinematic
st.markdown('<div class="glow">C.I.A. SAFEHOUSE TERMINAL – ACCESS VERIFIED</div>', unsafe_allow_html=True)
st.markdown(f'<div>USER: LAWRENCE | FEDERAL WAY WA | {datetime.datetime.now().strftime("%Y-%m-%d %H:%M PDT")} <span class="cursor"></span></div>', unsafe_allow_html=True)
st.markdown('<div class="alert">**CLASSIFIED – PATRIOT CLEARANCE**</div>', unsafe_allow_html=True)
st.markdown("---")

# Daily directive
quotes = [
    "MR. GORBACHEV, TEAR DOWN THIS WALL! – REAGAN 1987",
    "WE WIN, THEY LOSE. – RONALD REAGAN",
    "TRUST BUT VERIFY. – RONALD REAGAN",
    "FREEDOM IS A FRAGILE THING... – REAGAN",
]
st.markdown(f'<div class="glow">> DAILY BRIEFING: "{random.choice(quotes)}" <span class="cursor"></span></div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar – clean & thematic
with st.sidebar:
    st.markdown('<div class="glow">> COMMAND CONSOLE</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("📞 PHONE: (253) XXX-XXXX")  # ← YOUR REAL PHONE NUMBER
    st.markdown("✉️ EMAIL: lawrence@example.com")  # ← YOUR REAL EMAIL
    st.markdown("---")
    st.markdown('<div class="glow">STATUS: ACTIVE | SEC LEVEL: PATRIOT</div>', unsafe_allow_html=True)

# Main content – command style, smooth flow
st.markdown('<div class="glow">> DIR /HOME/LAWRENCE</div>', unsafe_allow_html=True)
st.write("""
OPERATOR......... LAWRENCE
LOCATION......... FEDERAL WAY COMMAND POST
PRIMARY MISSION.. CONSERVATIVE TRUTH DISSEMINATION
KEY ASSET........ THEREALNEWS TERMINAL
""")

st.markdown("---")

st.markdown('<div class="glow">> EXECUTE THEREALNEWS</div>', unsafe_allow_html=True)
st.markdown("""
<div class="glow">
> <a href="https://therealnews-8q9zgdyymx83erjszxjxgb.streamlit.app/" target="_blank">
LAUNCH THEREALNEWS – WAR / POLITICS / ECONOMICS FEED
</a> <span class="cursor"></span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown('<div class="glow">> CAT CONTACT.INFO</div>', unsafe_allow_html=True)
st.markdown(f'- PHONE: (253) XXX-XXXX')  # ← YOUR REAL PHONE
st.markdown(f'- EMAIL: lawrence@example.com')  # ← YOUR REAL EMAIL
st.markdown('<div class="glow">> TRANSMIT & ACKNOWLEDGE <span class="cursor"></span></div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("TERMINAL v1.0 – STREAMLIT / PYTHON – CLASSIFIED 2026 – LIBERTY & TRUTH")

st.markdown('</div></div>', unsafe_allow_html=True)
