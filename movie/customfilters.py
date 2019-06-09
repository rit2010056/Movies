from .models import Movie, Genre
import django_filters

class GenreFilters(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='iexact')

    # created_by = django_filters.CharFilter(method="created_by_filter",)


    class Meta:
        model = Genre
        fields = ['name']

    # def created_by_filter(self, queryset, name, value):
    #     return queryset.filter(created_by__username=value)


class MovieFilters(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='iexact')
    popularity = django_filters.CharFilter(field_name="popularity", lookup_expr='iexact')
    director = django_filters.CharFilter(field_name="director", lookup_expr='iexact')
    imdb_score  = django_filters.NumberFilter(field_name="imdb_score", lookup_expr='iexact')

    class Meta:
        model = Movie
        fields = ['name', "popularity", "director", "imdb_score"]


