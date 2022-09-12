# Starwars

Built with Django 4.0.6 & Python 3.10.4

Run:
```sh
python manage.py runserver
```
## Features

- SW Films list 
- Film detail pages
    - Film details
    - Max 5 characters in the film
        - Each character's own detail page when clicked 
    - Max 5 planets in the film
    - Max 5 vehicles in the film
- Character detail pages
    - Max 5 films the character is casted in
        - Each film's own detail page when clicked
- Film search by title
- Planets list from nav bar
- Starships list from nav bar 
- Incomplete image datasets 
- Cahching API response for optimization
    - Saves to db.sqlite3, set as never-expire since Swapi is no longer updating
    - Manual navigation to http://127.0.0.1:8000/clearcache/ to clear cache and fetch new api response again
- Responsiveness (Bootstrap)
