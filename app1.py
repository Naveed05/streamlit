#lib imported
import streamlit as st 

#Title
st.title("My First streamlit App created By Mirza Naveed ")

#Added somme text
st.write("This app calculates the square of a number. ") 

#creted a interactive slider 
st.header("select a Number ")
number = st.slider("pick a number ", 0, 100, 25 )


#calculate and display result 
st.subheader("Result")
squared_number = number * number 
st.write(f"The Square of **{number} ** is **{squared_number}**.")