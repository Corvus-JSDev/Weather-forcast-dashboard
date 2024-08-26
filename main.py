import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Weather forcast for the next days")
place = st.text_input("Place:", placeholder="New York", help="Type in the name of any place in the world")
days = st.slider("Forcast Days:", min_value=1, max_value=5)
option = st.selectbox("Option", ("Temperature", "Sky Forcast"))

subhead_text = f"{option} for {f'the next {days} days' if days > 1 else 'today'}"
st.subheader(subhead_text)

dates = ["Mar. 4", "Mar. 6", "Mar. 7"]
temp = [20, 25, 15]

plot = px.line(x=dates, y=temp, labels={"x": "Dates", "y": "Temp"})
st.plotly_chart(plot)