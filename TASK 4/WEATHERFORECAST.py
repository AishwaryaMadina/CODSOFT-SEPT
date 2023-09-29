import requests

api_key = '6387bd606e1bc6e3ea54f1701f7d4f31'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    description = weather_data.json()["weather"][0]["description"].capitalize()
    wind_speed = weather_data.json()["wind"]["speed"]

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")
    print(f"Description: {description}")
    print(f"Wind Speed: {wind_speed} m/s")