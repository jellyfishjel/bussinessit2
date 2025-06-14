import streamlit as st
from PIL import Image

# ==== Page Config ====
st.set_page_config(
    page_title="Education Career Success",
    layout="wide"
)

# ==== Apply Global Styles ====
from utils import apply_global_styles
apply_global_styles()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

# ==== Import Google Fonts + Animation ====
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

# ==== HERO SECTION ====
st.markdown("""
    <div class="fade-in" style='text-align: center; padding: 5px 20px 30px; margin-top: -40px;'>
        <h1 style='font-family: "Bungee", sans-serif; font-size: 60px; color: #cf5a2e; line-height: 1.0; margin-bottom: 0px;'>
            🎓 EDUCATION<br>💼 CAREER<br>🏆 SUCCESS
        </h1>
        <p style="font-family: 'Inter', sans-serif; font-size: 24px; color: #cf5a2e; font-weight: bold; margin-top: 20px;">
            Insight into success, powered by data.
        </p>
        <p style="font-family: 'Inter', sans-serif; font-size: 18px; color: #222;">
            Explore how education, location, and personal factors shape career paths — through interactive, visual analytics.
        </p>
        <p style="font-family: 'Inter', sans-serif; font-size: 17px; color: #444; max-width: 900px; margin: auto;">
            Built using <b>Python, GitHub, and Streamlit</b> by <b style="color: #cf5a2e;">Team Py7on</b> as part of the Python Project 2 for the <b>Business IT 2</b> course at <b>Vietnamese–German University</b>.
        </p>
    </div>
""", unsafe_allow_html=True)

# ==== EXPLORE BUTTON ====
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center;'>"
    "<a href='/'><button style='padding: 0.7em 1.5em; font-size: 18px; background-color: #cf5a2e; color: white; border: none; border-radius: 8px; cursor: pointer;'>🚀 Explore the Dashboard</button></a>"
    "</div>", unsafe_allow_html=True
)

# ==== TEAM SECTION ====
st.markdown("<br><br><div style='text-align: center; font-size: 36px; font-family: \"Bungee\", sans-serif; color: black;'>OUR TEAM</div><br>", unsafe_allow_html=True)

team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "image/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "image/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "image/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "image/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "image/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "image/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "image/Nguyen Boi Ngoc.png"},
]

def show_member_grid(members):
    rows = [members[:4], members[4:]]
    for row in rows:
        cols = st.columns(len(row))
        for col, member in zip(cols, row):
            with col:
                st.image(member["image"], width=250)
                st.markdown(
                    f"<div style='text-align:center; font-family: \"Inter\", sans-serif; font-weight:bold; font-size:15px; color:black'>{member['name']}</div>",
                    unsafe_allow_html=True
                )

show_member_grid(team_members)
