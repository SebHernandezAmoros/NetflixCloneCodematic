from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World", status=200)
def abaut(request):
    return HttpResponse("Abaut", status=200)