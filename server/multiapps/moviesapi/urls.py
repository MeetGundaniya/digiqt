from django.urls import path
from Backend.urls import router
from multiapps.moviesapi.views import MoviesAPIModelViewSet



urlpatterns = [
  # path('', MoviesAPIModelViewSet.as_view(), name='movie_home'),
]


router.register('movie', MoviesAPIModelViewSet, basename='movie_api')