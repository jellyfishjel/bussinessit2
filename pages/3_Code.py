import streamlit as st
import os

# ==== Page Config ====
st.set_page_config(page_title="Education & Career Success", layout="wide")

# ==== Global Styles ====
from utils import apply_global_styles
apply_global_styles()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

# ==== Google Fonts ====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter&family=Bungee&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ==== Page Title ====
st.markdown("""
    <h1 style='font-family: "Inter", sans-serif; color: #cf5a2e; font-size: 40px;'>📄 Displayed Code</h1>
""", unsafe_allow_html=True)

# ==== Filter function ====
def is_valid_py_file(file_name):
    excluded = {"__init__.py", "utils.py", "style.py"}
    return file_name.endswith(".py") and file_name not in excluded

# ==== Load .py files from root and pages/ ====
root_files = [f for f in os.listdir(".") if is_valid_py_file(f)]
pages_files = [f"pages/{f}" for f in os.listdir("pages") if is_valid_py_file(f)]
py_files = root_files + pages_files

# ==== Dropdown ====
selected_file = st.selectbox("Select a Python file to display", py_files)

# ==== Display Code ====
try:
    with open(selected_file, "r", encoding="utf-8") as f:
        code_content = f.read()
    st.code(code_content, language='python')
except FileNotFoundError:
    st.warning(f"File `{selected_file}` not found. Please make sure it’s in the correct directory.")
