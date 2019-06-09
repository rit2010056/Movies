from django.db import models
from fynd import settings
from django.contrib.auth.models import User


class Genre(models.Model):
    class Meta:
        db_table = 'genre'

    name = models.TextField(null=False)

class Movie(models.Model):
    class Meta:
        db_table = 'movie'

    popularity = models.FloatField(null=False)
    director = models.TextField(null=False)
    imdb_score = models.FloatField(null=False)
    name = models.TextField(null=False)

    genre = models.ManyToManyField(Genre)
