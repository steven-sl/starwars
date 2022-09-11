from django.urls import path
from .views import def_view

app_name = 'starwars'
urlpatterns = [
    path('', def_view.index, name="index"),

    path('film/<int:episode_id>/', def_view.film_view, name="film_view"),
    
    # path('character/<int:character_id>/', def_view.char_detail, name="char_detail"),
    path('character/<str:char_id>/', def_view.char_detail, name="char_detail"),

    path('planets/', def_view.planets, name="planets"),
    path('starships/', def_view.starships, name="starships"),
    path('starships/', def_view.starships, name="starships"),

    # Testing
    path('clearcache/', def_view.clearcache, name="clearcache"),




]