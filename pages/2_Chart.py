import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import gaussian_kde
import numpy as np

st.set_page_config(page_title="Entrepreneurship Insights", layout="wide")

# ==== Apply global styles ==== 
from utils import apply_global_styles
apply_global_styles()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        color: #52504d;
        font-size: 15px;
    }
    .main-title {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #222;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_excel("education_career_success.xlsx")

df = load_data()

# ==== Sidebar Filters ====
st.sidebar.title("Filters")

# Gender Filter
gender_options = sorted(df['Gender'].dropna().unique())
selected_genders = st.sidebar.multiselect("Select Gender(s)", gender_options, default=gender_options)
gender_filtered = df if not selected_genders or 'All' in selected_genders else df[df['Gender'].isin(selected_genders)]
if not selected_genders:
    st.sidebar.warning("⚠️ No gender selected. Using full data.")

# Job Level Filter
job_levels = sorted(df['Current_Job_Level'].dropna().unique())
selected_level = st.sidebar.selectbox("Select Job Level", job_levels)

# Age Filter
min_age, max_age = int(df['Age'].min()), int(df['Age'].max())
age_range = st.sidebar.slider("Select Age Range", min_value=min_age, max_value=max_age, value=(min_age, max_age))
if age_range[0] == age_range[1]:
    st.sidebar.warning(f"⚠️ Only one age ({age_range[0]}) selected. Using full range.")
    age_range = (min_age, max_age)

# Entrepreneurship Filter
st.sidebar.markdown("**Select Entrepreneurship Status**")
show_yes = st.sidebar.checkbox("Yes", value=True)
show_no = st.sidebar.checkbox("No", value=True)
selected_statuses = [s for s, show in zip(["Yes", "No"], [show_yes, show_no]) if show]
if not selected_statuses:
    st.sidebar.warning("⚠️ No status selected. Using full data.")
    selected_statuses = ['Yes', 'No']

# ==== Filtered Data ====
df_demo = gender_filtered[
    (gender_filtered['Current_Job_Level'] == selected_level) &
    (gender_filtered['Age'].between(*age_range)) &
    (gender_filtered['Entrepreneurship'].isin(selected_statuses))
]

# ==== Notes Dictionary ====
# [unchanged - reuse same dictionaries as in your original code]

# ==== Main Content ====
st.markdown("""
    <h1 style='font-family: "Inter", sans-serif; color: #cf5a2e; font-size: 40px;'>📊 Demographics</h1>
""", unsafe_allow_html=True)

chart_option = st.selectbox("Select Variable for Visualization", ['Gender Distribution', 'Field of Study'])

if df_demo.empty:
    st.warning("⚠️ Not enough data to display charts. Please adjust the filters.")
else:
    metric_container = st.container()
    if chart_option == 'Gender Distribution':
        percent_female = (df_demo['Gender'] == 'Female').mean() * 100
        with metric_container:
            st.markdown(f"""
                <div style="border: 2px solid #cf5a2e; border-radius: 12px; padding: 20px; margin: 20px 0; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);">
                    <div style="display: flex; justify-content: space-around; text-align: center;">
                        <div><div style="color: #555;">Total Records</div><div style="font-size: 28px;">{len(df_demo)}</div></div>
                        <div><div style="color: #555;">Median Age</div><div style="font-size: 28px;">{df_demo['Age'].median():.1f}</div></div>
                        <div><div style="color: #555;">% Female</div><div style="font-size: 28px;">{percent_female:.1f}%</div></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    else:
        top_fields = df_demo['Field_of_Study'].value_counts().head(3).index.tolist()
        with metric_container:
            st.markdown(f"""
                <div style="border: 2px solid #cf5a2e; border-radius: 12px; padding: 20px; margin: 20px 0; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);">
                    <div style="display: flex; justify-content: space-around; text-align: center;">
                        <div><div style="color: #555;">Total Records</div><div style="font-size: 28px;">{len(df_demo)}</div></div>
                        <div><div style="color: #555;">Top 3 Fields</div><div style="font-size: 20px;">{', '.join(top_fields)}</div></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # ==== Charts ====
    col1, col2 = st.columns(2)
    group_col = 'Gender' if chart_option == 'Gender Distribution' else 'Field_of_Study'

    with col1:
        fig_density = go.Figure()
        for cat in df_demo[group_col].dropna().unique():
            age_data = df_demo[df_demo[group_col] == cat]['Age']
            if len(age_data) > 1:
                kde = gaussian_kde(age_data)
                x_vals = np.linspace(age_range[0], age_range[1], 100)
                fig_density.add_trace(go.Scatter(
                    x=x_vals,
                    y=kde(x_vals),
                    mode='lines',
                    name=str(cat),
                    fill='tozeroy'
                ))

        fig_density.update_layout(
            title=f"Age Distribution by {group_col.replace('_', ' ')}",
            xaxis_title="Age",
            yaxis_title="Density",
            height=500,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=40, l=40, r=40, b=80),
            legend=dict(orientation="h", y=-0.3, x=0.5, xanchor="center")
        )
        st.plotly_chart(fig_density, use_container_width=True)

    with col2:
        pie_data = df_demo[group_col].value_counts().reset_index()
        pie_data.columns = [group_col, 'Count']

        fig_donut = go.Figure(data=[
            go.Pie(
                labels=pie_data[group_col],
                values=pie_data['Count'],
                hole=0.5,
                textinfo='percent+label',
                insidetextorientation='radial',
                marker=dict(line=dict(color='#fff', width=1))
            )
        ])

        fig_donut.update_layout(
            title=dict(
                text=f"{group_col.replace('_', ' ')} Distribution (Donut Chart)",
                x=0.5,
                font=dict(size=18, color='#333')
            ),
            height=500,
            margin=dict(t=40, l=20, r=20, b=80),
            legend=dict(orientation='h', y=-0.3, x=0.5, xanchor='center')
        )
        st.plotly_chart(fig_donut, use_container_width=True)

    # ==== Notes Section ====
    # Reuse same logic as original for displaying insight notes


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
