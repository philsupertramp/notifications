import json

import googlemaps
from datetime import datetime

import requests
from googlemaps.geocoding import geocode


class Traffic:
    pass
key='5c62a514bc5654415a84920a8e7cdfca'
app_id='8fcc6719'


class Client:
    ROOT_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?{param}&key={key}'

    def __init__(self):
        self.key = 'AIzaSyDLpyDJtO6LEXKlIwv-BaAY_QQL1Io1F7g'

    def get(self, param=''):
        response = requests.post(self.ROOT_URL.format(key=self.key, param=param))
        if response.ok:
            return response


def main():
    response = Client().get()
    data = json.loads(response.content)
    print(data)


if __name__ == '__main__':
    main()
