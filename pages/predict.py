import streamlit as st
phy_activity = st.selectbox(label='Physical Activity', options=['low', "medium", 'high']) # categorical
var = st.multiselect(label='Multiselect', options=['a', "b", 'c'])
gender = st.select_slider(label='gender', options=['female', 'x', 'male'])
is_healthy = st.checkbox(label='is healhy')
gender = st.radio(label='Gender', options=['Male', "Female"])
age = st.slider(label="Age", min_value=22, max_value=50) # numerical
is_submit = st.button("Submit") # True / False
if is_submit:
    print(f"phy_activity: {phy_activity}")
    print(f"age: {age}")
    print(var)
    print(f"is_healthy: {is_healthy}")
    print(f"gender: {gender}")