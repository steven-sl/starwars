import urllib.request, json 
import os.path
from django.core.cache import cache
from datetime import date

def link_images(list_, type_, keyword):
    for item in list_:
        if os.path.exists("static/media/" + type_ + "/" + item[keyword] + ".jpg"):
            # link to downloaded images
            item['img_url'] = "media/" + type_ + "/" + item[keyword] + ".jpg"
        else:
            # link to failover image 
            item['img_url'] = "media/fallback_poster.png"
    return list_


def get_sw_films():

    # dates = "FILMS-" +  str(date.today())
    dates = "FILMS_CACHE" # If I don't want new fetch

    if cache.get(dates):
        print("getting api from DB")
        sw_films = cache.get(dates)

    else:
        print("calling api")

        sw_films = urllib.request.urlopen("https://swapi.dev/api/films")
        sw_films = json.loads(sw_films.read())
        sw_films = sw_films['results']
        sw_films.sort(key = lambda sw_films: sw_films['episode_id'], reverse = False)

        # Add images
        link_images(sw_films, "films", "title")

        # Save to DB, does not expire 
        cache.set(dates, sw_films, None)

    return sw_films


def get_sw_planets():
    
    # dates = "PLANETS-" +  str(date.today())
    dates = "PLANETS_CACHE" # If I don't want new fetch

    if cache.get(dates):
        print("getting api from DB")
        sw_planets = cache.get(dates)

    else:
        print("calling api")

        sw_planets = urllib.request.urlopen("https://swapi.dev/api/planets")
        sw_planets = json.loads(sw_planets.read())
        sw_planets = sw_planets['results']

        # Add images
        link_images(sw_planets, "planets", "name")

       
        cache.set(dates, sw_planets, None)
        
    return sw_planets

def get_sw_starships():
    # dates = "STARSHIPS-" +  str(date.today()) # Fetch only once a day
    dates = "STARSHIPS_CACHE" # If I don't want new fetch

    if cache.get(dates):
        print("getting api from DB")
        sw_starships = cache.get(dates)

    else:
        print("calling api")    
        sw_starships = urllib.request.urlopen("https://swapi.dev/api/starships")
        sw_starships = json.loads(sw_starships.read())
        sw_starships = sw_starships['results']

        link_images(sw_starships, "starships", "name")

        cache.set(dates, sw_starships, None)

    return sw_starships