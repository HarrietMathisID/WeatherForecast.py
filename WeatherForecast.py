import requests

class WeatherForecast:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather_forecast(self, city):
        url = f"https://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={city}&days=3"
        response = requests.get(url)

        if response.status_code == 200:
            forecast_data = response.json()
            city_name = forecast_data['location']['name']
            country = forecast_data['location']['country']
            print(f"Weather forecast for {city_name}, {country}:")

            for day in forecast_data['forecast']['forecastday']:
                date = day['date']
                max_temp = day['day']['maxtemp_c']
                min_temp = day['day']['mintemp_c']
                condition = day['day']['condition']['text']

                print(f"Date: {date}")
                print(f"Max Temp: {max_temp}°C")
                print(f"Min Temp: {min_temp}°C")
                print(f"Condition: {condition}")
                print()
        else:
            print("Failed to retrieve the weather forecast.")

def main():
    api_key = "YOUR_API_KEY"
    city = "London"

    forecast = WeatherForecast(api_key)
    forecast.get_weather_forecast(city)

if __name__ == "__main__":
    main()
