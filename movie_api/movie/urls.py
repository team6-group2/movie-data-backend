from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.home, name='home'),
    path('city/', views.redirectCorrectCity, name='city'),
    path('district/', views.redirectCorrectDistrict, name='district'),

    path('seoul/', views.seoul, name='seoul'),
    path('gyeonggi/', views.gyeonggi, name='gyeonggi'),
    path('incheon/', views.incheon, name='incheon'),
    

    path('<str:district>/', views.movieScheduleDetail, name='movieScheduleDetail'),
    path('movie-detail/<str:movie_title>', views.movieInfoDetail, name='movieInfoDetail')
]
