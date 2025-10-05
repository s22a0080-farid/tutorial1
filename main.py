import streamlit as st

# ----- PAGE SETUP -----
st.set_page_config(page_title="My Resume", page_icon="📄", layout="centered")

# ----- HEADER SECTION -----
col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://via.placeholder.com/150", caption="Your Name", use_container_width=True)  # Replace with your image path or URL

with col2:
    st.title("Muhammad Farid Bin Mohd Yusop")
    st.write("📍 Location: Melaka, Malaysia")
    st.write("✉️ Email: faridyusop03.com")
    st.write("📞 Phone: +60197605897")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/s2a0080-farid)")

st.markdown("---")

# ----- EDUCATION SECTION -----
st.header("🎓 Education")
st.write("**Bachelor of Information Technology**, University Malaysia Kelantan (2022 – 2026)")
st.write("- Major in Artificial Intelligence")
st.write("- Dean’s List Award (2021, 2022)")

st.markdown("---")

# ----- WORK EXPERIENCE SECTION -----
st.header("💼 Work Experience")
st.write("**Software Developer**, Tech Company (Jun 2025 – Aug 2025)")
st.write("- Developed internal dashboard using Python and Streamlit")

st.write("**Freelance Web Developer** (2022 – Present)")
st.write("- Built personal and business websites using HTML, CSS, and JavaScript")


st.markdown("---")

# ----- SKILLS SECTION -----
st.header("🧠 Skills")
skills_col1, skills_col2 = st.columns(2)

with skills_col1:
    st.write("- Python")
    st.write("- HTML / CSS / JavaScript")
    st.write("- Streamlit")
with skills_col2:
    st.write("- Machine Learning")
    st.write("- SQL")
    st.write("- Git & GitHub")

st.markdown("---")

# ----- PROJECTS SECTION -----
st.header("🚀 Projects & Achievements")
st.write("**Water Leakage Detection IoT System**")
st.write("- Designed an IoT-based system using ESP8266 to detect water leakage in real time")
st.write("- Integrated with a mobile app for instant notifications")

st.write("**Twitter Hate Speech Detection**")
st.write("- Adapted a Transformer model to detect hate speech using PyTorch")
st.write("- Achieved 90% accuracy on test data")

st.markdown("---")

# ----- FOOTER -----
st.markdown(
    """
    <div style='text-align: center; color: grey; font-size: 0.9em;'>
        ©️ 2025 Your Name | Built with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
