from django.urls import path
from .views import index
from .views import abaut

urlpatterns=[
    path("hello", index),
    path("abaut", abaut)
]