# 롯데시네마 크롤링 정보 올리는 코드
import json
from django.core.management.base import BaseCommand
from movie.models import MovieTimeDetail

class Command(BaseCommand):
    help = 'Import data from JSON file'

    def handle(self, *args, **options):
        json_file_path = './data/test.json'
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for row in data:
                MovieTimeDetail.objects.create(
                    theater_type=row['theater_type'],
                    theater_name=row['theater_name'],
                    location=row['location'],
                    movie_title=row['movie_title'],
                    start_time=row['start_time'],
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))