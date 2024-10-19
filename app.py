import requests
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# Function to get weather data from OpenWeatherMap API
def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,          # Use city name in the parameters
        'appid': API_KEY,   # Use the loaded API key
        'units': 'metric'   # Celsius
    }
    response = requests.get(base_url, params=params)

    # Debugging: print response status code and content
    st.write(f"Response Status Code: {response.status_code}")
    st.write(f"Response Content: {response.json()}")  # Print actual response content

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.json().get('message', 'Unknown error')}")
        return None

# Streamlit app interface
def main():
    st.title("Weather App 🌦️")
    
    # Input field for city name
    city = st.text_input("Enter the city name")

    if st.button("Get Weather"):
        if city:
            weather_data = get_weather(city)
            if weather_data:
                st.write(f"## Weather in {city.capitalize()}")
                st.write(f"**Temperature:** {weather_data['main']['temp']}°C")
                st.write(f"**Weather:** {weather_data['weather'][0]['description'].capitalize()}")
                st.write(f"**Humidity:** {weather_data['main']['humidity']}%")
                st.write(f"**Wind Speed:** {weather_data['wind']['speed']} m/s")
        else:
            st.error("Please enter a city name.")

if __name__ == "__main__":
    main()
