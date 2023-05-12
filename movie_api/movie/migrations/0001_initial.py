# Generated by Django 4.2 on 2023-05-12 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('cast', models.CharField(max_length=100)),
                ('nation', models.CharField(max_length=100)),
                ('age_limit', models.CharField(max_length=100)),
                ('running_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TheaterMovieSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=100)),
                ('theater_type', models.CharField(max_length=100)),
                ('theater_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('movie_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movieinfo')),
            ],
        ),
    ]
