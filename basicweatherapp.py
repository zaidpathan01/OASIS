import requests

# API key and base URL (replace with your own)
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Make sure to replace this with your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(location):
    """
    Fetches weather data for the given location and returns a dictionary.
    """

    url = f"{BASE_URL}?q={location}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        try:
            city = data["name"]
            temperature = round(data["main"]["temp"] - 273.15, 2)
            humidity = data["main"]["humidity"]
            conditions = data["weather"][0]["description"]

            return {
                "city": city,
                "temperature": temperature,
                "humidity": humidity,
                "conditions": conditions
            }
        except KeyError as e:
            print(f"Error: Missing key in response data: {e}")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    location = input("Enter city name or ZIP code: ")

    weather_info = get_weather(location)

    if weather_info:
        print(f"\nWeather in {weather_info['city']}:")
        print(f"  Temperature: {weather_info['temperature']}°C")
        print(f"  Humidity: {weather_info['humidity']}%")
        print(f"  Conditions: {weather_info['conditions']}")
    else:
        print("Please replace YOUR API KEY (can't share my API due security purpose).")

if __name__ == "__main__":
    main()
