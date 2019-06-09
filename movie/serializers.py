from rest_framework import serializers
from .models import Movie, Genre

class Genreserielizer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MoviesSerializer(serializers.ModelSerializer):

    genre = Genreserielizer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = [
                    "popularity",
                    "name",
                    "genre",
                    "director",
                    "imdb_score",
                ]
