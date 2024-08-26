import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_data(place, days, option, degree):
	url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

	request = requests.get(url)
	data = request.json()
	data = data["list"]
	# The data will return a list of 40 objects. One object accounts for 3 hours. There is enough data for the next 5 days. 8 objects accounts for one day.
	filtered_data = data[:8*days]

	if option == "Temperature":
		temp_list = [item["main"]["temp"] / 10 for item in filtered_data]
		dates = [item["dt_txt"] for item in filtered_data]
		if degree == "Fahrenheit":
			temp_list = [item * 1.8 + 32 for item in temp_list]

	elif option == "Sky Forcast":
		temp_list = [item["weather"][0]["main"] for item in filtered_data]
		dates = [item["dt_txt"] for item in filtered_data]

	else:
		temp_list = None
		dates = None

	return temp_list, dates





if __name__ == "__main__":
	get_data = get_data("Tokyo", 1, "Temperature")
	print(get_data[0])
	print(get_data[1])


