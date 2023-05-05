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
    movie_schedules = {}
    for schedule in schedules:
        movie_title = schedule.movie_info.movie_title
        theater_type = schedule.theater_type
        theater_name = schedule.theater_name
        start_time = schedule.start_time
        if movie_title in movie_schedules:
            if (theater_type, theater_name) in movie_schedules[movie_title]:
                movie_schedules[movie_title][(theater_type, theater_name)].append(start_time)
            else:
                movie_schedules[movie_title][(theater_type, theater_name)] = [start_time]
        else:
            movie_schedules[movie_title] = {(theater_type, theater_name): [start_time]}
    print(movie_schedules)
    return render(request, 'movieTimeDetail.html', {'movie_schedules': movie_schedules})
