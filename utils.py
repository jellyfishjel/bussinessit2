import streamlit as st

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
                font-color: white;
            }
            
            /* Phần hiển thị đã chọn */
            div[data-baseweb="select"] > div {
                background-color: #FFF3E0 !important;  /* nền cam pastel */
                border: 2px solid #cf5a2e !important;  /* viền cam */
                color: #333 !important;
            }

            [data-testid="stMetricLabel"] {
                    color: #333 !important;
            }
            label, span, p {
                color: #333 !important;
            }
            [role="menuitem"], [role="menuitem"] span {
                color: #cf5a2e !important;
            }
            [role="menu"] {
                background-color: #fdf7f3 !important;
            }
        </style>
    """, unsafe_allow_html=True)
