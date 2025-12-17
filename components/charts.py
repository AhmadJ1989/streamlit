import streamlit as st

def sales_chart(data):
    st.line_chart(data)

def customers_chart(data):
    st.bar_chart(data)
