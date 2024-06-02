import streamlit as st
import functions

todos = functions.get_todos()  # establishing a variable in our function


def add_todo():
    todo = st.session_state["new_todo"] + "\n"   # session state allows us to extract from input the n makes new line
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app. ")
st.write("This app is to increase your productivity")

for todo in todos:  # calling the function to make a checkbox for the todos
    st.checkbox(todo)

st.text_input(label="Enter Here", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')  # A placeholder for the textbox giving a hint

st.session_state
