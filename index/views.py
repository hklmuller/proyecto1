from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenidos a mi proyecto de Django</h1>')

def plantilla(request):

    template = loader.get_template('plantilla.html')

    datos = {
        'lista': ['primero', 'segundo', 'tercero']
        'nombre': 'Leandro'
    }


    plantilla_generada = template.render({})

    return HttpResponse('planilla_generada')    
