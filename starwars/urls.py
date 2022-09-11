from django.urls import path
from .views import def_view, planets_view, starships_view

app_name = 'starwars'
urlpatterns = [
    path('', def_view.index, name="index"),

    path('film/<int:unique_id>/', def_view.film_view, name="film_view"),
    
    path('character/<str:char_id>/', def_view.char_detail, name="char_detail"),

    path('planets/', planets_view.planets, name="planets"),
    path('starships/', starships_view.starships, name="starships"),

    # Testing
    path('clearcache/', def_view.clearcache, name="clearcache"),




]