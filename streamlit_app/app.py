import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
import pymysql
from query_functions import fetch_data

st.title("📊 Personal Expense Tracker Dashboard")

# Connect to MySQL and get data
df = fetch_data("SELECT * FROM expenses")

st.subheader("💰 Total Spending by Category")
category_df = fetch_data("SELECT category, SUM(amount_paid) AS total_spent FROM expenses GROUP BY category")
st.bar_chart(category_df.set_index("category"))

st.subheader("💳 Spending by Payment Mode")
payment_df = fetch_data("SELECT payment_mode, SUM(amount_paid) AS total_spent FROM expenses GROUP BY payment_mode")
st.bar_chart(payment_df.set_index("payment_mode"))

st.subheader("📅 Monthly Spending Trend")
month_df = fetch_data("SELECT MONTH(date) AS month, SUM(amount_paid) AS total_spent FROM expenses GROUP BY month")
st.line_chart(month_df.set_index("month"))

st.subheader("🎯 Cashback Received")
cashback_df = fetch_data("SELECT SUM(cashback) AS total_cashback FROM expenses")
st.write(f"Total Cashback: ₹{cashback_df.iloc[0, 0]:,.2f}")

st.subheader("📊 Average Spending per Transaction")
avg_spent_df = fetch_data("SELECT AVG(amount_paid) AS avg_spent FROM expenses")
st.write(f"Average Spending per Transaction: ₹{avg_spent_df.iloc[0, 0]:,.2f}")

st.subheader("📈 Total Number of Transactions")
total_transactions_df = fetch_data("SELECT COUNT(*) AS total_transactions FROM expenses")
st.write(f"Total Number of Transactions: {total_transactions_df.iloc[0, 0]}")

st.subheader("🏆 Highest Spending Category")
highest_spending_category_df = fetch_data("""
    SELECT category, SUM(amount_paid) AS total_spent
    FROM expenses
    GROUP BY category
    ORDER BY total_spent DESC
    LIMIT 1
""")
st.write(f"Highest Spending Category: {highest_spending_category_df.iloc[0, 0]} with ₹{highest_spending_category_df.iloc[0, 1]:,.2f}")

st.subheader("📉 Lowest Spending Category")
lowest_spending_category_df = fetch_data("""
    SELECT category, SUM(amount_paid) AS total_spent
    FROM expenses
    GROUP BY category
    ORDER BY total_spent ASC
    LIMIT 1
""")
st.write(f"Lowest Spending Category: {lowest_spending_category_df.iloc[0, 0]} with ₹{lowest_spending_category_df.iloc[0, 1]:,.2f}")

st.subheader("📅 Highest Spending Month")
highest_spending_month_df = fetch_data("""
    SELECT MONTH(date) AS month, SUM(amount_paid) AS total_spent
    FROM expenses
    GROUP BY month
    ORDER BY total_spent DESC
    LIMIT 1
""")
st.write(f"Highest Spending Month: {highest_spending_month_df.iloc[0, 0]} with ₹{highest_spending_month_df.iloc[0, 1]:,.2f}")

st.subheader("📅 Lowest Spending Month")
lowest_spending_month_df = fetch_data("""
    SELECT MONTH(date) AS month, SUM(amount_paid) AS total_spent
    FROM expenses
    GROUP BY month
    ORDER BY total_spent ASC
    LIMIT 1
""")
st.write(f"Lowest Spending Month: {lowest_spending_month_df.iloc[0, 0]} with ₹{lowest_spending_month_df.iloc[0, 1]:,.2f}")

st.subheader("📅 Total Spending by Year")
yearly_spending_df = fetch_data("SELECT YEAR(date) AS year, SUM(amount_paid) AS total_spent FROM expenses GROUP BY year")
st.bar_chart(yearly_spending_df.set_index("year"))

st.subheader("💸 Average Cashback per Transaction")
avg_cashback_df = fetch_data("SELECT AVG(cashback) AS avg_cashback FROM expenses")
st.write(f"Average Cashback per Transaction: ₹{avg_cashback_df.iloc[0, 0]:,.2f}")

st.subheader("🍽️ Total Spending on Food")
food_spending_df = fetch_data("SELECT SUM(amount_paid) AS total_spent FROM expenses WHERE category = 'Food'")
st.write(f"Total Spending on Food: ₹{food_spending_df.iloc[0, 0]:,.2f}")

st.subheader("💳 Total Spending on Credit Card")
credit_card_spending_df = fetch_data("SELECT SUM(amount_paid) AS total_spent FROM expenses WHERE payment_mode = 'Credit Card'")
st.write(f"Total Spending on Credit Card: ₹{credit_card_spending_df.iloc[0, 0]:,.2f}")

st.subheader("📅 Total Spending by Day of the Week")
day_of_week_spending_df = fetch_data("SELECT DAYOFWEEK(date) AS day_of_week, SUM(amount_paid) AS total_spent FROM expenses GROUP BY day_of_week")
st.bar_chart(day_of_week_spending_df.set_index("day_of_week"))