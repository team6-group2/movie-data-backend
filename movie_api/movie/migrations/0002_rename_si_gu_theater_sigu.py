# Generated by Django 3.2.5 on 2023-05-03 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theater',
            old_name='si_gu',
            new_name='sigu',
        ),
    ]