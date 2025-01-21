from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Привет мир!')

def home(request):
    return render(request, 'home.html')