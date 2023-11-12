from django.http import HttpResponse
from django.shortcuts import render
from .models import Ciudad

def index(request):
    return HttpResponse("hola")

def inicio(request):

    ciudades= Ciudad.objects.all()
    context = {'ciudades' : ciudades}
    return render(request, 'inicio.html', context)