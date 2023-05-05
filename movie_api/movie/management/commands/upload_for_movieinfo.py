import json
from django.core.management.base import BaseCommand
from movie.models import MovieInfo

class Command(BaseCommand):
    help = 'Upload movie info from JSON file'

    def handle(self, *args, **options):
        json_file_path = './data/movieinfo.json'
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for movie_data in data:
                movie_info = MovieInfo(
                    movie_title=movie_data['movie_title'],
                    director=movie_data['director'],
                    cast=movie_data['cast'],
                    nation=movie_data['nation'],
                    age_limit=movie_data['age_limit'],
                    running_time=movie_data['running_time']
                )
                movie_info.save()

        self.stdout.write(self.style.SUCCESS('Data uploaded successfully.'))