import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q=
    {city_name}&appid={api_key}&units=metric"
    response = requests.get(url) 
    data = response.json()
    if data["cod"] == 200:

        weather_description = data["weather"][0]["description"]

        temperature = data["weather"][0]["description"]

        temperature = data["main"]["temp"]

        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"weather in {city_name}:")

        print(f"description:{weather_description}")

        print(f"humidity:{humidity}%")

        print(f"windspeed: {wind_speed} m/s")
            
    else:

        print("city not found. Please check the city name and try again.")

        if __name__ == "__main__":
            city = input("Enter city name: ")
            api_key = "Your open weather Api key here"

            #Put your open weather api key in the api_key.
            #This is an example weather app.
            #Never share your api key in open source projects.

            get_weather(city, api_key)