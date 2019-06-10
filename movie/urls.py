from rest_framework.routers import SimpleRouter
from .views import  ListCreateDeleteMovieView


router = SimpleRouter()
router.register("", ListCreateDeleteMovieView)

urlpatterns = router.urls
