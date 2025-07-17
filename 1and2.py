import streamlit as st
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="Naveed's Streamlit App", layout="centered")

# App Title
st.title("🚀 My First Streamlit App by Mirza Naveed")

st.markdown("""
Welcome to my interactive Python + Streamlit app!  
This app lets you:
- Calculate the **square of a number**
- Enter your **name, age, and favorite color**
- Generate and view **random data**
""")

st.divider()

# Sidebar Inputs
st.sidebar.header("🧑 User Info")
user_name = st.sidebar.text_input("What is your name?", "Streamlit User")
age = st.sidebar.slider("Select your age", 0, 100, 25)
favorite_colour = st.sidebar.selectbox("What is your favourite colour?", ["Blue", "Red", "Green", "Yellow"])

# Show user details
st.header(f"👋 Welcome, {user_name}!")
st.write(f"You are **{age}** years old and your favorite color is **{favorite_colour}**.")

st.divider()

# Square Calculator
st.header("🔢 Square Calculator")
number = st.slider("Pick a number", 0, 100, 25)
squared_number = number ** 2
st.success(f"The square of **{number}** is **{squared_number}**")

st.divider()

# Random Data Table
st.subheader("📊 Here's Some Random Data:")
data = pd.DataFrame({
    'A': np.random.randn(10),
    'B': np.random.rand(10),
    'C': np.random.randint(1, 100, 10)
})
st.dataframe(data)

st.caption("Built with ❤️ by Mirza Naveed")
