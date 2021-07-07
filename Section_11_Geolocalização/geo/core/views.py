from django.shortcuts import render
from django.views.generic import View

from .utils import yelp_search, get_client_city_data

class IndexView(View):

    def get(self, request, *args, **kwargs):
        items = []

        city = None

        while not city:
            ret = get_client_city_data()
            if ret:
                city = ret['city']

        g = request.GET.get('key', None)
        loc = request.GET.get('loc', None)
        location = city

        context = {
            'city': city,
            'busca': False,
        }

        if loc:
            location = loc
        if g:
            items = yelp_search(keyword=g, location=loc)
            context = {
                'items': items,
                'city': location,
                'busca': True,
            }
        return render(request, 'index.html', context)
