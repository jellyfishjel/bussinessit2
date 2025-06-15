import streamlit as st
from PIL import Image

# ==== Page Config ====
st.set_page_config(
    page_title="Education Career Success",
    layout="wide"
)

# ==== Apply global styles (Inter font + sidebar color) ====
from utils import apply_global_styles
apply_global_styles()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

# ==== Import Google Fonts + Fade-in CSS ====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter&family=Bungee&display=swap" rel="stylesheet">
    <style>
        .fade-in {
            animation: fadeIn 1.5s ease-in;
        }
        @keyframes fadeIn {
            0% {opacity: 0;}
            100% {opacity: 1;}
        }
    </style>
""", unsafe_allow_html=True)

# ==== HEADER ====
st.markdown("""
    <div style='text-align: center; padding: 5px 20px 30px; margin-top: -60px;'>
        <h1 style='font-family: "Bungee", sans-serif; font-size: 60px; color: #cf5a2e; line-height: 1.0; margin-bottom: 0px;'>
            EDUCATION<br>CAREER<br>SUCCESS
        </h1>
    </div>
""", unsafe_allow_html=True)

# ==== SLOGAN ====
st.markdown("""
 <div class="fade-in" style="text-align: center; max-width: 900px; margin: auto; padding-top: 20px;">
    <p style="font-family: 'Inter', sans-serif; font-size: 25px; color: #cf5a2e; font-weight: bold;">
        Insight into success, powered by data.
    </p>
    <p style="font-family: 'Inter', sans-serif; font-size: 18px; color: #222;">
        Discover how different factors shape career paths—through interactive analytics.
    </p>
    <p style="font-family: 'Inter', sans-serif; font-size: 17px; color: #444;">
        Developed using <b>Python, GitHub, and Streamlit</b> by <b style="color: #cf5a2e;">Team Py7on</b> as part of the Python Project 2 for <b>Business IT 2</b> course at <b>Vietnamese–German University</b>.
    </p>
 </div>
""", unsafe_allow_html=True)

# ==== OUR TEAM Title ====
st.markdown("""
    <div style='text-align: center; font-size: 36px; font-family: "Bungee", sans-serif; color: black; margin-top: 1rem; margin-bottom: 2rem;'>
        OUR TEAM
    </div>
""", unsafe_allow_html=True)

# ==== TEAM MEMBERS ====
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "image/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "image/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "image/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "image/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "image/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "image/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "image/Nguyen Boi Ngoc.png"},
]

# ==== Top row ====
top_row = team_members[:4]
cols_top = st.columns(len(top_row))
for col, member in zip(cols_top, top_row):
    with col:
        st.image(member["image"], width=250)
        st.markdown(
            f"<div style='text-align:center; font-family: \"Inter\", sans-serif; font-weight:bold; font-size:15px; color:black'>{member['name']}</div>",
            unsafe_allow_html=True
        )
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
# ==== Bottom row ====
bottom_row = team_members[4:]
cols_bot = st.columns([1, 3, 3, 3, 1])  # center 3 members
for i, member in enumerate(bottom_row):
    with cols_bot[i + 1]:
        st.image(member["image"], width=300)
        st.markdown(
            f"<div style='text-align:center; font-family: \"Inter\", sans-serif; font-weight:bold; font-size:15px; color:black'>{member['name']}</div>",
            unsafe_allow_html=True
        )
