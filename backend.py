import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_data(place, days, option):
	url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

	request = requests.get(url)
	data = request.json()
	data = data["list"]
	# The data will return a list of 40 objects. One object accounts for 3 hours. There is enough data for the next 5 days. 8 objects accounts for one day.
	filtered_data = data[:8*days]

	temp_list = []
	if option == "Temperature":
		for item in filtered_data:
			temp_list.append(item["main"]["temp"])

	elif option == "Sky Forcast":
		for item in filtered_data:
			temp_list.append(item["weather"][0]["main"])

	return temp_list





if __name__ == "__main__":
	print(get_data("Tokyo", 1, "Temperature"))
	# get_data("Tokyo", 3, "Sky Forcast")

