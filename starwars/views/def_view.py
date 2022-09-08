from django.shortcuts import render
from ..api.swapi import get_sw_films, get_sw_planets
import urllib.request, json 

# Create your views here.
def index(request):
    # print("Test1")
    films_list = get_sw_films()
    # print(films_list)
    return render(request, 'index.html', locals())

def film_view(request, episode_id):
    film = get_sw_films()
    film = [x for x in film if x['episode_id'] == episode_id]
    film = film[0]


    

    # get max 5 characters in this film
    film_chars = []
    for i in range(5):
        if(film['characters'][i]):
            # PARSE URL
            char = urllib.request.urlopen(film['characters'][i])
    # print(films_api)
            char = json.loads(char.read())
            film_chars.append(char)
    # print(film['characters'])

    # get max 5 planets 
    
    return render(request, 'film_view.html', locals())

def planets(request):
    planets_list = get_sw_planets()
    return render(request, 'planets.html', locals())