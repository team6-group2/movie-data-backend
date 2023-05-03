from django.db import models

class Theater(models.Model):
    theater_type = models.CharField(max_length=100)
    theater_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sigu = models.CharField(max_length=100)

    def __str__(self):
        return self.theater_name