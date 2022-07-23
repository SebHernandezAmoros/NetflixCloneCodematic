from django.urls import path
from .views import index
from .views import abaut
from .views import movies_index
from .views import movies_create
from .views import movies_store
from .views import movies_json

urlpatterns=[
    path("hello", index),
    path("abaut", abaut),
    path('movies', movies_index, name="movie_index"),
    path('movies/create', movies_create),
    path('movies/store', movies_store),
    path('json/movies', movies_json)
]