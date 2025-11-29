import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

# --------------------------
#  Title & Description
# --------------------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Analytics Dashboard")
st.write("A simple and clean data analytics dashboard created for portfolio & resume projects.")

# --------------------------
#  Load Data
# --------------------------
@st.cache_data
def load_data():
    conn = sqlite3.connect("sales.db")
    df = pd.read_sql_query("SELECT * FROM sales_data", conn)
    conn.close()
    return df

try:
    df = load_data()
except:
    st.error("❌ Database not found! Please ensure sales.db exists in the root folder.")
    st.stop()

# --------------------------
#  Sidebar Filters
# --------------------------
st.sidebar.header("🔍 Filters")

years = df["year"].unique()
regions = df["region"].unique()

selected_year = st.sidebar.selectbox("Select Year", sorted(years))
selected_region = st.sidebar.multiselect("Select Region(s)", regions, default=regions)

# Apply filters
filtered = df[
    (df["year"] == selected_year) &
    (df["region"].isin(selected_region))
]

# --------------------------
#  Charts
# --------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Sales by Region")
    fig = px.bar(filtered, x="region", y="sales", color="region")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("💰 Sales Trend")
    fig2 = px.line(filtered, x="month", y="sales", markers=True)
    st.plotly_chart(fig2, use_container_width=True)

st.success("✨ Dashboard loaded successfully!")