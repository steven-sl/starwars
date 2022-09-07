import urllib.request, json 
import os.path

def get_sw_films():
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


    return sw_films