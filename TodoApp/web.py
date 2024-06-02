import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.set_todos(todos)

st.title("My Todo App")
st.subheader("By: Heba Azeef")
st.write("This app will increase your <b>productivity</b>", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos) #write updated list
        del st.session_state[todo] #remove it from the dictionary
        st.experimental_rerun()

st.text_input(label="Enter a todo", 
              placeholder="Buy groceries",
              on_change = add_todo, key='new_todo')