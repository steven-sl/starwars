import urllib.request, json 
import os.path

def get_sw_films():
    print("start")

    sw_films = urllib.request.urlopen("https://swapi.dev/api/films")
    # print(films_api)
    sw_films = json.loads(sw_films.read())
    sw_films = sw_films['results']
    sw_films.sort(key = lambda sw_films: sw_films['episode_id'], reverse = False)

    # Add images
    # print(os.path.exists('static/media/placeholder.jpg'))
    # print(files)
    for film in sw_films:
        if os.path.exists("static/media/films/" + film['title'] + ".jpg"):
            # link to downloaded images
            film['img_url'] = "media/films/" + film['title'] + ".jpg"
        else:
            # link to failover image 
            film['img_url'] = "media/fallback_poster.png"

    print("done")

    return sw_films


def get_sw_planets():
    print("test")
    sw_planets = urllib.request.urlopen("https://swapi.dev/api/planets")
    sw_planets = json.loads(sw_planets.read())
    sw_planets = sw_planets['results']

    for planets in sw_planets:
        if os.path.exists("static/media/planets/" + planets['name'] + ".jpg"):
            # link to downloaded images
            planets['img_url'] = "media/planets/" + planets['name'] + ".jpg"
        else:
            # link to failover image 
            planets['img_url'] = "media/fallback_poster.png"
    return sw_planets

def get_sw_starships():
    print("test")
    sw_starships = urllib.request.urlopen("https://swapi.dev/api/starships")
    sw_starships = json.loads(sw_starships.read())
    sw_starships = sw_starships['results']

    for starship in sw_starships:
        if os.path.exists("static/media/starship/" + starship['name'] + ".jpg"):
            # link to downloaded images
            starship['img_url'] = "media/starship/" + starship['name'] + ".jpg"
        else:
            # link to failover image 
            starship['img_url'] = "media/fallback_poster.png"
    return sw_starships