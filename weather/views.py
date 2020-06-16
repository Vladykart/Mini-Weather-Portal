from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView
from django.views.generic.base import TemplateView
from .models import City
from .forms import CityForm
from .service import weather_by_city_name
from django.http import JsonResponse
from datetime import datetime
from django.utils.dateparse import parse_date
from dateutil import parser

from django.core.paginator import Paginator

import requests


class HomeView(TemplateView):
    template_name = 'home.html'
    partial_template_name = 'city_weather_partial.html'

    def get_city_data(self, request):
        form = CityForm(request.POST)
        if not form.is_valid():
            raise Exception('Invalid city name')
        city_name = form.cleaned_data['name']
        city_data = weather_by_city_name(city_name)
        if not city_data:
            raise Exception('City weather not found')
        exists = City.objects.filter(name=city_name).first()
        if not exists:
            city = form.save(commit=False)
            city.description = city_data['description']
            city.icon = city_data['icon']
            city.temperature = city_data['temperature']
            city.save()
        return city_data

    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = CityForm()

        return context

    def post(self, request, *args, **kwargs):
        error = False
        city_data = None
        try:
            city_data = self.get_city_data(request)
        except Exception as e:
            error = str(e)

        return render(request, self.partial_template_name, {
            'error': error,
            'city_data': city_data
        })


class CityListView(ListView):
    template_name = 'cities.html'
    model = City
    paginate_by = 3

    def get_queryset(self):
        query = 'SELECT * FROM weather_city'
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        params = []
        if date_from:
            date_from = parser.parse(date_from).strftime('%Y-%m-%d')
            params.append(date_from)
            query += " WHERE created >= %s "
        if date_to:
            date_to = parser.parse(date_to).strftime('%Y-%m-%d')
            params.append(date_to)
            if date_from:
                query += ' AND '
            else:
                query += ' WHERE '
            query += " created <= %s "
        query += ' ORDER BY created DESC'

        return list(City.objects.raw(query, params))

    def get_context_data(self, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)
        date_from = self.request.GET.get('date_from', '')
        date_to = self.request.GET.get('date_to', '')

        filter = []

        if date_from:
            filter.append('date_from=' + date_from)

        if date_to:
            filter.append('date_to=' + date_to)

        filter = '&'.join(filter)

        if filter:
            filter = '&' + filter

        context['filter'] = filter
        context['date_from'] = date_from
        context['date_to'] = date_from

        return context


class DeleteCityView(TemplateView):
    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        City.objects.get(id=id).delete()
        return JsonResponse(
            {'success': True}
        )
