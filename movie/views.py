from .serializers import MoviesSerializer, Genreserielizer, MoviesCreateSerializer
from .authentication import CustomAuthentication
from .models import Movie, Genre
import django_filters
from .customfilters import MovieFilters, GenreFilters
from .permissions import Authenticated
from rest_framework.viewsets import ModelViewSet



class ListCreateDeleteMovieView(ModelViewSet):

    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return MoviesCreateSerializer
        else:
            return MoviesSerializer

    authentication_classes = ( CustomAuthentication, )
    permission_classes = (Authenticated,)

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = MovieFilters


class ListCreateDeleteGenreView(ModelViewSet):
    queryset = Genre.objects.all()

    authentication_classes = ( CustomAuthentication, )
    permission_classes = (Authenticated,)
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    serializer_class = Genreserielizer
    filter_class = GenreFilters