from django.shortcuts import render
from django.http import HttpResponse
from movie.models import TheaterMovieSchedule
#from .models import Theater, MovieTimeDetail
# Create your views here.


def home(request):
    return render(request, 'home.html')

def seoul(request):
    districts = TheaterMovieSchedule.objects.filter(city='서울').values('district').distinct()
    district_list = [district['district'] for district in districts]
    return render(request, 'seoul.html', {'districts': district_list})

def gyeonggiAndIncheon(request):
    return render(request, 'gyeonggiAndIncheon.html')

def movieTimeDetail(request, city, district):
    schedules = TheaterMovieSchedule.objects.filter(district=district)
    return render(request, 'movieTimeDetail.html', {'schedules': schedules})