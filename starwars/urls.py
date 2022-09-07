from django.urls import path
from .views import def_view

app_name = 'starwars'
urlpatterns = [
    path('', def_view.index, name="index"),

    path('film/<int:episode_id>/', def_view.film_view, name="film_view"),
]