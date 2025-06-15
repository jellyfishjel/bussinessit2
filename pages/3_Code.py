import streamlit as st


# Page config
st.set_page_config(page_title="Education & Career Success", layout="wide")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


# Google Fonts
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter&family=Bungee&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)


# === Page Title ===
st.markdown("""
    <h1 style='font-family: "Inter", sans-serif; color: #cf5a2e; font-size: 40px;'>📄 Displayed Code</h1>
""", unsafe_allow_html=True)


# === Load .py File Dynamically ===
uploaded_file = st.text_input("Enter Python filename", value="2_Chart.py")


try:
    with open(uploaded_file, "r", encoding="utf-8") as f:
        code_content = f.read()
    st.code(code_content, language='python')
except FileNotFoundError:
    st.warning(f"File `{uploaded_file}` not found. Please make sure it’s in the same directory.")
