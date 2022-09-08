from django.shortcuts import render
from ..api.swapi import get_sw_films, get_sw_planets, get_sw_starships
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
        # if(film['characters'][i]): # for failover
        try:
            # PARSE URL
            char = urllib.request.urlopen(film['characters'][i])
    # print(films_api)
            char = json.loads(char.read())
            film_chars.append(char)
        except:
            break
    # print(film['characters'])

    # get max 5 planets 
    film_planets = []
    for i in range(5):
        try: # for failover
            # PARSE URL
            planet = urllib.request.urlopen(film['planets'][i])
    # print(films_api)
            planet = json.loads(planet.read())
            film_planets.append(planet)
        except:
            break

    # get max 5 vehicles 
    film_vehicles = []
    for i in range(5):
        try: # for failover
            # PARSE URL
            vehicle = urllib.request.urlopen(film['vehicles'][i])
    # print(films_api)
            vehicle = json.loads(vehicle.read())
            film_vehicles.append(vehicle)
        except:
            break
    
    return render(request, 'film_view.html', locals())

def planets(request):
    planets_list = get_sw_planets()
    return render(request, 'planets.html', locals())

def starships(request):
    starships_list = get_sw_starships()
    return render(request, 'starships.html', locals())