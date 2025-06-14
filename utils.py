import streamlit as st

def apply_global_styles():
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet">
    <style>
        * {
            font-family: 'Inter', sans-serif;
        }
        section[data-testid="stSidebar"],
        section[data-testid="stSidebar"] * {
            color: #333 !important;
            font-family: 'Inter', sans-serif !important;
        }
    </style>
""", unsafe_allow_html=True)
