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
                background-color: #cf5a2e !important;
                color: white !important;
                font-color: white;
            }
    </style>
        </style>
    """, unsafe_allow_html=True)
