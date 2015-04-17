# -*- coding: utf-8 -*-
"""

"""
from collections import namedtuple
import os

import requests
import json

with open(os.path.dirname(os.path.realpath(__file__)) + '/config') as f:
    FORECAST_API_KEY = f.read()

FORECAST_API_URL = 'https://api.forecast.io/forecast/{api_key}/{lat},{long}?units=si'

Forecast = namedtuple('Forecast', ['condition', 'temperature'])


def get_weather(lat, long):

    try:
        response = requests.get(FORECAST_API_URL.format(api_key=FORECAST_API_KEY, lat=lat, long=long))
    except requests.HTTPError:
        return Forecast('Error', 'Error')

    weather_dict = json.loads(response.text).get('currently', {})

    try:
        temp = int(weather_dict.get('temperature', 'N/A'))
    except ValueError:
        temp = 'N/A'

    return Forecast(weather_dict.get('summary', 'N/A'), temp)




