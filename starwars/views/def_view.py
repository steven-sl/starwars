from django.shortcuts import render

# Create your views here.
def index(request):
    print("Test1")
    return render(request, 'index.html', locals())