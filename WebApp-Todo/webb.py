import streamlit as st
import functions

todos = functions.get_todos()                # establishing a variable in our function

st.title("My Todo App")
st.subheader("This is my todo app. ")
st.write("This app is to increase your productivity")

for todo in todos:                          # calling the function to make a checkbox for the todos
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")      # A placeholder for the textbox giving a hint
