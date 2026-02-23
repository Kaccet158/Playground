import streamlit as st

#st.title("Simple Notepad")
st.markdown("<h1 style='text-align: center;'>Simple Notepad</h1>",unsafe_allow_html=True)

cols = st.columns([2,2])
with cols[0]: code = st.text_input("Code")
with cols[1]: runCode = st.button("Run", use_container_width = True)

if runCode:
    result = code.lower()
    st.success(result)