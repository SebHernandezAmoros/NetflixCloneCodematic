from email.mime import image
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Movie

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.
def index(request):
    return HttpResponse("Hello World", status=200)
def abaut(request):
    return HttpResponse("Abaut", status=200)
def movies_index(request):
    #Esta obteniendo todos los datos de la tabla movie
    movies = Movie.objects.all()
    return render (request,"movies/index.html", {'movies':movies})
def movies_create(request):
    return render (request,"movies/create.html")
def movies_store(request):
    print(request.POST)
    print(request.FILES)

    image = request.FILES['image']
    path = default_storage.save("posters/"+image.name, ContentFile(image.read()))
    print(path)
    print(request.POST["Titulo"])
    #movie = Movie()
    #movie.name = request.POST["Titulo"]
    #movie.save()
    return redirect("movie_index")

def movies_json(request):
    movies = Movie.objects.all()
    json_movies =[]
    for movie in movies:
        movie={
            "title": movie.name
        }
        json_movies.append(movie)
    return JsonResponse(json_movies, safe=False)