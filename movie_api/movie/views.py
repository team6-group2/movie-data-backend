from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from movie.models import TheaterMovieSchedule, MovieInfo
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

def redirectCorrectCity(request):
    city = request.GET.get('city')

    if city == 'seoul':
        return redirect(reverse('movie:seoul'))
    elif city == 'gyeonggi':
        return redirect(reverse('movie:gyeonggiAndIncheon'))
    else:
        #return redirect(reverse('movie:home'))
        return HttpResponse('잘못된 접근입니다.')

def movieScheduleDetail(request, city, district):
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
    return render(request, 'movieScheduleDetail.html', {'movie_schedules': movie_schedules})

def movieInfoDetail(request, movie_title):
    movie_info_data = MovieInfo.objects.get(movie_title=movie_title)
    movie_info = {}
    movie_info["movie_title"] = movie_info_data.movie_title
    movie_info["director"] = movie_info_data.director
    movie_info["cast"] = movie_info_data.cast
    movie_info["nation"] = movie_info_data.nation
    movie_info["age_limit"] = movie_info_data.age_limit
    movie_info["running_time"] = movie_info_data.running_time

    return render(request, 'movieInfoDetail.html', {'movie_info': movie_info})