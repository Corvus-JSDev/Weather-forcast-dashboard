import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forcast for the next days")
place = st.text_input("Enter a city name:", placeholder="New York", help="Type in the name of any place in the world")
days = st.slider("Forcast Days:", min_value=1, max_value=5)
option = st.selectbox("Option", ("Temperature", "Sky Forcast"))
degree = st.selectbox("Degree", ("Fahrenheit", "Celsius"))

subhead_text = f"{option} for {f'the next {days} days' if days > 1 else 'today'}"
st.subheader(subhead_text)


try:
	if place:
		data, dates = get_data(place, days, option, degree)

		if option == "Temperature":
			plot = px.line(x=dates, y=data, labels={"x": "Date and Time", "y": f"Temp in {degree}"})
			st.plotly_chart(plot)

		elif option == "Sky Forcast":
			img_list = [f"images/{item.lower()}.png" for item in data]
			st.image(img_list, width=115)

except KeyError:
	st.write(f"{place} was not found. Please search for only the city name.")

	st.write("Examples:")
	st.write("✅ \"New York\"")
	st.write("❌ \"New York, NY\"")
	st.write("❌ \"New York, NY, USA\"")



