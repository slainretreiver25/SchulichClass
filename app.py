# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:30:56 2024

@author: Aman
"""

#%% Creating app
import streamlit as st
import pandas as pd
import plotly.express as px

#Grab data
ticker = st.sidebar.selectbox("Choose a stock:", ['AAPL','DIS','NKE','MCD','MMM','XOM','SP500'])
df = pd.read_csv(ticker + '.csv', parse_dates=['Date'],index_col=['Date'])

#Filter the data
#reqDates = list(df.index.year.unique())
#year = st.sidebar.selectbox("Pick a year", yearsData)
minValue = df.index.min()
maxValue = df.index.max()
startDate = st.sidebar.date_input("Enter Start Date:", format="YYYY-MM-DD")
endDate = st.sidebar.date_input("Enter End Date:", format="YYYY-MM-DD")
df = df.loc[startDate:endDate]


#Create a chart
fig = px.line(df, y='Adj Close')
#Outout
st.title("Web APP - Schulich Class")
st.plotly_chart(fig) #output plotly graph
st.write(df) #Its like print option, but it will show it in the app

