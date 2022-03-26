import os
#import requests
API_KEY= os.getenv('API_KEY')
def get_weather(lat='24',lon='83'):
    WEATHER_URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    #data = requests.get(WEATHER_URL)
    return 'data'
