from rest_framework import serializers
from .models import Movie, Genre

class Genreserielizer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']

class MoviesSerializer(serializers.ModelSerializer):

    genres = Genreserielizer(many=True, source='genre')
    class Meta:
        model = Movie
        fields = [
                    "popularity",
                    "name",
                    "genres",
                    "director",
                    "imdb_score",
                ]

class MoviesCreateSerializer(serializers.ModelSerializer):

    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all(), read_only=False, source='genre')

    class Meta:
        model = Movie
        fields = [
                    "popularity",
                    "name",
                    "genres",
                    "director",
                    # "alternate_name",
                    "imdb_score",
                ]