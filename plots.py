import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import altair as alt #pip install altair


data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

plt.scatter(data['a'],data['b'])
plt.title("scatter")
st.pyplot()

chart = alt.Chart(data).mark_circle().encode(
    x = 'a',y='b',tooltip =['a','b']
)

st.altair_chart(chart,use_container_width =True)

st.graphviz_chart("""
digraph{
watch -> like
like -> share
share -> subscribe
share -> watch
}
""")

##st.plotly_chart(chart,use_container_width=True)

city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})


st.map(city)

st.image("images/cd cmd.jpg")
st.audio("audio\demo_audio for streamlit.m4a")

##st.video("video/thirupaachi bgm.mpeg")
st.video("https://youtu.be/D-k_xx_4PfE")