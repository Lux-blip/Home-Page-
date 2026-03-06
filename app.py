import streamlit as st

st.set_page_config(
    page_title="Lawrence Hartman | THEREALNEWS",
    page_icon="📰",
    layout="wide"
)

# Dark/cozy/formal theme toggle
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=True)

if dark_mode:
    st.markdown("""
    <style>
        .stApp {
            background-color: #0d1117;
            color: #c9d1d9;
        }
        h1, h2, h3 {
            color: #58a6ff !important;
        }
        .contact-card {
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 24px;
            margin: 32px 0;
            box-shadow: 0 4px 16px rgba(0,0,0,0.4);
        }
        .link-btn {
            background: #238636 !important;
            color: white !important;
            border: none !important;
            padding: 12px 24px !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
            display: inline-block !important;
            text-decoration: none !important;
            margin: 16px 0;
        }
        .link-btn:hover {
            background: #2ea043 !important;
        }
        hr {
            border-color: #30363d !important;
        }
    </style>
    """, unsafe_allow_html=True)

# Main content – mature, formal, cozy layout
st.title("Lawrence Hartman")
st.subheader("Federal Way, Washington")

st.markdown("---")

st.markdown("""
### About Me
Hello. I'm Lawrence — a conservative-minded individual from Federal Way, WA.

I created **THEREALNEWS** to provide a focused feed of Republican and right-leaning news sources, with special attention to war-related developments and estimated probabilities of future events.

This is my personal homepage. Feel free to reach out.
""")

# Big link to your news site
news_url = "https://yourusername-therealnews.streamlit.app"  # ← CHANGE THIS to your actual news site URL
st.markdown(
    f'<a href="{news_url}" target="_blank" class="link-btn">→ Visit THEREALNEWS</a>',
    unsafe_allow_html=True
)

st.markdown("---")

# Contact card
st.markdown('<div class="contact-card">', unsafe_allow_html=True)

st.subheader("Contact Information")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Email**")
    st.markdown("Hartmanlawrence291@gmail.com")

with col2:
    st.markdown("**Phone**")
    st.markdown("(509) 552-7109")

st.markdown("**Location**")
st.markdown("Federal Way, Washington, United States")

st.markdown("**Notes**")
st.markdown("- Prefer email for detailed messages")
st.markdown("- Phone calls/texts welcome during reasonable hours (Pacific Time)")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("© 2026 Lawrence Hartman | Built with Streamlit • Conservative perspective")
