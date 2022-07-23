from contextlib import nullcontext
from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Movie(models.Model) :
    name = models.CharField(max_length=255, null=True)
    #Upload_to crea una subcarpeta en la capeta media
    poster = models.ImageField(upload_to='posters', null = True)