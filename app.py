#imports for our app
import streamlit as st
import plotly.graph_objects as go

import calendar
from datetime import datetime

#variables
incomes = ["Salary","Blog","Other Income"]
expenses = ["Rent","Utilities","Groceries","Car","Saving"]
currency = "USD"
page_title = "Expense Stream"
page_icon = ":money_with_wings:"
layout = "centered"

#setting title for our app
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)


years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])


st.header(f"Data Entry in {currency}")
with st.form("Entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1.selectbox("Select Month:", months, key= "month")
    col2.selectbox("Select Year:", years, key="year")


    with st.expander("Income"):
        for income in incomes:
            st.number_input(f"{income}:",min_value=0, format="%i", step=10,key=income)
    with st.expander("Expenses"):
        for expense in expenses:
            st.number_input(f"{expense}:", min_value=0,format="%i",step=10,key=expense)
    with st.expander("Comment"):
        comment = st.text_area("", placeholder="Enter a comment hee ...")



    submitted = st.form_submit_button("Save Data")
    if submitted:
        period = str(st.session_state["year"]) + "" + str(st.session_state["month"])
        incomes = {income: st.session_state[income] for income in incomes}
        expenses = {expense: st.session_state[expense] for expense in expenses}

        st.write(f"incomes: {incomes}")
        st.write(f"expenses: {expenses}")
        st.success("Data Saved!")






st.header("Data Visualization")
with st.form("Saved periods"):

    period = st.selectbox("Select Period:",["2022_March"])
    submitted = st.form_submit_button("Plot_Period")
    if submitted:
        comment = "Some comment"
        incomes = {'Salary':1000, 'Blog': 50, 'Other_Income':10}
        expenses = {'Rent':600, 'Utilities':200, 'Groceries': 300, 'Car': 100, 'Other_Expenses': 50, 'Saving':10}


        total_income = sum(incomes.values())
        total_expense = sum(expenses.values())
        remaining_budget = total_income - total_expense
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Income",f"{total_income} {currency}")
        col1.metric("Total Expense",f"{total_expense} {currency}")
        col1.metric("Remaining Budget",f"{remaining_budget} {currency}")
        st.text(f"Comment:{comment}")

