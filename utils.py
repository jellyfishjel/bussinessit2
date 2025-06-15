import streamlit as st

# ========== Áp dụng font và CSS toàn cục ==========
def apply_global_styles():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet">
        <style>
            * {
                font-family: 'Inter', sans-serif;
            }

            /* Sidebar font and color */
            section[data-testid="stSidebar"] *,
            section[data-testid="stSidebar"] {
                font-family: 'Inter', sans-serif !important;
                color: #333 !important;
            }

            /* Gender multiselect tags */
            [data-baseweb="tag"] {
                background-color: #ffd7b5 !important;
                color: white !important;
            }

            /* Phần hiển thị đã chọn */
            div[data-baseweb="select"] > div {
                background-color: #FFF3E0 !important;
                border: 2px solid #cf5a2e !important;
                color: #333 !important;
            }

            [data-testid="stMetricLabel"] {
                color: #333 !important;
            }

            label, p {
                color: #333 !important;
            }
        </style>
    """, unsafe_allow_html=True)


def apply_chart_style(fig, title=None, xaxis_title=None, yaxis_title=None, legend_title=None):
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#333'),
        title=dict(text=title, font=dict(color='#333')) if title else None,
        xaxis=dict(
            title=xaxis_title if xaxis_title else None,
            titlefont=dict(color='#333'),
            tickfont=dict(color='#333')
        ),
        yaxis=dict(
            title=yaxis_title if yaxis_title else None,
            titlefont=dict(color='#333'),
            tickfont=dict(color='#333')
        ),
        legend=dict(
            title=dict(text=legend_title, font=dict(color='#333')) if legend_title else None,
            orientation='h',
            yanchor='bottom',
            y=-0.3,
            xanchor='center',
            x=0.5,
            font=dict(color='#333')
        ),
        margin=dict(t=40, l=40, r=40, b=60),
        height=500
    )
    return fig
