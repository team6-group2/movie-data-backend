from django.contrib import admin
from .models import Theater

class TheaterAdmin(admin.ModelAdmin):
    list_display = ('theater_type', 'theater_name', 'location', 'sigu')

admin.site.register(Theater, TheaterAdmin)