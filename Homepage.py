import streamlit as st
from PIL import Image



# ==== Page Config ====
st.set_page_config(
    page_title="Education Career App",
    layout="wide"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

# ==== Import font ====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)


# ==== Global CSS ====
st.markdown("""
     <style>
        .homepage {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 80px 20px 80px;
        }

        .homepage h1 {
            font-family: 'Bungee', sans-serif;
            font-size: 64px;
            color: #cf5a2e;
            line-height: 1.2;
            margin-bottom: 10px;
        }

        .team-title {
            text-align: center;
            font-size: 36px;
            font-family: 'Bungee', sans-serif;
            color: black;
            margin-bottom: 3rem;
            margin-top: 3rem;
        }
     </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="homepage">
        <h1>EDUCATION<br>CAREER<br>SUCCESS</h1>
    </div>
""", unsafe_allow_html=True)

# ==== OUR TEAM section ====
st.markdown('<a name="team"></a>', unsafe_allow_html=True)
st.markdown('<div class="team-title">OUR TEAM</div>', unsafe_allow_html=True)


# ==== Danh sách thành viên ====
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
        st.markdown( f"<div style='text-align:center; font-weight:bold; font-size:15px; color:black'>{member['name']}</div>", unsafe_allow_html=True)

# ==== Spacing ====
st.markdown("<div class='row-spacing'></div>", unsafe_allow_html=True)

# ==== Bottom row (3 people centered) ====
bottom_row = team_members[4:]
cols_bot = st.columns([1, 3, 3, 3, 1])  # center 3 members
for i, member in enumerate(bottom_row):
    with cols_bot[i + 1]:
        st.image(member["image"], width=300)
        st.markdown(f"<div style='text-align:center; font-weight:bold; font-size:15px; color:black'>{member['name']}</div>", unsafe_allow_html=True)
