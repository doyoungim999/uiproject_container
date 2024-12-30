import streamlit as st

def main():
    st.title("My first streamlit application")
    myname = st.text_input("Name", value="My Name")
    st.write(f"Welcome to my app, {myname}.")

if __name__ == "__main__":
    main()