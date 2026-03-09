import streamlit as st
import datetime
import random

# ── Page Config ──
st.set_page_config(
    page_title="Lawrence | Home",
    page_icon="🇺🇸",
    layout="wide",
)

# Custom CSS for alive feel: gradients, animations, patriotic colors
st.markdown("""
    <style>
    @keyframes fadeIn { from {opacity: 0;} to {opacity: 1;} }
    .fade-in { animation: fadeIn 1.5s ease-in; }
    .hero { 
        background: linear-gradient(135deg, #b22222, #000080, #ffffff); 
        color: white; padding: 60px 20px; text-align: center; border-radius: 15px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.4); margin-bottom: 30px;
    }
    .big-title { font-size: 70px; font-weight: bold; margin: 0; text-shadow: 3px 3px 6px #000; }
    .subtitle { font-size: 32px; margin: 10px 0; }
    .pulse-button { 
        background: #d32f2f; color: white; font-size: 24px; padding: 15px 40px; 
        border: none; border-radius: 50px; cursor: pointer; transition: all 0.3s;
        box-shadow: 0 5px 15px rgba(211,47,47,0.5);
    }
    .pulse-button:hover { transform: scale(1.08); box-shadow: 0 10px 25px rgba(211,47,47,0.7); }
    .quote { font-style: italic; color: #ffd700; font-size: 22px; margin: 20px 0; }
    .alive-clock { font-size: 18px; color: #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# ── Sidebar (keep or simplify) ──
with st.sidebar:
    st.title("Lawrence 🇺🇸")
    st.markdown("Federal Way, WA • Conservative • Builder")
    st.markdown("### Quick Jump")
    st.markdown("- [THEREALNEWS →](https://therealnews-8q9zgdyymx83erjszxjxgb.streamlit.app/)")

# ── Hero / Alive Section ──
st.markdown('<div class="hero fade-in">', unsafe_allow_html=True)
st.markdown('<p class="big-title">Welcome, Patriot</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Lawrence\'s Corner – Truth, Tech & Freedom</p>', unsafe_allow_html=True)

# Dynamic daily quote (rotate conservative icons)
quotes = [
    "Freedom is never more than one generation away from extinction. — Ronald Reagan",
    "The Constitution is not an instrument for the government to restrain the people, it is an instrument for the people to restrain the government. — Patrick Henry",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. — Martin Luther King Jr.",
    "The tree of liberty must be refreshed from time to time with the blood of patriots and tyrants. — Thomas Jefferson",
]
daily_quote = random.choice(quotes)
st.markdown(f'<p class="quote">"{daily_quote}"</p>', unsafe_allow_html=True)

# Live-ish clock
now = datetime.datetime.now().strftime("%B %d, %Y • %I:%M %p PDT")
st.markdown(f'<p class="alive-clock">Right now in Federal Way: {now}</p>', unsafe_allow_html=True)

# Big pulsing link to THEREALNEWS
st.markdown("""
    <a href="https://therealnews-8q9zgdyymx83erjszxjxgb.streamlit.app/" target="_blank">
        <button class="pulse-button">Go to THEREALNEWS with Lawrence → Real Conservative Feed</button>
    </a>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── Rest of your sections (fade-in for life) ──
st.markdown('<div class="fade-in">', unsafe_allow_html=True)
st.header("About Me")
st.write("Federal Way resident, Python/Streamlit builder, focused on real news from trusted Republican sources. Check out my main project below.")

st.header("Featured Project")
st.subheader("THEREALNEWS with Lawrence")
st.write("Your go-to conservative news aggregator — switch between War, Politics, Economics. War mode includes next-event probabilities.")
st.markdown("[Launch THEREALNEWS →](https://therealnews-8q9zgdyymx83erjszxjxgb.streamlit.app/)")

# Add more sections as before: Skills, Contact, etc.
st.markdown('</div>', unsafe_allow_html=True)

st.caption("Built with Python + Streamlit • Always fighting for truth • 2026")
