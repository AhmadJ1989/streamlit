import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="AI Dashboard",
    page_icon="📊",
    layout="wide"
)

# CSS laden
css_file = Path("styles/main.css")
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar (Navigation)
st.sidebar.title("Navigation")
st.sidebar.info("Use the menu to navigate")

