import streamlit as st
from components.cards import info_card

st.title("📈 Analytics")

accuracy = st.slider("Model Accuracy", 0.0, 1.0, 0.85)
latency = st.slider("API Latency (ms)", 50, 500, 120)

info_card("Accuracy", f"{accuracy * 100:.2f}%")
info_card("Latency", f"{latency} ms")
