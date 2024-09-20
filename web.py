import streamlit as st
import functions

todos = functions.get_todos()


st.title("My TODO App")
st.subheader("This is a todo app")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")
