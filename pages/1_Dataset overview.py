import pandas as pd
import streamlit as st

# Load dataset
@st.cache_data
def load_data():
    return pd.read_excel("education_career_success.xlsx")

df = load_data()

# Set up the app layout
st.set_page_config(page_title="Education & Career Success", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Create tab navigation
tab1, tab2, tab3 = st.tabs(["📌 Introduction", "📂 Dataset Overview", "📊 Variable Explanation"])


# --- Tab 1: Introduction ---
with tab1:
    st.header("📌 Introduction")
    st.markdown("""
    <div style='font-family: Inter, sans-serif; font-size: 17px;'>
        <p>The “Education and Career Success” dataset provides valuable insights into the relationship
        between academic background, career progression, and financial outcomes. By delving into various
        categories of this dataset, we can uncover valuable insights into how different fields of study,
        academic performance, and practical experiences impact career satisfaction, work-life balance, and
        long-term professional achievements.</p>

        <p>This report is our project for R for Data Science course. The report contains plots that are created
        by using RStudio to visualize information from the dataset in a more accessible way. Each diagram
        is followed by a detailed description and code from RStudio to provide readers with clear
        explanation on statistical data and how RStudio is used in practical data analysis.</p>
    </div>
    """, unsafe_allow_html=True)


# --- Tab 2: Dataset Overview ---
with tab2:
    st.header("📂 Dataset Overview")
    st.markdown("""
    <div style='font-family: Inter, sans-serif; font-size: 17px;'>
        <p>This dataset has <strong>20 columns</strong> and <strong>5000 rows</strong>, exploring the relationship
        between academic performance and career success.</p>

        <p>It includes students' educational backgrounds, skills, and career outcomes.</p>

        <p>The dataset can be used for:</p>
        <ul>
            <li>Predicting job success based on education</li>
            <li>Identifying key factors influencing salaries</li>
            <li>Understanding the role of networking and internships in career growth</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Preview of Dataset")
    st.dataframe(df.head())


# --- Tab 3: Variable Explanation ---
with tab3:
    st.header("📊 Variable Explanation")
    st.markdown("""
    <div style='font-family: Inter, sans-serif; font-size: 17px;'>

    <h4>1. Student Information</h4>
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

    <h4>2. Academic Performance</h4>
    <ul>
        <li><code>Internships_Completed</code>: Number of internships (0–4)</li>
        <li><code>Projects_Completed</code>: Number of academic/personal projects (0–9)</li>
        <li><code>Certifications</code>: Number of additional certifications earned (0–5)</li>
        <li><code>Soft_Skills_Score</code>: Soft skills rating (1–10)</li>
        <li><code>Networking_Score</code>: Networking and connections score (1–10)</li>
    </ul>

    <h4>3. Career Outcomes</h4>
    <ul>
        <li><code>Job_Offers</code>: Number of job offers post-graduation (0–5)</li>
        <li><code>Starting_Salary</code>: First job salary in USD ($25,000–$150,000)</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)
