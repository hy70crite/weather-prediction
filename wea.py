import requests
from bs4 import BeautifulSoup
import numpy as np

def get_current_weather(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the relevant data (this will depend on the website's structure)
        # For example, let's say the current weather is in a <div> with class "current-weather"
        weather_div = soup.find('div', class_='current-weather')
        
        if weather_div:
            current_weather = weather_div.text.strip()  # Get the text and remove extra spaces
            return current_weather
        else:
            print("Weather data not found on the page.")
            return None
    else:
        print("Failed to retrieve data")
        return None

states = ["Clear", "Cloudy", "Rainy"]
transition_matrix = np.array([
    [0.6, 0.3, 0.1],  # From Clear
    [0.4, 0.4, 0.2],  # From Cloudy
    [0.2, 0.5, 0.3]   # From Rainy
])

def predict_weather(current_weather, days=1):
    current_index = states.index(current_weather)
    predictions = []

    for _ in range(days):
        probabilities = transition_matrix[current_index]
        next_weather = np.random.choice(states, p=probabilities)
        predictions.append(next_weather)
        current_index = states.index(next_weather)

    return predictions

if __name__ == "__main__":
    # Replace with the actual URL of the weather website you want to scrape
    URL = "https://example-weather-website.com/nyc"

    # Get the current weather
    current_weather = get_current_weather(URL)
    
    if current_weather:
        if "clear" in current_weather.lower():
            current_weather = "Clear"
        elif "cloud" in current_weather.lower():
            current_weather = "Cloudy"
        elif "rain" in current_weather.lower():
            current_weather = "Rainy"
        else:
            print("Current weather not recognized.")
            current_weather = "Clear"  # Default to Clear if unrecognized

        # Predict the weather for the next 5 days
        predicted_weather = predict_weather(current_weather, days=5)

        print(f"Current Weather in NYC: {current_weather}")
        print("Predicted Weather for the next 5 days:")
        for day, weather in enumerate(predicted_weather, start=1):
            print(f"Day {day}: {weather}")

