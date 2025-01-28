from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})

def hello_world(request):
    return HttpResponse('Привет мир!')