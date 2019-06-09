from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import MoviesSerializer
# from rest_framework import permissions
# from rest_framework.authentication import TokenAuthentication
from .authentication import CustomAuthentication
# from .permissions import IsOwnerOrReadOnly
# from .models import Box, InventoryConditions
from .models import Movie
import django_filters
from .customfilters import MovieFilters, GenreFilters
from .permissions import Authenticated
# from django.db.models import Sum
# from datetime import timedelta
# from django.utils import timezone
# from datetime import datetime
# from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet



class ListCreateDeleteView(ModelViewSet):
    queryset = Movie.objects.all()

    authentication_classes = ( CustomAuthentication, )
    permission_classes = (Authenticated,)

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = MovieFilters

    serializer_class = MoviesSerializer

    # def get(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #
    #     return Response(serializer.data)

# class CreateMovie(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    # serializer_class = MoviesSerializer