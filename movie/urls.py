from .views import ListCreateDeleteView
from django.conf.urls import url

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'movie', ListCreateDeleteView, basename='movie')
# urlpatterns = router.urls

from rest_framework.routers import SimpleRouter

from .views import ListCreateDeleteView

router = SimpleRouter()
router.register("", ListCreateDeleteView)

urlpatterns = router.urls

# urlpatterns = [
#     url(r'^$', ListCreateDeleteView.as_view()),
#     # url(r'^$', CreateMovie.as_view()),
#     # url(r'^(?P<pk>\d+)$', CreateMovie.as_view(), name="Update and delete boxes"),
#     # url(r'list_user_boxes',ListUserBoxes.as_view(), name="list user's boxes"),
#
# ]
