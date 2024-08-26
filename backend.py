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

	if option == "Temperature":
		temp_list = [item["main"]["temp"] for item in filtered_data]

	elif option == "Sky Forcast":
		temp_list = [item["weather"][0]["main"] for item in filtered_data]
	else:
		temp_list = None

	return temp_list





if __name__ == "__main__":
	print(get_data("Tokyo", 1, "Temperature"))

