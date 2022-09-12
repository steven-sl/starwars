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

![c1](https://user-images.githubusercontent.com/46691433/189576765-44b30baf-e354-42dd-b2f7-f7799c316b2e.png)
![c2](https://user-images.githubusercontent.com/46691433/189576764-fb8ca08c-b9a0-4b36-bfc5-afc206d6962d.png)
![c3](https://user-images.githubusercontent.com/46691433/189576761-7b992336-9637-440c-8b33-c94bb5151532.png)
![c4](https://user-images.githubusercontent.com/46691433/189576766-241d78e9-7a97-4f3d-b647-78b4681f93a3.png)
