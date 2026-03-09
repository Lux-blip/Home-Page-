import streamlit as st
import datetime

st.set_page_config(
    page_title="Lawrence | Federal Way",
    page_icon="🇺🇸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Modern dark theme with patriotic accents
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    body, .stApp {
        font-family: 'Inter', sans-serif !important;
        background: #0f1117 !important;
        color: #e2e8f0 !important;
    }
    .stButton > button {
        background: #dc2626 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 14px 32px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        background: #ef4444 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 25px rgba(220,38,38,0.4) !important;
    }
    h1, h2, h3 {
        color: #f1f5f9 !important;
        font-weight: 700 !important;
    }
    a {
        color: #60a5fa !important;
        text-decoration: none !important;
    }
    a:hover {
        text-decoration: underline !important;
        color: #93c5fd !important;
    }
    .card {
        background: #1e293b !important;
        border-radius: 16px !important;
        padding: 28px !important;
        margin-bottom: 24px !important;
        border: 1px solid #334155 !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }
    .card:hover {
        transform: translateY(-6px) !important;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3) !important;
    }
    hr {
        border-color: #334155 !important;
        margin: 40px 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar – quick nav & contact
with st.sidebar:
    st.title("Lawrence")
    st.caption("Federal Way, Washington • Builder & Truth-Seeker")
    
    st.divider()
    
    st.subheader("Contact")
    st.markdown("**Phone**  \n(509) 552-7109")          # ← YOUR REAL PHONE NUMBER
    st.markdown("**Email**  \nHartmanlawrence291@gmail.com")    # ← YOUR REAL EMAIL
    
    st.divider()
    
    st.markdown("[GitHub](https://github.com/YOURUSERNAME)")
    st.markdown("[X / Twitter](https://x.com/YOURHANDLE)")

# Hero section
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("<h1 style='margin-bottom:0.2rem;'>Hey, I'm Lawrence</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#94a3b8; margin-top:0;'>Federal Way, WA • Conservative • Python Developer</h3>", unsafe_allow_html=True)
    
    st.write("""
    I build tools that cut through the noise. Focused on real information from trusted sources, 
    staying informed on politics, economics, national security, and freedom.
    """)
    
    st.markdown("### My Main Project")
    st.button("→ Visit THEREALNEWS with Lawrence", 
              on_click=lambda: st.markdown("<meta http-equiv='refresh' content='0; url=https://therealnews-8q9zgdyymx83erjszxjxgb.streamlit.app/' />", unsafe_allow_html=True))

with col2:
    # Placeholder for your photo (upload profile.jpg to repo root)
    # st.image("profile.jpg", use_column_width=True, caption="Lawrence")
    st.caption("Photo coming soon – or upload yours")

# Sections in cards
st.divider()

col_left, col_right = st.columns(2)

with col_left:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("About")
        st.write("""
        Living in Federal Way, Washington.  
        Passionate about conservative values, staying informed, and building useful apps with Python & Streamlit.  
        Always open to talk politics, current events, tech, or life in the PNW.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("THEREALNEWS")
        st.write("""
        Real-time conservative news feed from trusted Republican-leaning sources.  
        Switch between War, Politics, Economics.  
        War mode includes next-event probabilities with % chances.
        """)
        st.button("Launch THEREALNEWS →", 
                  on_click=lambda: st.markdown("<meta http-equiv='refresh' content='0; url=https://therealnews-8q9zgdyymx83erjszxjxgb.streamlit.app/' />", unsafe_allow_html=True))
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.divider()
st.caption(f"© {datetime.date.today().year} Lawrence • Built with Python + Streamlit • Hosted on GitHub")
