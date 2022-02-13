from rest_framework import serializers
from multiapps.moviesapi.models import MovieDB

class MovieDBSerializer(serializers.ModelSerializer):
  class Meta:
    model = MovieDB
    fields = ['name', 'rating', 'release', 'duration', 'description']

