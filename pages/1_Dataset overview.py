import pandas as pd
import streamlit as st
import plotly.express as px

# Load dataset
@st.cache_data
def load_data():
    return pd.read_excel("education_career_success.xlsx")

df = load_data()

# Page config
st.set_page_config(page_title="Education & Career Success", layout="wide")

# ==== Apply global styles (Inter font + sidebar color) ====
from utils import apply_global_styles
apply_global_styles()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

# Google Fonts
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter&family=Bungee&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Tab navigation
tab1, tab2, tab3 = st.tabs(["📌 Introduction", "📂 Dataset Overview", "📊 Variable Explanation"])

# === TAB 1: INTRODUCTION ===
with tab1:
    st.markdown("""
        <h1 style='font-family: "Inter", sans-serif; color: #cf5a2e; font-size: 40px;'>📌 Introduction</h1>
        <div style="font-family: 'Inter', sans-serif; font-size: 17px; color: #333; line-height: 1.6;">
        <p>The <b>“Education Career Success”</b> dataset provides valuable insights into the relationship
        between academic background, career progression, and financial outcomes...</p>
        <p>This report is our project for R for Data Science course...</p>
        </div>
    """, unsafe_allow_html=True)

# === TAB 2: DATASET OVERVIEW ===
with tab2:
    st.markdown("<h1 style='font-family: Inter, sans-serif; color: #cf5a2e; font-size: 40px;'>📂 Dataset Overview</h1>", unsafe_allow_html=True)

    st.markdown("""
        <div style="font-family: 'Inter', sans-serif; font-size: 17px; color: #333; line-height: 1.6;">
            <p>This dataset has <b>20 columns</b> and <b>5000 rows</b>, exploring the relationship...</p>
        </div>
    """, unsafe_allow_html=True)

    # Filter section
    st.markdown("<h2 style='font-family: Inter, sans-serif; color: #333; font-size: 30px;'>🎛️ Filter & Quick Statistics</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        genders = df["Gender"].dropna().unique()
        selected_gender = st.multiselect("Select Gender(s):", genders, default=list(genders))
    with col2:
        fields = df["Field_of_Study"].dropna().unique()
        selected_field = st.multiselect("Select Field(s) of Study:", fields, default=list(fields))

    filtered_df = df[df["Gender"].isin(selected_gender) & df["Field_of_Study"].isin(selected_field)]

    # Stats
    st.markdown("#### ✅ Quick Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students", len(filtered_df))
    col2.metric("Avg. University GPA", f"{filtered_df['University_GPA'].mean():.2f}")
    col3.metric("Avg. Starting Salary", f"${filtered_df['Starting_Salary'].mean():,.0f}")

    # Chart
    st.markdown("#### 📊 Number of Students by Field of Study")
    field_counts = filtered_df["Field_of_Study"].value_counts().reset_index()
    field_counts.columns = ["Field of Study", "Count"]
    fig = px.bar(field_counts, x="Field of Study", y="Count", color="Field of Study", title="Students per Field of Study")
    st.plotly_chart(fig, use_container_width=True)

    # Data
    st.markdown("<h2 style='font-family: Inter, sans-serif; color: #333; font-size: 30px;'>📄 Dataset</h2>", unsafe_allow_html=True)
    st.dataframe(filtered_df, use_container_width=True)

# === TAB 3: VARIABLE EXPLANATION ===
with tab3:
    st.markdown("""
        <h1 style='font-family: "Inter", sans-serif; color: #cf5a2e; font-size: 40px;'>📊 Variable Explanation</h1>
    """, unsafe_allow_html=True)

    # Student Info
    st.markdown("""
        <h3 style='font-family: Inter, sans-serif; color: #333;'>1. Student Information</h3>
        <ul style="margin-left: 20px; font-family: Inter, sans-serif; color: #333; font-size: 16px;">
            <li><code>Student_ID</code>: Unique ID</li>
            <li><code>Age</code>: 18–30</li>
            ...
        </ul>
    """, unsafe_allow_html=True)

    # Academic
    st.markdown("""
        <h3 style='font-family: Inter, sans-serif; color: #333;'>2. Academic Performance</h3>
        <ul style="...">
            <li><code>Internships_Completed</code>: 0–4</li>
            ...
        </ul>
    """, unsafe_allow_html=True)

    # Career
    st.markdown("""
        <h3 style='font-family: Inter, sans-serif; color: #333;'>3. Career Outcomes</h3>
        <ul style="...">
            <li><code>Job_Offers</code>: 0–5</li>
            <li><code>Starting_Salary</code>: $25,000–$150,000</li>
        </ul>
    """, unsafe_allow_html=True)
