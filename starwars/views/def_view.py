from django.shortcuts import render
from ..api.swapi import get_sw_films, get_sw_planets, get_sw_starships
import urllib.request, json 
import os.path

# Create your views here.
def index(request):
    # print("Test1")
    films_list = get_sw_films()
    # print(films_list)
    if (request.GET):
        keyword = request.GET.get('keyword')
        if not keyword.isspace():
            films_list = film_search(keyword)
        else:
            keyword = '' #removing spaces in the search bar

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
            # Get character's unique ID
            # ex) https://swapi.dev/api/people/1
            # Will need to get 1 at the end

            char_url = film['characters'][i].split('/')
            char_url = [split for split in char_url if split]
            char_id = char_url[-1] #the last number is the ID
            # print(char_url)

            char = json.loads(char.read())
            
            # TOOD: Make a separate function for this:
            if os.path.exists("static/media/characters/" + char['name'] + ".jpg"):
            # link to downloaded images
                char['img_url'] = "media/characters/" + char['name'] + ".jpg"
            else:
            # link to failover image 
                char['img_url'] = "media/fallback_poster.png"
            
            char['char_id'] = char_id
            char['char_url'] = film['characters'][i]


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
            planet = json.loads(planet.read())
            if os.path.exists("static/media/planets/" + planet['name'] + ".jpg"):
            # link to downloaded images
                planet['img_url'] = "media/planets/" + planet['name'] + ".jpg"
            else:
            # link to failover image 
                planet['img_url'] = "media/fallback_poster.png"
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
            if os.path.exists("static/media/vehicles/" + vehicle['name'] + ".jpg"):
            # link to downloaded images
                vehicle['img_url'] = "media/vehicles/" + vehicle['name'] + ".jpg"
            else:
            # link to failover image 
                vehicle['img_url'] = "media/fallback_poster.png"
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

def film_search(keyword):
    sw_films = get_sw_films()
    print(keyword)
    sw_films = [x for x in sw_films if keyword.lower() in x['title'].lower()]
    # print(sw_films)

    return sw_films

def char_detail(request, char_id):
    url = 'https://swapi.dev/api/people/' + char_id

    char = urllib.request.urlopen(url)
    char = json.loads(char.read())

    char_films = []
    for i in range(5):
        try: # for failover
            # PARSE URL
            film = urllib.request.urlopen(char['films'][i])
            film = json.loads(film.read())
            if os.path.exists("static/media/films/" + film['title'] + ".jpg"):
            # link to downloaded images
                film['img_url'] = "media/films/" + film['title'] + ".jpg"
            else:
            # link to failover image 
                film['img_url'] = "media/fallback_poster.png"
            char_films.append(film)
        except:
            break

    return render(request, 'char_view.html', locals())
