from django.shortcuts import render
from django.http import HttpResponse
from .models import Theater
# Create your views here.


def home(request):
    return render(request, 'home.html')

def seoul(request):
    unique_sigu = Theater.objects.filter(location='서울').values('sigu').distinct()
    context = {'unique_sigu': unique_sigu}
    return render(request, 'seoul.html', context)

def gyeonggiAndIncheon(request):
    return render(request, 'gyeonggiAndIncheon.html')