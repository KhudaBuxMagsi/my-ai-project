import requests

def get_weather(city):
    """Get weather for a city using a free API"""
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    city = input("Enter a city name: ")
    weather = get_weather(city)
    print(f"Weather in {city}: {weather}")