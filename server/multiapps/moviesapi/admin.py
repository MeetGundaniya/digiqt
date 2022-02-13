from django.contrib import admin
from multiapps.moviesapi.models import MovieDB

# Register your models here.

class MovieDBModelAdmin(admin.ModelAdmin):
  list_display = ('name', 'rating', 'release', 'duration')
  search_fields = ('name',)
  list_filter = ('rating',)
  list_per_page = 15



admin.site.register(MovieDB, MovieDBModelAdmin)