import pandas as pd
import streamlit as st

# ==== Page Config (nên đặt ở đầu) ====
st.set_page_config(page_title="Education & Career Success", layout="wide")

# ==== Load dataset with caching ====
@st.cache_data
def load_data():
    return pd.read_excel("education_career_success.xlsx")

df = load_data()

# ==== Apply global styles ====
from utils import apply_global_styles
apply_global_styles()

# ==== Inject custom CSS & Google Fonts ====
def inject_styles():
    with open("style/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    st.markdown(
        '<link href="https://fonts.googleapis.com/css2?family=Inter&family=Bungee&display=swap" rel="stylesheet">',
        unsafe_allow_html=True
    )

inject_styles()

# ==== Tab Navigation ====
tab1, tab2, tab3 = st.tabs(["📌 Introduction", "📂 Dataset Overview", "📊 Variable Explanation"])

# === TAB 1: INTRODUCTION ===
with tab1:
    st.markdown("""
        <h1 style='font-family: "Inter", sans-serif; color: #cf5a2e; font-size: 40px;'>📌 Introduction</h1>
        <div style="font-family: 'Inter', sans-serif; font-size: 17px; color: #333; line-height: 1.6;">
        <p>The <b>“Education Career Success”</b> dataset provides valuable insights into the relationship between 
        academic background, career progression, and financial outcomes. By delving into various categories of this 
        dataset, we can uncover how different fields of study, academic performance, and practical 
        experiences impact career satisfaction and long-term professional achievements.</p>
    
        <p>This website is a project for our Python course. It contains interactive graphs that visualize information 
        from the dataset using Python libraries such as Pandas and Plotly.</p>
        </div>
    """, unsafe_allow_html=True)

# === TAB 2: DATASET OVERVIEW ===
with tab2:
    st.markdown("<h1 style='font-family: Inter, sans-serif; color: #cf5a2e; font-size: 40px;'>📂 Dataset Overview</h1>", unsafe_allow_html=True)

    st.markdown("""
        <div style="font-family: 'Inter', sans-serif; font-size: 17px; color: #333; line-height: 1.6;">
            <p>This dataset has <b>20 columns</b> and <b>5000 rows</b>, exploring the relationship between academic performance and career success.
            It includes students’ educational backgrounds, skills, and outcomes.</p>
            <p>The dataset can be used to:</p>
            <ul style="margin-left: 20px;">
                <li>Predict job success based on education</li>
                <li>Identify key factors influencing salaries</li>
                <li>Understand the role of networking and internships in career growth</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='font-family: Inter, sans-serif; color: #333; font-size: 30px;'>Dataset</h2>", unsafe_allow_html=True)
    st.dataframe(df)

# === TAB 3: VARIABLE EXPLANATION ===
with tab3:
    st.markdown("""
        <h1 style='font-family: "Inter", sans-serif; color: #cf5a2e; font-size: 40px;'>📊 Variable Explanation</h1>

        <h3 style='font-family: Inter, sans-serif; color: #333;'>1. Student Information</h3>
        <ul style="margin-left: 20px; font-family: Inter, sans-serif; color: #333; font-size: 16px;">
            <li><code>Student_ID</code>: Unique identifier for each student</li>
            <li><code>Age</code>: Age of student (18–30)</li>
            <li><code>Gender</code>: Male, Female, or Others</li>
            <li><code>High_School_GPA</code>: GPA on a 2.0–4.0 scale</li>
            <li><code>SAT_score</code>: SAT test score (900–1600)</li>
            <li><code>University_Ranking</code>: University ranking (1–1000)</li>
            <li><code>University_GPA</code>: GPA in university (2.0–4.0)</li>
            <li><code>Field_of_Study</code>: Major field (Arts, Law, Business, etc.)</li>
        </ul>

        <h3 style='font-family: Inter, sans-serif; color: #333;'>2. Academic Performance</h3>
        <ul style="margin-left: 20px; font-family: Inter, sans-serif; color: #333; font-size: 16px;">
            <li><code>Internships_Completed</code>: Number of internships (0–4)</li>
            <li><code>Projects_Completed</code>: Academic/personal projects (0–9)</li>
            <li><code>Certifications</code>: Certifications earned (0–5)</li>
            <li><code>Soft_Skills_Score</code>: Soft skills rating (1–10)</li>
            <li><code>Networking_Score</code>: Connections/networking score (1–10)</li>
        </ul>

        <h3 style='font-family: Inter, sans-serif; color: #333;'>3. Career Outcomes</h3>
        <ul style="margin-left: 20px; font-family: Inter, sans-serif; color: #333; font-size: 16px;">
            <li><code>Job_Offers</code>: Number of job offers after graduation (0–5)</li>
            <li><code>Starting_Salary</code>: First salary (USD $25,000–$150,000)</li>
        </ul>
    """, unsafe_allow_html=True)
