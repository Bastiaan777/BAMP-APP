from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hola")

def inicio(request):
    return render(request, 'AppBamp/inicio.html', context)