from django.db import models
from datetime import time

# Create your models here.
class MovieInfo(models.Model):
    movie_title = models.CharField(max_length=100)
    director = models.TextField(null=True)
    actor = models.TextField(null=True)
    deploy = models.DateField(null=True) 
    genre = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=100, null=True)
    running = models.IntegerField()


class TheaterInfo(models.Model):
    theater_type = models.CharField(max_length=100)
    theater_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    movie_title = models.ForeignKey(MovieInfo, on_delete=models.DO_NOTHING) 
    start_time = models.TimeField(default=time(0, 0)) # 0시 0분 ?? 

# MovieInfo
# {
# 	'movie_title': '슈퍼 마리오 브라더스', 
# 	'director': '아론 호바스, 마이클 젤레닉',
# 	'actor': '크리스 프랫, 안야 테일러 조이, 잭 블랙, 세스 로건, 찰리 데이', 
# 	'deploy': '2023.04.26', 
# 	'genre': '애니메이션, 어드벤처, 코미디',
# 	'country': '미국, 일본',
# 	'age': '전체관람가', 
# 	'running': 92 }