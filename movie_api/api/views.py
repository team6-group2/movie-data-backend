from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class MovieInfoViewSet(viewsets.ModelViewSet):
    queryset = MovieInfo.objects.all()
    serializer_class = MovieInfoSerializer

class TheaterInfoViewSet(viewsets.ModelViewSet):
    queryset = TheaterInfo.objects.all()
    serializer_class = TheaterInfoSerializer

"""
Viewset 장점
queryset 사용으로 반복되는 CRUD 로직을 한번에 정의할 수 있음
Router를 사용함으로써, URL설정을 다룰 필요가 없음
"""