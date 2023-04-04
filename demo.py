import streamlit as st
st.title("HEllo streamlit")

st.header("Header")

st.subheader("Sub header")

st.text("Arpudhamm")

st.markdown(""" # h1 tag #h2 tag #h3tag 
:smile:<br>
:icecream:
:butterfly:<br> 
**bold** _italic_ 
""",True)

st.latex(r''' a + a r^2 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)''')

