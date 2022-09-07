from django.shortcuts import render
from ..api.swapi import get_sw_films

# Create your views here.
def index(request):
    # print("Test1")
    films_list = get_sw_films()
    # print(films_list)
    return render(request, 'index.html', locals())