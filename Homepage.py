import streamlit as st
from PIL import Image

# ==== Page Config ====
st.set_page_config(
    page_title="Education Career Success",
    layout="wide"
)

# ==== Global Style ====
from utils import apply_global_styles
apply_global_styles()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")

# ==== Font & Animation CSS ====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Bungee&display=swap" rel="stylesheet">
    <style>
        .fade-in { animation: fadeIn 1.5s ease-in; }
        @keyframes fadeIn {
            0% {opacity: 0;}
            100% {opacity: 1;}
        }
        .hero-box {
            background: rgba(255,255,255,0.8);
            padding: 40px 30px;
            border-radius: 20px;
            display: inline-block;
            max-width: 900px;
        }
    </style>
""", unsafe_allow_html=True)

# ==== HERO Section ====
st.markdown("""
<div class="fade-in" style='text-align: center; margin-top: -30px;'>
    <div class="hero-box">
        <h1 style='font-family: "Bungee", sans-serif; font-size: 60px; color: #cf5a2e; margin-bottom: 10px;'>
            🎓 EDUCATION · 💼 CAREER · 🏆 SUCCESS
        </h1>
        <p style="font-family: 'Inter', sans-serif; font-size: 22px; color: #cf5a2e; font-weight: 600;">
            Turning educational data into career insight.
        </p>
        <p style="font-family: 'Inter', sans-serif; font-size: 18px; color: #333; margin-top: 25px;">
            This interactive platform analyzes how education level, field of study, gender, and location 
            impact career outcomes. Our goal is to help you explore data-driven insights into career success, 
            based on real global statistics.
        </p>
        <p style="font-family: 'Inter', sans-serif; font-size: 16px; color: #555;">
            Built using <b>Python, GitHub, and Streamlit</b> by <b style="color: #cf5a2e;">Team Py7on</b> 
            as part of the <b>Python Project 2</b> for the <b>Business IT 2</b> course at 
            <b>Vietnamese–German University</b>.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ==== CTA Button ====
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center;">
    <a href="/" style="text-decoration: none;">
        <button style="
            background-color: #cf5a2e;
            color: white;
            font-size: 18px;
            padding: 12px 30px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-family: 'Inter', sans-serif;
        ">
            🚀 Explore the Dashboard
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# ==== OUR TEAM ====
st.markdown("<br><br><div style='text-align: center; font-size: 36px; font-family: \"Bungee\", sans-serif; color: black;'>OUR TEAM</div><br>", unsafe_allow_html=True)

# ==== Member Data ====
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "image/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "image/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "image/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "image/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "image/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "image/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "image/Nguyen Boi Ngoc.png"},
]

# ==== Show Team Grid ====
def show_member_grid(members, n_cols=4):
    for i in range(0, len(members), n_cols):
        row = members[i:i+n_cols]
        cols = st.columns(len(row))
        for col, member in zip(cols, row):
            with col:
                st.image(member["image"], width=200)
                st.markdown(
                    f"<div style='text-align:center; font-family: Inter; font-size:15px; font-weight:600; color:#222'>{member['name']}</div>",
                    unsafe_allow_html=True
                )

show_member_grid(team_members)

