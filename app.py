import streamlit as st
import datetime
import random

# ── Page config for darker orangish-brown amber terminal ──
st.set_page_config(
    page_title="CIA SAFEHOUSE TERMINAL – LAWRENCE ACCESS",
    page_icon="🖥️",
    layout="wide",
)

# Custom CSS: Darker orangish-brown amber CRT (aged, brownish tint)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

    body, .stApp {
        background-color: #000000 !important;
        color: #cc8800 !important;  /* Darker orangish-brown amber phosphor */
        font-family: 'VT323', monospace !important;
        font-size: 1.5rem !important;
        line-height: 1.4 !important;
    }
    .stMarkdown, h1, h2, h3, p, div, span, a {
        color: #cc8800 !important;
        text-shadow: 0 0 8px #aa6600, 0 0 16px #884400, 0 0 24px #662200;
    }
    /* Aged brownish scanlines */
    .stApp::before {
        content: " ";
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(
            to bottom,
            transparent 0px,
            transparent 4px,
            rgba(180,100,0,0.12) 4px,
            rgba(180,100,0,0.12) 8px
        );
        pointer-events: none;
        z-index: 9999;
    }
    /* Stronger flicker for worn CRT */
    @keyframes flicker {
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% { opacity: 1; transform: translateY(0); }
        20%, 24%, 55% { opacity: 0.85; transform: translateY(2px); }
    }
    .crt-flicker {
        animation: flicker 6s infinite;
    }
    /* Burned-in glow + brownish phosphor bloom */
    .glow {
        text-shadow: 
            0 0 6px #cc8800,
            0 0 12px #aa6600,
            0 0 24px #884400,
            0 0 36px #662200;
    }
    /* Blinking cursor – brownish amber */
    @keyframes blink {
        0%, 49% { opacity: 1; }
        50%, 100% { opacity: 0; }
    }
    .cursor { 
        display: inline-block; 
        width: 14px; 
        height: 1.3em; 
        background: #cc8800; 
        animation: blink 1s step-end infinite; 
        vertical-align: middle;
    }
    /* Heavier vignette + edge burn for aged monitor */
    .vignette {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        pointer-events: none;
        background: radial-gradient(circle at 50% 50%, transparent 20%, rgba(0,0,0,0.9) 100%);
        z-index: 9998;
    }
    hr { border-color: #442200; }  /* Dark brown */
    a { color: #aa6600 !important; text-decoration: underline; }
    .red-alert { color: #aa3300 !important; text-shadow: 0 0 10px #aa3300; }
    </style>
    <div class="vignette"></div>
    """, unsafe_allow_html=True)

# Main content wrapper
st.markdown('<div class="crt-flicker">', unsafe_allow_html=True)

# ── Boot / Login ──
st.markdown('<h1 class="glow">CIA SAFEHOUSE TERMINAL – ACCESS GRANTED</h1>', unsafe_allow_html=True)
st.markdown('<p class="glow">USER: LAWRENCE | LOCATION: FEDERAL WAY WA | ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + ' <span class="cursor"></span></p>', unsafe_allow_html=True)
st.markdown('<p class="red-alert">**CLASSIFIED – LEVEL PATRIOT**</p>', unsafe_allow_html=True)
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
    st.markdown('<p>📞 PHONE: (253) XXX-XXXX</p>')           # ← YOUR REAL PHONE
    st.markdown('<p>✉️ EMAIL: lawrence@example.com</p>')     # ← YOUR REAL EMAIL
    st.markdown("---")
    st.markdown('<p class="glow">> STATUS: ONLINE | SEC LEVEL: PATRIOT</p>', unsafe_allow_html=True)

# Main
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
st.markdown('- PHONE: (253) XXX-XXXX')           # ← YOUR REAL PHONE
st.markdown('- EMAIL: lawrence@example.com')     # ← YOUR REAL EMAIL
st.write('> ACKNOWLEDGE RECEIPT WITHIN 0600 SECONDS. <span class="cursor"></span>', unsafe_allow_html=True)

st.markdown("---")
st.caption("TERMINAL v1.0 – STREAMLIT / PYTHON – CLASSIFIED 2026 – FOR LIBERTY")

st.markdown('</div>', unsafe_allow_html=True)
