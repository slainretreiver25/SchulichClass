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
yearsData = list(df.index.year.unique())
year = st.sidebar.selectbox("Pick a year", yearsData)
df = df.loc[str(year)]


#Create a chart
fig = px.line(df, y='Adj Close')
#Outout
st.title("Web APP - Schulich Class")
st.plotly_chart(fig) #output plotly graph
st.write(df) #Its like print option, but it will show it in the app

