import streamlit as st
import plotly.express as px
df = px.data.tips()
st.title("Welcome To our Sleep Analysis Project")
st.text("Here is our Data format")
st.dataframe(df.head(7))
