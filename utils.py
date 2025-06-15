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
            .rc-slider-track {
                background-color: #FF6F00 !important;  /* Cam đậm */
            }

            /* Tay cầm (nút tròn) */
            .rc-slider-handle {
                border-color: #FF6F00 !important;
                background-color: #FF6F00 !important;
                box-shadow: 0 0 0 3px rgba(255, 111, 0, 0.2) !important;  /* hiệu ứng glow */
            }
        </style>
    """, unsafe_allow_html=True)
