import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
df = px.data.tips()
st.title("Interactive Visualizations")
cat_cols = list(df.select_dtypes(include='O').columns)
num_cols = list(df.select_dtypes(include='number').columns)
num_choice = st.radio(label="Numerical Column", options=num_cols)
cat_choice = st.selectbox(label="Categorical Column", options=cat_cols)
graph_choice = st.selectbox(label="Graph Type", options=['box', 'violin', 'strip'])
choice_to_graph = {'box':px.box, 'violin':px.violin, 'strip':px.strip}

is_submit = st.button("Graph")
if is_submit == True:
    fig = choice_to_graph[graph_choice](df, x=cat_choice, y=num_choice)
    st.plotly_chart(fig)