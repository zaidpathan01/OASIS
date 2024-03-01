# Import libraries
import requests

# API key and base URL (replace with your own)
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(location):
  """
  Fetches weather data for the given location and returns a dictionary.
  """
  # Build the URL with API key and location
  url = f"{BASE_URL}?q={location}&appid={API_KEY}"

  # Make the API request
  response = requests.get(url)

  # Check for successful response
  if response.status_code == 200:
    # Parse JSON data
    data = response.json()

    # Extract relevant information
    city = data["name"]
    temperature = round(data["main"]["temp"] - 273.15, 2)  # Convert Kelvin to Celsius
    humidity = data["main"]["humidity"]
    conditions = data["weather"][0]["description"]

    # Return weather information as a dictionary
    return {
      "city": city,
      "temperature": temperature,
      "humidity": humidity,
      "conditions": conditions
    }
  else:
    # Handle error
    print(f"Error: {response.status_code}")
    return None

def main():
  # Get location from user
  location = input("Enter city name or ZIP code: ")

  # Fetch and display weather data
  weather_info = get_weather(location)
  if weather_info:
    print(f"\nWeather in {weather_info['city']}:")
    print(f"  Temperature: {weather_info['temperature']}°C")
    print(f"  Humidity: {weather_info['humidity']}%")
    print(f"  Conditions: {weather_info['conditions']}")
  else:
    print("Please replace YOUR API KEY (can't share my API due security purpose).")

# Run the main function
if __name__ == "__main__":
  main()
