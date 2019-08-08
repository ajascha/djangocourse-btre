from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # '<h1>Hello world</h1>')
    return render(request, 'pages/index.html')
    # return HttpResponse('Hello world')


def about(request):
    return render(request, 'pages/about.html')
