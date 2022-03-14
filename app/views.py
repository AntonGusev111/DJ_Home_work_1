import os
from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().time()
    time_format = "%H:%M:%S"

    msg = f"Текущее время: {current_time:{time_format}}"
    return HttpResponse(msg)


def workdir_view(request):
    dir = directory_list()
    return HttpResponse(dir)



def directory_list():
    dir = []
    for n, name in enumerate(sorted(os.listdir(path="."))):
        dir.append(f"{n+1}-{name}, ")
    return (dir)

