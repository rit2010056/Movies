from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    class Meta:
        db_table = 'genre'

    name = models.CharField(null=False, max_length=40, unique=True)


class Movie(models.Model):
    class Meta:
        db_table = 'movie'

    popularity = models.FloatField(null=False, validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ])
    director = models.CharField(null=False, max_length=40)
    imdb_score = models.FloatField(null=False, validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])
    name = models.CharField(null=False, max_length=50)
    genre = models.ManyToManyField(Genre)
