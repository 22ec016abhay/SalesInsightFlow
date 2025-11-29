import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")

st.title("📊 Sales Analytics Dashboard")

# Sidebar
st.sidebar.header("Filter Data")
region = st.sidebar.multiselect("Select Region", ["North", "South", "East", "West"], default=["North", "South"])

# Mock Data
data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': [15000, 23000, 12000, 18000, 16000, 21000],
    'Month': ['Jan', 'Jan', 'Jan', 'Jan', 'Feb', 'Feb']
}
df = pd.DataFrame(data)

# KPI Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", "$105,000", "12%")
col2.metric("Total Orders", "1,240", "5%")
col3.metric("Avg Order Value", "$85", "-2%")

# Charts
st.subheader("Revenue by Region")
fig = px.bar(df, x='Region', y='Sales', color='Region', title="Sales Performance")
st.plotly_chart(fig, use_container_width=True)

st.write("This dashboard visualizes sales performance across different regions.")
