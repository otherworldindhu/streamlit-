import streamlit as st
import pandas as pd # pip install pandas
from matplotlib import pyplot as plt # pip install matplotlib
import time

plt.style.use("ggplot")

data = {
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}
_='''
df = pd.DataFrame(data = data)

st.sidebar.selectbox("Select a number", [1,2,3,4,5])

col =st.sidebar.selectbox("Select a column", df.columns)

plt.plot(df['num'],df[col])
st.pyplot()

col =st.sidebar.multiselect("Select a column", df.columns)
plt.plot(df['num'],df[col])
st.pyplot()
'''
rad =st.sidebar.radio("Navigation",["Home","About Us"])

if rad == "Home":
    df = pd.DataFrame(data = data)

    col = st.sidebar.multiselect("Select a Column",df.columns)

    plt.plot(df['num'],df[col])

    st.pyplot()

if rad == "About Us":
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
    #st.write("You are in about us page")

    st.balloons()

    st.error("Error")
    st.success("Show Success")
    st.info("Information")
    st.exception(RuntimeError("this is an error"))
    st.warning("this is a warning")

  

