from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная страница</h>')

def about(request):
    return HttpResponse('<h2>Страница о нас</h>')


# Create your views here.
