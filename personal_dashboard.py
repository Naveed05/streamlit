import streamlit as st
import pandas as pd
import numpy as np
import random
import math

# Set Page 
st.set_page_config(page_title="✨ Personal Insights Dashboard", layout="centered")

# Title
st.title("🧠 AI-Powered Personal Insights Dashboard")
st.markdown("Welcome to your personalized dashboard powered by Python & Streamlit!")

st.divider()

# Sidebar Input
st.sidebar.header("🔍 Enter Your Details")

with st.sidebar.form("user_info"):
    name = st.text_input("What's your name?", "Naveed")
    age = st.slider("Your Age:", 10, 80, 21)
    hobby = st.text_input("Your Favorite Hobby:", "Cricket")
    goal = st.text_input("Your Current Goal:", "Become a Data Scientist")
    submitted = st.form_submit_button("Get My Insights")


if submitted:
    st.success(f"Hey **{name}**, here's something for you! 🙌")

    
    tab1, tab2, tab3 = st.tabs(["🧠 Personality Boost", "📊 Number Zone", "📈 Mock AI Dataset"])

    
    with tab1:
        st.subheader("🌟 Your Motivation Zone")

        
        quotes = [
            "Believe in yourself, you're halfway there!",
            "Consistency beats motivation.",
            "Be so good they can't ignore you.",
            "Big dreams begin with small steps.",
            "You are capable of amazing things!"
        ]
        st.info(f"💬 *{random.choice(quotes)}*")

        st.write(f"At **{age}**, you're already working toward **{goal}**, and that’s awesome! 🚀")
        st.write(f"Keep enjoying your hobby: {hobby}. It keeps your creativity alive. 🎨")


    with tab2:
        st.subheader("🔢 Math Fun Zone")
        num = st.number_input("Enter a number:", 1, 100)

        col1, col2, col3 = st.columns(3)
        col1.metric("Square", f"{num ** 2}")
        col2.metric("Cube", f"{num ** 3}")
        col3.metric("Factorial", f"{math.factorial(num)}")

    #Random Dataset ---
    with tab3:
        st.subheader("🧪 Your Random Insights Dataset")
        df = pd.DataFrame({
            'Metric': ['Focus Score', 'Energy Level', 'Confidence', 'Learning Rate'],
            'Value': [round(random.uniform(70, 100), 2) for _ in range(4)]
        })
        st.dataframe(df, use_container_width=True)

    st.caption("Dashboard generated with ❤️ by Mirza Naveed")
