from django.shortcuts import render
from ..api.swapi import get_sw_films, get_sw_planets

# Create your views here.
def index(request):
    # print("Test1")
    films_list = get_sw_films()
    # print(films_list)
    return render(request, 'index.html', locals())

def film_view(request, episode_id):
    films_list = get_sw_films()
    films_list = [x for x in films_list if x['episode_id'] == episode_id]
    
    return render(request, 'film_view.html', locals())

def planets(request):
    planets_list = get_sw_planets()
    return render(request, 'planets.html', locals())