import streamlit as st
import functions

todos = functions.get_todos()  # establishing a variable in our function


def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # session state allows us to extract from input the n makes new line
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app. ")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):  # making the item the user selects an index
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:                    # action only happens if the box is checked
        todos.pop(index)  # deleting the item in said index
        functions.write_todos(todos)  # write the updated value to todos.txt
        del st.session_state[todo]  # deletes from the session state dictionary
        st.experimental_rerun()         # re-runs the code after deleting from the session

st.text_input(label="Enter Here", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')  # A placeholder for the textbox giving a hint
