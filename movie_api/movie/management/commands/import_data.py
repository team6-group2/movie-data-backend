# 영화관 지역 관련 데이터 업로드
# python manage.py import_data로 실행
import json
from django.core.management.base import BaseCommand
from movie.models import Theater

class Command(BaseCommand):
    help = 'Import data from JSON file'

    def handle(self, *args, **options):
        json_file_path = './data/mega_theater_loc_data.json'
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for row in data:
                Theater.objects.create(
                    theater_type=row['theater_type'],
                    theater_name=row['theater_name'],
                    location=row['location'],
                    sigu=row['sigu']
                )
        self.stdout.write(self.style.SUCCESS('Megabox location data imported successfully.'))

        json_file_path = './data/lotte_theater_loc_data.json'
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for row in data:
                Theater.objects.create(
                    theater_type=row['theater_type'],
                    theater_name=row['theater_name'],
                    location=row['location'],
                    sigu=row['sigu']
                )
        self.stdout.write(self.style.SUCCESS('Lotte cinema location data imported successfully.'))

        json_file_path = './data/cgv_theater_loc_data.json'
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for row in data:
                Theater.objects.create(
                    theater_type=row['theater_type'],
                    theater_name=row['theater_name'],
                    location=row['location'],
                    sigu=row['sigu']
                )
        self.stdout.write(self.style.SUCCESS('cgv location data imported successfully.'))