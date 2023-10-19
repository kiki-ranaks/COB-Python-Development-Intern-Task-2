import tkinter as tk
import requests

# OpenWeatherMap API URL and your API key
API_KEY = 'e10c0d9b8d0ca395466275cc254ada49'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
app = tk.Tk()
app.title('Weather App')


def get_weather():
    city = entry.get()
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(API_URL, params=params)
    data = response.json()
    print(data)

    if data['cod'] == 200:
        weather_info = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp']
        result_label.config(text=f"Weather: {weather_info}\nTemperature: {temperature}°C")
    else:
        result_label.config(text="City not found")


label = tk.Label(app, text="Enter a city:")
label.pack()

entry = tk.Entry(app)
entry.pack()

get_button = tk.Button(app, text="Get Weather", command=get_weather)
get_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

# Start the application
app.mainloop()
