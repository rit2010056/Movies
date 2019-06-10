from rest_framework import serializers
from .models import Movie, Genre

class Genreserielizer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MoviesSerializer(serializers.ModelSerializer):

    genre = Genreserielizer(many=True)
    class Meta:
        model = Movie
        fields = [
                    "popularity",
                    "name",
                    "genre",
                    "director",
                    "imdb_score",
                ]

    #
    # def create(self, validated_data):
    #     genre_data = validated_data.pop('genre')
    #     for genre in genre_data:
    #         Genre.objects.create(**genre_data)
    #     return genre_data