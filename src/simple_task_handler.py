import datetime
import requests
import os
from dotenv import load_dotenv

# Handles simpler tasks like getting the time, date, or weather.
class SimpleTaskHandler:
    def __init__(self):
        load_dotenv()
        self.weather_api_key = os.getenv("WEATHER_API_KEY")

    def handle_task(self, user_input):
        if "time" in user_input.lower():
            return self.get_time()
        elif "date" in user_input.lower():
            return self.get_date()
        elif "weather" in user_input.lower():
            return self.get_weather()
        else:
            return "I'm not sure how to handle that."

    def get_time(self):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    def get_date(self):
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {current_date}."

    def get_weather(self, city="New York"):
        weather_api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}"
        weather_response = requests.get(weather_api).json()
        if weather_response.get("main"):
            temp = weather_response["main"]["temp"]
            return f"The current temperature in {city} is {temp - 273.15:.1f}°C."
        else:
            return "Sorry, I couldn't fetch the weather."
