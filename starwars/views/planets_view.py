from django.shortcuts import render
from ..api.swapi import get_sw_planets, get_sw_starships


def planets(request):
    planets_list = get_sw_planets()
    return render(request, 'planets.html', locals())
