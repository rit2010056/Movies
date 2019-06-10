from .models import Movie, Genre
import django_filters

class GenreFilters(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='iexact')

    class Meta:
        model = Genre
        fields = ['name']


class MovieFilters(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
    popularity = django_filters.NumberFilter(field_name="popularity", lookup_expr='iexact')
    director = django_filters.CharFilter(field_name="director", lookup_expr='icontains')
    imdb_score  = django_filters.NumberFilter(field_name="imdb_score", lookup_expr='iexact')
    genre = django_filters.CharFilter(field_name='genre__name', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['name', "popularity", "director", "imdb_score", "genre"]


