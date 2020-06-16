import json
import urllib

from .models import City
# from .forms import CityForm
from .config import WEATHER_API_KEY


def weather_by_city_name(city_name):
    """Take weather from Open Weather API and return it.

    Args:
        city_name (str): city name.

    Returns:
        dict: object with information about weather.
              Has keys:
              - city_name (str),
              - description (str),
              - temperature (float),
              - icon (str)
    """
    url_template = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    city_name = urllib.parse.quote_plus(city_name)
    url = url_template.format(city_name, WEATHER_API_KEY)
    try:
        response = urllib.request.urlopen(url).read()
    except urllib.error.HTTPError:
        return dict(error=True)

    r = json.loads(response)

    weather_data = {
        'city': r['name'],
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    return weather_data
