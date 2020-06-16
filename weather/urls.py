from django.conf.urls import url

from .views import HomeView, CityListView, DeleteCityView

app_name = 'weather'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^cities$', CityListView.as_view(), name='search_results'),
    url(r'^delete-city$', DeleteCityView.as_view(), name='delete_city'),
    #url(r'^(?P<city_name>\\d+)$', CityWeatherView.as_view(), name='city_weather')
]
