import streamlit as st

@st.dialog("This is a dialog")
def dialog_function():
    st.write("This is a dialog function.")
    if st.button("Close"):
        st.rerun(scope="app")

st.header("Latihan Soal")
