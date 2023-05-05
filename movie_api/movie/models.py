from django.db import models

class MovieInfo(models.Model):
    movie_title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=100)
    nation = models.CharField(max_length=100)
    age_limit = models.CharField(max_length=100)
    running_time = models.CharField(max_length=100)

    def __str__(self):
        return self.movie_title

class TheaterMovieSchedule(models.Model):
    movie_info = models.ForeignKey(MovieInfo, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=100)
    theater_type = models.CharField(max_length=100)
    theater_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.theater_name} - {self.movie_info.movie_title}"