from django.contrib import admin
from django.urls import path, include
from movie.views import ListCreateDeleteGenreView
from rest_framework.routers import DefaultRouter

app_name = 'Movie'

router = DefaultRouter()
router.register(r'genre', ListCreateDeleteGenreView, basename='genre')
urlpatterns = router.urls

urlpatterns += [
    path('user/', include('user.urls') ),
    path('admin/', admin.site.urls),
    path('movie/', include('movie.urls')),
]