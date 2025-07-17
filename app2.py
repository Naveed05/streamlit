import streamlit as st 
import pandas as pd 
import numpy as np 

st.title("My First streamlit App")
st.write("this is the simple app to demostrate the basic funtionalities of streamlit. ")

st.header("user input Features ")

user_name = st.sidebar.text_input("what is your name? ", "streamlit User ")

age = st.sidebar.slider("select your age", 0 , 100, 25)

favorite_colour = st.sidebar.selectbox("What is your favourite colour?", ["Blue", "Red", "Green", "Yellow"])


st.header(f"welcome, {user_name}!")
st.write(f"you are{age} year old and your favourite colour is {favorite_colour}.")

st.subheader("Here's some random data: ")

data = pd.DataFrame({
    'A': np.random.randn(10),
    'B': np.random.rand(10),
    'C': np.random.randint(1, 100, 10)
})

st.dataframe(data)

# data = pd.DataFrame(
#     np.random.random(10,5),
#     columns=('col %d' % i for i in range(5))
# )

# st.dataframe(data)

