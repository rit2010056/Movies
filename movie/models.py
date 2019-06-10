from django.db import models

class Genre(models.Model):
    class Meta:
        db_table = 'genre'

    name = models.CharField(null=False,max_length=40)

class Movie(models.Model):
    class Meta:
        db_table = 'movie'

    popularity = models.FloatField(null=False)
    director = models.CharField(null=False, max_length=40)
    imdb_score = models.FloatField(null=False)
    name = models.CharField(null=False, max_length=50)
    genre = models.ManyToManyField(Genre)
