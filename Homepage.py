import streamlit as st
import pandas as pd
import plotly.express as px

# === Load data ===
df = pd.read_csv("data/your_dataset.csv")  # thay bằng đường dẫn dữ liệu thực tế

st.title("📊 Dataset Overview")

st.markdown("Use the filters below to explore the dataset interactively:")

# === Sidebar Filters ===
with st.sidebar:
    st.header("🔍 Filters")

    gender_options = df["gender"].dropna().unique()
    selected_gender = st.multiselect("Select Gender(s):", gender_options, default=gender_options)

    age_range = (int(df["age"].min()), int(df["age"].max()))
    selected_age = st.slider("Select Age Range:", min_value=age_range[0], max_value=age_range[1], value=age_range)

    education_levels = df["education_level"].dropna().unique()
    selected_edu = st.multiselect("Select Education Level(s):", education_levels, default=education_levels)

# === Apply Filters ===
filtered_df = df[
    (df["gender"].isin(selected_gender)) &
    (df["age"].between(selected_age[0], selected_age[1])) &
    (df["education_level"].isin(selected_edu))
]

# === Quick Stats ===
st.subheader("📌 Quick Statistics")

col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(filtered_df))
col2.metric("Avg. Income", f"${filtered_df['income'].mean():,.0f}" if not filtered_df.empty else "N/A")
col3.metric("Unique Education Levels", filtered_df["education_level"].nunique())

# === Optional: Small chart (e.g., education count) ===
fig = px.bar(filtered_df["education_level"].value_counts().reset_index(),
             x="index", y="education_level", labels={"index": "Education Level", "education_level": "Count"},
             title="Distribution by Education Level")
st.plotly_chart(fig, use_container_width=True)

# === Show Filtered Data Table ===
st.subheader("📄 Filtered Dataset")
st.dataframe(filtered_df, use_container_width=True)

# === Optional: Download CSV ===
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download Filtered Data", data=csv, file_name="filtered_data.csv", mime="text/csv")
