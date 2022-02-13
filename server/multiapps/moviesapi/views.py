# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions

from django_filters.rest_framework import DjangoFilterBackend

from multiapps.moviesapi.models import MovieDB
from multiapps.moviesapi.serializers import MovieDBSerializer
from multiapps.moviesapi.paginations import MoviesPagination



# Create your views here.

class MoviesAPIModelViewSet(ModelViewSet):
  queryset = MovieDB.objects.all()
  serializer_class = MovieDBSerializer

  pagination_class = MoviesPagination
  
  authentication_classes = [SessionAuthentication]
  permission_classes = [DjangoModelPermissions]
  
  filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
  
  filterset_fields  = ['name', 'description']
  search_fields = ['name', 'description']
  ordering_fields = ['name', 'rating', 'release', 'duration']
  ordering = ['-release']
