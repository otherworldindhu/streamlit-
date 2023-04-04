import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1.1,2,3,4,5,6,7.65,8]
n = np.array(a)
nd = n.reshape((2,4))

dic = { "name":"Indhu", "age": 21, "status": "Ok" }

data =pd.read_csv("data//2017-2020.csv")
##print(data)

st.dataframe(a)
st.dataframe(nd)
st.dataframe(dic)
st.dataframe(data)
##st.dataframe(data, width=500,height=400)
##st.table(data)
st.table(dic)
st.json(dic)
st.json(data)
st.write(data)
st.write(a)
st.write(dic)

@st.cache_data
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))
