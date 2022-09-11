from django.shortcuts import render
from ..api.swapi import get_sw_planets, get_sw_starships


def starships(request):
    starships_list = get_sw_starships()
    return render(request, 'starships.html', locals())
   