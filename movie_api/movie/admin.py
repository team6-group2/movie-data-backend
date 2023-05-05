from django.contrib import admin
from .models import MovieInfo, TheaterMovieSchedule

@admin.register(MovieInfo)
class MovieInfoAdmin(admin.ModelAdmin):
    list_display = ['movie_title', 'director', 'cast', 'nation', 'age_limit', 'running_time']

@admin.register(TheaterMovieSchedule)
class TheaterMovieScheduleAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'theater_type', 'theater_name', 'movie_info']