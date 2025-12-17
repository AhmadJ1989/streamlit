import streamlit as st
from services.data_service import load_dashboard_data
from components.charts import sales_chart, customers_chart

st.title("📊 Dashboard")

data = load_dashboard_data()

col1, col2 = st.columns(2)

with col1:
    sales_chart(data["Sales"])

with col2:
    customers_chart(data["Customers"])
