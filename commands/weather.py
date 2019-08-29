import datetime
import os

import requests
from environs import Env

env = Env()
env.read_env()


class WeatherData:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs.copy()
        self.data = kwargs.get('list')
        self.list = self.data
        self.data = self.__clean_weather_data()

    def __clean_weather_data(self):
        weather = {}
        for dt in self.data:
            weather[dt['dt']] = dt
        return weather

    def get_future_weather(self):
        return {dt.dt['dt']: dt for dt in self.data if dt > datetime.datetime.now().microsecond}


class Weather:
    def __init__(self, city, country):
        self.city = city
        self.country = country
        request_data = self.make_request()
        self.data = WeatherData(**request_data.json())

    def make_request(self):
        return requests.get(
            f'http://api.openweathermap.org/data/2.5/forecast'
            f'?q={self.city},{self.country}'
            f'&APPID={os.environ.get("WEATHER_KEY")}'
        )

    def get_today(self):
        return f'{self.city}/{self.country}:\n' \
            f'Currently: '

    def is_good(self):
        future_weather = self.data.list[0] if self.data.list else None
        return future_weather['main']['temp'] - 273.15 > 20

    @property
    def current_temp(self):
        future_weather = self.data.list[0] if self.data.list else None
        weather = future_weather['main']['temp'] - 273.15
        weather = str(weather)
        weather = '.'.join(i[0:2] for i in weather.split('.'))
        return weather


if __name__ == '__main__':
    Weather('Berlin', 'de')
