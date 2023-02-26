import requests

def get_weather_data(city):
    try:
        API_Key = "7acdf1d16577b36cc3572a33386a2b80"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}"
        data = requests.get(url).json()
        lon = data['coord']['lon']
        lat = data['coord']['lat']

        temp = data['main']['temp']
        feels_like = data['main']['feels_like']

        visibility = data['visibility']

        print(f"The data for {city}:\n"
              f"Coordinates are: {lon}, {lat}\n"
              f"The temperature is {temp}\n"
              f"But it feels like {feels_like}\n"
              f"With a visibility of {visibility}")
    except KeyError as e:
        print(f"Unfortunately the city that you inserted: {city} is not found.")

if __name__ == '__main__':
    city  = input("City: ")
    get_weather_data(city)