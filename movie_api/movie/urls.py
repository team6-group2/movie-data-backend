from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.home, name='home'),
    path('seoul/', views.seoul, name='seoul'),
    path('gyeonggi-incheon/', views.gyeonggiAndIncheon, name='gyeonggiAndIncheon'),
    #path('<char:sigu_name>/', views.movieTimeDetail, name='MovieTimeDetail'),
]