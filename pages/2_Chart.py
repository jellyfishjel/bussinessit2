# ==== Import Libraries ====
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import gaussian_kde
import numpy as np

# ==== Page Config ====
st.set_page_config(page_title="Chart", layout="wide")

# ==== Load Data ====
@st.cache_data
def load_data():
    return pd.read_excel("education_career_success.xlsx", sheet_name="education_career_success")

df = load_data()

# ==== Style for Notes ====
note_style = """
<div style="background-color:#ffe6e6; border-left: 6px solid #ff4d4d; padding: 16px; margin-bottom: 20px; border-radius: 10px;">
    <h4 style="margin-top: 0;">📌 {title}</h4>
    {text}
</div>
"""

# ==== Gender Distribution Pie Chart ====
st.subheader("Gender Distribution")
gender_counts = df['Gender'].value_counts()
gender_percent = gender_counts / gender_counts.sum() * 100

fig_pie = go.Figure(data=[go.Pie(
    labels=gender_percent.index,
    values=gender_percent.values,
    hole=0.5,
    marker=dict(colors=['#1f77b4', '#ff4136', '#0074D9']),
    textinfo='percent+label'
)])
fig_pie.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=300)

# ==== Age Distribution KDE ====
st.subheader("Age Distribution by Gender")
genders = df['Gender'].unique()
colors = {'Male': 'blue', 'Female': 'red', 'Other': 'purple'}

fig_kde = go.Figure()
for gender in genders:
    subset = df[df['Gender'] == gender]
    if len(subset) > 1:
        kde = gaussian_kde(subset['Age'])
        x = np.linspace(df['Age'].min(), df['Age'].max(), 200)
        fig_kde.add_trace(go.Scatter(
            x=x,
            y=kde(x),
            mode='lines',
            name=gender,
            line=dict(color=colors.get(gender, 'gray'))
        ))

fig_kde.update_layout(xaxis_title='Age', yaxis_title='Density', height=300)

# ==== Layout with Columns ====
col1, col2 = st.columns([2, 1])
with col1:
    st.plotly_chart(fig_kde, use_container_width=True)
with col2:
    st.plotly_chart(fig_pie, use_container_width=True)

# ==== Notes Data ====

# Gender Notes by Level
pie1_notes = {
    "Entry": """
    <ul>
        <li>Gender distribution is nearly equal, suggesting balanced access to entry-level opportunities.</li>
        <li>Female and male participation rates are the highest at this level, indicating wide entry to the workforce.</li>
    </ul>
    """,
    "Mid": """
    <ul>
        <li>Female representation begins to drop slightly, signaling potential career progression challenges.</li>
        <li>Male dominance increases gradually at mid-level positions.</li>
    </ul>
    """,
    "Senior": """
    <ul>
        <li>Significant drop in female participation at senior levels, highlighting a possible leadership gap.</li>
        <li>Gender imbalance may reflect systemic barriers or differing career paths.</li>
    </ul>
    """
}

# Age Notes by Level
age_notes = {
    "Entry": """
    <ul>
        <li>Most individuals fall between ages 22–25, consistent with recent graduates starting careers.</li>
        <li>The peak density shows a sharp entry age, suggesting a clear transition from education to work.</li>
    </ul>
    """,
    "Mid": """
    <ul>
        <li>Age range broadens, with many individuals between 26–30, reflecting progression after initial entry.</li>
        <li>Gradual density slope indicates varying speeds of career advancement.</li>
    </ul>
    """,
    "Senior": """
    <ul>
        <li>Senior roles are concentrated in ages 30+, showing typical timeline for long-term career development.</li>
        <li>Lower density suggests fewer individuals reach these positions, aligning with hierarchical structure.</li>
    </ul>
    """
}

# ==== User Level Selection ====
selected_level = st.selectbox("Select Career Level for Notes", ["Entry", "Mid", "Senior"])

# ==== Show Notes ====
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        note_style.format(
            title="Age Distribution Key Note – " + selected_level,
            text=age_notes.get(selected_level, "")
        ),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        note_style.format(
            title="Gender Distribution Key Note – " + selected_level,
            text=pie1_notes.get(selected_level, "")
        ),
        unsafe_allow_html=True
    )



# === TAB 2 (Job Offers) ===
job_level_notes = {
    "Entry": """
        - Majority of individuals across all ages do not pursue entrepreneurship.<br>
        - A slight increase in entrepreneurial interest is seen between ages 21–23.<br>
    """,
    "Mid": """
        - Entrepreneurship participation remains relatively steady, with slight increases around age 21–23.<br>
        - Majority still fall under the non-entrepreneurship group across all ages.<br>
    """,
    "Senior": """
        - A fairly balanced distribution between entrepreneurs and non-entrepreneurs, with some age groups showing higher entrepreneurship (e.g., age 29).<br>
        - Proportion of entrepreneurs is more prominent than in mid and entry levels.<br>
    """,
    "Executive": """
        - Entrepreneurship (Yes) fluctuates across ages, with no clear increasing or decreasing pattern.<br>
        - Ages 20–22 show a relatively higher proportion of entrepreneurship compared to other ages.<br>
    """
}

job_offers_notes = {
    "Entry": """
        - Individuals with entrepreneurial intentions generally receive more job offers, especially at ages 18, 26, and 28.<br>
        - Entrepreneurial individuals maintain a more stable or slightly upward trend in offers.<br>
    """,
    "Mid": """
        - Highest job offer spike for entrepreneurs occurs around age 27.<br>
        - Despite fluctuations, the difference in job offers between groups is generally narrow (within ~0.5).<br>
    """,
    "Senior": """
        - Sharp spike for entrepreneurs at age 29 indicates potential late-career success.<br>
        - Entrepreneurs face more volatility in job offers, suggesting high risk–high reward dynamics at senior levels.<br>
    """,
    "Executive": """
        - Peak job offers for entrepreneurs occur around age 27, suggesting growing opportunities with age.<br>
        - Fluctuations in entrepreneurial job offers imply less stability compared to non-entrepreneurs.<br>
    """
}

with graph_tab[1]:
    st.markdown("""
        <h1 style='font-family: "Inter", sans-serif; color: #cf5a2e; font-size: 36px;'>Job Offers</h1>
    """, unsafe_allow_html=True)



    df_filtered = gender_filtered[
        (gender_filtered['Current_Job_Level'] == selected_level) &
        (gender_filtered['Age'].between(age_range[0], age_range[1])) &
        (gender_filtered['Entrepreneurship'].isin(selected_statuses))
    ]

    if df_filtered.empty:
        st.warning("⚠️ Not enough data to display charts. Please adjust the filters.")
    else:
        with st.container():
            st.markdown("""<div style="border: 2px solid #cf5a2e; border-radius: 12px; padding: 20px; margin-top: 10px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);">
                <div style="display: flex; justify-content: space-around; text-align: center; line-height: 1.3;">
                    <div>
                        <div style="font-size: 14px; color: #555;">Total Records</div>
                        <div style="font-size: 28px;">{}</div>
                    </div>
                    <div>
                        <div style="font-size: 14px; color: #555;">Median Age</div>
                        <div style="font-size: 28px;">{:.1f}</div>
                    </div>
                    <div>
                        <div style="font-size: 14px; color: #555;">Entrepreneurs (%)</div>
                        <div style="font-size: 28px;">{:.1f}%</div>
                    </div>
                </div></div>
            """.format(len(df_filtered), df_filtered['Age'].median(),
                       (df_filtered['Entrepreneurship'] == "Yes").mean() * 100),
            unsafe_allow_html=True)

        df_grouped = (
            df.groupby(['Current_Job_Level', 'Age', 'Entrepreneurship'])
            .size()
            .reset_index(name='Count')
        )
        df_grouped['Percentage'] = df_grouped.groupby(['Current_Job_Level', 'Age'])['Count'].transform(lambda x: x / x.sum())

        df_bar = df_grouped[
            (df_grouped['Current_Job_Level'] == selected_level) &
            (df_grouped['Age'].between(age_range[0], age_range[1])) &
            (df_grouped['Entrepreneurship'].isin(selected_statuses))
        ]

        even_ages = sorted(df_bar['Age'].unique())
        even_ages = [age for age in even_ages if age % 2 == 0]

        fig_bar = px.bar(
            df_bar,
            x='Age',
            y='Percentage',
            color='Entrepreneurship',
            barmode='stack',
            color_discrete_map=color_map,
            category_orders={'Entrepreneurship': ['No', 'Yes']},
            labels={'Age': 'Age', 'Percentage': 'Percentage'},
            height=450,
            width=1250,
            title=f"Entrepreneurship Distribution by Age – {selected_level} Level"
        )

        fig_bar.update_traces(
            hovertemplate="Entrepreneurship=%{customdata[0]}<br>Age=%{x}<br>Percentage=%{y:.0%}<extra></extra>",
            customdata=df_bar[['Entrepreneurship']].values,
            hoverinfo="skip"
        )

        fig_bar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=40, l=40, r=40, b=40),
            legend_title_text='Entrepreneurship',
            xaxis_tickangle=0,
            bargap=0.1,
            xaxis=dict(tickvals=even_ages),
            yaxis=dict(title="Percentage", range=[0, 1], tickformat=".0%"),
            legend=dict(orientation='h', yanchor='bottom', y=-0.3, xanchor='center', x=0.5)
        )

        df_avg_offers = (
            df_filtered
            .groupby(['Age', 'Entrepreneurship'])['Job_Offers']
            .mean()
            .reset_index()
        )

        fig_line = go.Figure()
        for status in selected_statuses:
            data_status = df_avg_offers[df_avg_offers["Entrepreneurship"] == status]
            fig_line.add_trace(go.Scatter(
                x=data_status["Age"],
                y=data_status["Job_Offers"],
                mode="lines+markers",
                name=status,
                line=dict(color=color_map[status], width=2),
                marker=dict(size=6),
                hovertemplate="%{y:.2f}"
            ))

        fig_line.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            title=f"Average Job Offers by Age – {selected_level} Level",
            margin=dict(t=40, l=40, r=40, b=40),
            legend_title_text='Entrepreneurship',
            xaxis_tickangle=0,
            hovermode="x unified",
            width=1250,
            xaxis=dict(
                showspikes=True,
                spikemode='across',
                spikesnap='cursor',
                spikethickness=1.2,
                spikedash='dot',
                tickvals=even_ages
            ),
            yaxis=dict(
                title="Average Job Offers",
                showspikes=True,
                spikemode='across',
                spikesnap='cursor',
                spikethickness=1.2,
                spikedash='dot',
                gridcolor='#b4adae'
            ),
            legend=dict(orientation='h', yanchor='bottom', y=-0.3, xanchor='center', x=0.5)
        )

        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig_bar, use_container_width=True)
        with col2:
            st.plotly_chart(fig_line, use_container_width=True)
            
        # Add dual note boxes below the two charts
        note_bar = job_level_notes.get(selected_level, "No specific notes available for this level.")
        note_line = job_offers_notes.get(selected_level, "No specific notes available for this level.")
        
        note_style = """
        <div style="
            background-color: #fff4ec;
            border-left: 6px solid #cf5a2e;
            padding: 18px 22px;
            margin-top: 25px;
            border-radius: 12px;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.05);
            font-family: 'Segoe UI', sans-serif;
        ">
            <div style="font-size: 18px; font-weight: 600; margin-bottom: 8px; color: #cf5a2e;">
                📌 {title}
            </div>
            <div style="font-size: 14px; color: #444;">
                {text}
            </div>
        </div>
        """
        
        note_col1, note_col2 = st.columns(2)
        
        with note_col1:
            st.markdown(note_style.format(title=f"Entrepreneurship Distribution Key Note – {selected_level}", text=note_bar), unsafe_allow_html=True)
        
        with note_col2:
            st.markdown(note_style.format(title=f"Average Job Offers Key Note – {selected_level}", text=note_line), unsafe_allow_html=True)
