import streamlit as st

#st.title("Simple Notepad")
st.markdown("<h1 style='text-align: center;'>Simple Notepad</h1>",unsafe_allow_html=True)

cols = st.columns([2,2])
with cols[0]: 
    st.markdown("**Code**")
    code = st.text_input("",label_visibility="collapsed") #Hide label
with cols[1]: 
    st.markdown("**Start**")
    runCode = st.button("Run", use_container_width = True)

if runCode:
    result = code.lower()
    st.success(result)