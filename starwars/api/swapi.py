import urllib.request, json 

def get_sw_films():
    sw_films = urllib.request.urlopen("https://swapi.dev/api/films")
    # print(films_api)
    sw_films = json.loads(sw_films.read())
    sw_films = sw_films['results']
    return sw_films