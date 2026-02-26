import streamlit as st
from streamlit_ace import st_ace
import sys
import io
import contextlib

#st.title("Simple Notepad")
st.markdown("<h1 style='text-align: center;'>Simple Notepad</h1>",unsafe_allow_html=True)

cols = st.columns([2,2])

with cols[0]: 
    st.markdown("<p style='text-align: center;'><b>Code</b></p>",unsafe_allow_html=True)
    code = st_ace(
       placeholder="Start coding...",
       language="python",
       theme="monokai",
       key="vscode" 
    )
    #code = st.text_input("",label_visibility="collapsed") Hide label
with cols[1]: 
    st.markdown("<p style='text-align: center;'><b>Start</b></p>",unsafe_allow_html=True)
    runCode = st.button("Run", use_container_width = True)

if runCode:
    codeResult = io.StringIO()
    with contextlib.redirect_stdout(codeResult):
        try: 
            exec(code)
        except Exception as e:
            st.error(f"Error {e}")
    
    st.code(codeResult.getvalue(), language="text")
