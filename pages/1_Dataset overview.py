import pandas as pd
import streamlit as st

# Load dataset
@st.cache_data
def load_data():
    return pd.read_excel("education_career_success.xlsx")

df = load_data()

# Page config
st.set_page_config(page_title="Education & Career Success", layout="wide")

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Import Google Fonts
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Create tab navigation
tab1, tab2, tab3 = st.tabs(["📌 Introduction", "📂 Dataset Overview", "📊 Variable Explanation"])

# === TAB 1: INTRODUCTION ===
with tab1:
    st.markdown("<h1 class='main-title'>📌 Introduction</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='intro-text'>
        <p>The <b>“Education Career Success”</b> dataset provides valuable insights into the relationship
        between academic background, career progression, and financial outcomes. By delving into various
        categories of this dataset, we can uncover valuable insights into how different fields of study,
        academic performance, and practical experiences impact career satisfaction, work-life balance, and
        long-term professional achievements.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='intro-text'>
        <p>This report is our project for R for Data Science course. The report contains plots that are created
        by using RStudio to visualize information from the dataset in a more accessible way. Each diagram
        is followed by a detailed description and code from RStudio to provide readers with clear
        explanation on statistical data and how RStudio is used in practical data analysis.</p>
    </div>
    """, unsafe_allow_html=True)

# === TAB 2: DATASET OVERVIEW ===
with tab2:
    st.markdown("<h1 class='main-title'>📂 Dataset Overview</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='intro-text'>
        <p>This dataset has <b>20 columns</b> and <b>5000 rows</b>, exploring the relationship between academic performance and career success.  
        It includes students' educational backgrounds, skills, and career outcomes.  
        The dataset can be used for:</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='intro-text'>
        <ul>
            <li>Predicting job success based on education</li>
            <li>Identifying key factors influencing salaries</li>
            <li>Understanding the role of networking and internships in career growth</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2 class='orange-title'>Preview of Dataset</h2>", unsafe_allow_html=True)
    st.dataframe(df.head())

# === TAB 3: VARIABLE EXPLANATION ===
with tab3:
    st.markdown("<h1 class='main-title'>📊 Variable Explanation</h1>", unsafe_allow_html=True)

    # Section 1: Student Information
    st.markdown("<h3 class='section-title'>1. Student Information</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='variable-list'>
        <ul>
            <li><code>Student_ID</code>: Order number to identify each student</li>
            <li><code>Age</code>: Age of student (18–30 years old)</li>
            <li><code>Gender</code>: Male, Female, or Others</li>
            <li><code>High_School_GPA</code>: GPA in high school (2.0–4.0 scale)</li>
            <li><code>SAT_score</code>: Standardized SAT test score (900–1600)</li>
            <li><code>University_Ranking</code>: Rank of the university attended (1–1000)</li>
            <li><code>University_GPA</code>: GPA in university (2.0–4.0 scale)</li>
            <li><code>Field_of_Study</code>: Student’s major (Arts, Law, Business, Medicine, CS, Engineering, Math)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Section 2: Academic Performance
    st.markdown("<h3 class='section-title'>2. Academic Performance</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='variable-list'>
        <ul>
            <li><code>Internships_Completed</code>: Number of internships (0–4)</li>
            <li><code>Projects_Completed</code>: Number of academic/personal projects (0–9)</li>
            <li><code>Certifications</code>: Number of additional certifications earned (0–5)</li>
            <li><code>Soft_Skills_Score</code>: Soft skills rating (1–10)</li>
            <li><code>Networking_Score</code>: Networking and connections score (1–10)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Section 3: Career Outcomes
    st.markdown("<h3 class='section-title'>3. Career Outcomes</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='variable-list'>
        <ul>
            <li><code>Job_Offers</code>: Number of job offers post-graduation (0–5)</li>
            <li><code>Starting_Salary</code>: First job salary in USD ($25,000–$150,000)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
