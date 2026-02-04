import streamlit as st
import pandas as pd

st.title("🛒 Supermarket Analysis Dashboard")

# Load CSVs
sales = pd.read_csv("sales_by_store.csv")
customers = pd.read_csv("customer_type_distribution.csv")
premium = pd.read_csv("premium_customers_by_store.csv")

# Sales by Store
st.subheader("Total Sales by Store")
st.bar_chart(sales.set_index("store"))

# Customer Type Distribution
st.subheader("Customer Type Distribution")
st.bar_chart(customers.set_index("customer_type"))

# Premium Customers by Store
st.subheader("Premium Customers by Store")
st.bar_chart(premium.set_index("store"))
