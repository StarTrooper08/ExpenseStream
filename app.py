#imports for our app
import streamlit as st
import plotly.graph_objects as go

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