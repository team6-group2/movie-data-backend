# Generated by Django 3.2.5 on 2023-05-03 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieTimeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theater_type', models.CharField(max_length=100)),
                ('theater_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('movie_title', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theater_type', models.CharField(max_length=100)),
                ('theater_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('sigu', models.CharField(max_length=100)),
            ],
        ),
    ]
