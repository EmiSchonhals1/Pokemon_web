from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from Pokémon.models import pokémon_favorito
#importamos render para poder renderizar los archivos jinja que creamos en la carpeta templates
from django.shortcuts import render

def hello (request) :
    return render(request, "hello.html")
    

#FUNCIONES PARA RENDERIZAR CADA ENLACE DE CADA POKÉMON
def pikachu (request):
    return render(request, 'pikachu.html')

def bulbasaur (request) :
    return render(request, 'bulbasaur.html')

def charmander (request) :
    return render(request, 'charmander.html')

def squirtle (request) :
    return render(request, 'squirtle.html')

def chikorita (request) :
    return render(request, 'chikorita.html')

def treecko (request) :
    return render(request, 'treecko.html')

def chimchar (request) :
    return render(request, 'chimchar.html')

def piplup (request) :
    return render(request, 'piplup.html')

    
