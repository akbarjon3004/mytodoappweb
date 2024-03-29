import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My ToDo App")
st.subheader("This is my ToDo App")
st.write("This app is to increase yur productivity")

for index, todo in enumerate(todos):
    chechbox = st.checkbox(todo, key=todo)
    if chechbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label=" ", placeholder="Enter a todo",
              on_change=add_todo, key="new_todo")

