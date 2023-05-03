from rest_framework import serializers
from .models import *

class MovieInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = ("__all__")
        fields = ('movie_title', 'director', 'actor', 'deploy', 'genre', 'country', 'age', 'running')

class TheaterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheaterInfo
        fields = ("__all__")
        fields = ('theater_type', 'theater_name', 'location', 'movie_title', 'start_time')


# MovieInfoSerializer 도 구현? 

## - serialiezer란 장고 모델 데이터를 json타입으로 바꿔주는 작업을 해준다. 즉 직렬화 작업을 해준다.
## - 장고 모델 데이터를 json으로 바꿔주면 api 통신을 할 때 훨씬 편하게 작업할 수 있다.