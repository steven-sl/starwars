from django.shortcuts import render
from ..api.swapi import get_sw_films, link_images
import urllib.request, json 
import os.path
from django.core.cache import cache


def clearcache(request):
    cache.clear()
    return index(request)

def index(request):
    # cache.clear() 
    films_list = get_sw_films()

    # SEARCH 
    if (request.GET):
        keyword = request.GET.get('keyword')
        if not keyword.isspace():
            films_list = film_search(keyword)
        else:
            keyword = '' #removing spaces in the search bar

    return render(request, 'index.html', locals())


# Detail film views
def film_view(request, unique_id):
    # IF CACHED
    id = str(unique_id)
    if cache.get(id + "_FILM_CACHE") and cache.get(id + "_FILM_CHARS_CACHE") and \
    cache.get(id + "_FILM_PLANETS_CACHE") and cache.get(id + "_FILM_VEHICLES_CACHE"):
        print("Getting data from DB")

        film = cache.get(id + "_FILM_CACHE")
        film_chars = cache.get(id + "_FILM_CHARS_CACHE")
        film_planets = cache.get(id + "_FILM_PLANETS_CACHE")
        film_vehicles = cache.get(id + "_FILM_VEHICLES_CACHE")
    
    else:
        print("Getting new data")
        film = get_sw_films()
        film = [x for x in film if x['unique_id'] == str(unique_id)][0]
        # print(film)


        # get max 5 characters in this film
        film_chars = []
        for i in range(5):
            try: #to prevent out of index

                # PARSE URL
                char = urllib.request.urlopen(film['characters'][i])
                char = json.loads(char.read())

                # Link images
                char = link_images([char], "characters", "name")[0]

                # Get character's unique ID
                char['char_id'] = get_id(film['characters'][i]) 

                film_chars.append(char)

            except: #exceeds 5
                break


        # get max 5 planets 
        film_planets = []
        for i in range(5):
            try: # for failover
                # PARSE URL
                planet = urllib.request.urlopen(film['planets'][i])
                planet = json.loads(planet.read())
                planet = link_images([planet], "planets", "name")[0]

                film_planets.append(planet)

            except:
                break

        # get max 5 vehicles 
        film_vehicles = []
        for i in range(5):
            try: # for failover
                # PARSE URL
                vehicle = urllib.request.urlopen(film['vehicles'][i])
                vehicle = json.loads(vehicle.read())
                vehicle = link_images([vehicle], "vehicle", "name")[0]
                
                film_vehicles.append(vehicle)

            except:
                break


        # Add date in the cache name if I want daily fetch
        cache.set(id + "_FILM_CACHE", film, None)
        cache.set(id + "_FILM_CHARS_CACHE", film_chars, None)
        cache.set(id + "_FILM_PLANETS_CACHE", film_planets, None)
        cache.set(id + "_FILM_VEHICLES_CACHE", film_vehicles,None)

    # end of if 
    return render(request, 'film_view.html', locals())


def film_search(keyword):
    sw_films = get_sw_films()
    print(keyword)
    sw_films = [x for x in sw_films if keyword.lower() in x['title'].lower()]
    # print(sw_films)

    return sw_films


def get_id(url):
    # ex) Need to get '1' from https://swapi.dev/api/people/1
    url = url.split('/')
    url = [split for split in url if split]
    return url[-1]


def char_detail(request, char_id):
    # cache.clear()
    id = str(char_id)
    if cache.get(id + "_CHAR_CACHE") and cache.get(id + "_CHAR_FILMS_CACHE"):
        print("Getting data from DB")
        char = cache.get(id + "_CHAR_CACHE")
        char_films = cache.get(id + "_CHAR_FILMS_CACHE")

    else:
        print("Getting new data")

        url = 'https://swapi.dev/api/people/' + char_id

        char = urllib.request.urlopen(url)
        char = json.loads(char.read())
        char = link_images([char], "characters", "name")[0]
        

        char_films = []
        for i in range(5):
            try: #to prevent out of index
                # PARSE URL
                film = urllib.request.urlopen(char['films'][i])
                film = json.loads(film.read())

                # Link images
                film = link_images([film], "films", "title")[0]

                # Get character's unique ID
                film['film_id'] = get_id(char['films'][i]) 

                char_films.append(film)

            except:
                break
        
        cache.set(id + "_CHAR_CACHE", char, None)
        cache.set(id + "_CHAR_FILMS_CACHE", char_films, None)


    return render(request, 'char_view.html', locals())
