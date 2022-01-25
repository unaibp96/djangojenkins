from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("<img src="'https://phantom-marca.unidadeditorial.es/1dd931abcac95b6b9e302f205e0552fb/crop/29x58/773x477/resize/1320/f/jpg/assets/multimedia/imagenes/2021/12/22/16401669242106.jpg'"><p>Calladito miserable miserableeeeeeee</p> ")
