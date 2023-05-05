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

def movieTimeDetail(request, sigu):
    # Theater와 MovieTimeDetail 테이블을 조인하여 필요한 필드 값을 가져옵니다.
    movie_details = MovieTimeDetail.objects.filter(theater__sigu=sigu)

    # 필요한 필드 값을 리스트로 저장합니다.
    theater_names = [detail.theater.theater_name for detail in movie_details]
    theater_types = [detail.theater.theater_type for detail in movie_details]
    locations = [detail.theater.location for detail in movie_details]
    movie_titles = [detail.movie_title for detail in movie_details]
    start_times = [detail.start_time for detail in movie_details]

    # 필요한 필드 값을 context에 저장합니다.
    context = {
        'theater_names': theater_names,
        'theater_types': theater_types,
        'locations': locations,
        'movie_titles': movie_titles,
        'start_times': start_times,
        'sigu': sigu
    }
    print("---------------------------------------------------------------------------------------------")
    print(movie_details)
    return render(request, 'movieTimeDetail.html', context)