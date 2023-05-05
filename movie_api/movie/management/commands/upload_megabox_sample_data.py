import json
from django.core.management.base import BaseCommand
from movie.models import TheaterMovieSchedule, MovieInfo

class Command(BaseCommand):
    help = 'Upload TheaterMovieSchedule info from JSON file'

    def handle(self, *args, **options):
        json_file_path = './data/megabox_sample_data.json'

        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for schedule_data in data:
            movie_title = schedule_data['movie_title']
            start_time = schedule_data['start_time']
            theater_type = schedule_data['theater_type']
            theater_name = schedule_data['theater_name']
            city = schedule_data['city']
            district = schedule_data['district']

            # Get or create MovieInfo
            movie_info, _ = MovieInfo.objects.get_or_create(movie_title=movie_title)

            # Create TheaterMovieSchedule
            schedule = TheaterMovieSchedule.objects.create(
                movie_info=movie_info,
                start_time=start_time,
                theater_type=theater_type,
                theater_name=theater_name,
                city=city,
                district=district
            )

        self.stdout.write(self.style.SUCCESS('Data uploaded successfully.'))