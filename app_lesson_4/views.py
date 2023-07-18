from django.shortcuts import render

from django.http import HttpResponse


def home_work(request):
    return HttpResponse("<h1>Домашка по 4-му занятию</h>")
