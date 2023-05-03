from django.contrib import admin
from .models import Theater, MovieTimeDetail

class TheaterAdmin(admin.ModelAdmin):
    list_display = ('theater_type', 'theater_name', 'location', 'sigu')

admin.site.register(Theater, TheaterAdmin)

class MovieTimeDetailAdmin(admin.ModelAdmin):
    list_display = ('theater_type', 'theater_name', 'location', 'movie_title', 'start_time')

admin.site.register(MovieTimeDetail, MovieTimeDetailAdmin)