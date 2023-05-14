from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from sqlalchemy import create_engine
import re
from .models import *
from django.db import IntegrityError

from crawling.current_movie.current_movie_from_daum_movie import crawl_current_movie_from_daum_movie as current_movie
from crawling.movie_schedule.today_movie_from_cgv import today_movie_from_cgv as today_movie_cgv
from crawling.movie_schedule.today_movie_from_lottecinema import today_movie_from_lottecinema as today_movie_lottecinema
from crawling.movie_schedule.today_movie_from_megabox import crawl_today_movie_from_megabox as today_movie_megabox

engine = create_engine('sqlite://///Users/0bver/project/6-2/movie-data-backend/movie_api/db.sqlite3')


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)

    @scheduler.scheduled_job('cron', hour=0, minute=1, id="111", name='expiry_check')
    def auto_check():
        print('[task start]')
        # scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
        webdriver_options = webdriver.ChromeOptions() 
        webdriver_options.add_argument("--headless=new")
        webdriver_options.add_argument('--no-sandbox')
        webdriver_options.add_argument('--disable-dev-shm-usage')
        webdriver_options.add_argument("--disable-gpu")
        webdriver_options.add_argument('window-size=1920x1080')
        webdriver_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
        webdriver_options.add_argument("lang=ko_KR")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=webdriver_options)

        MovieInfo.objects.all().delete()
        TheaterMovieSchedule.objects.all().delete()

        for idx, row in current_movie(driver).iterrows():
            try:
                movie_info = MovieInfo.objects.create(
                    movie_title=row['movie_title'],
                    director=row['director'],
                    cast=row['cast'],
                    nation=row['nation'],
                    age_limit=row['age_limit'],
                    running_time=row['running_time']
                )
                # print(f'{movie_info.movie_title} 정보 입력 완료')
            except IntegrityError:
                # movie_info = MovieInfo.objects.get(movie_title=row['movie_title'])
                # print(f'{movie_info.movie_title} 정보 이미 존재')
                pass

        for df in [today_movie_cgv(driver), today_movie_lottecinema(driver)]:
            for idx, row in df.iterrows():
                try:
                    search_term = re.sub(r'[-]', '. ', row['movie_title'])
                    movie_info = MovieInfo.objects.get(movie_title__regex=search_term)
                except MovieInfo.DoesNotExist:
                    print(f"{row['movie_title']} 정보 없음")
                    continue
                try:
                    TheaterMovieSchedule.objects.create(
                        movie_info=movie_info,
                        start_time=row['start_time'],
                        theater_type=row['theater_type'],
                        theater_name=row['theater_name'],
                        city=row['city'],
                        # district=row['district']
                        district=''
                    )
                    # print(f"{movie_info.movie_title} {row['theater_name']} 스케줄 입력 완료")
                except IntegrityError:
                    # print(f"{movie_info.movie_title} {row['theater_name']} 스케줄 이미 존재")
                    pass

        driver.quit()
        print('[task end]')

    scheduler.start()