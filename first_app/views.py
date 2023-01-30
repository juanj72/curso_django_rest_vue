from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return HttpResponse("hola mundo desde mi nuevo cruso API")


class ventanas_apis():
    def modulo1(request):
        return HttpResponse("este es una prueba desde un metodo de la clase ventanas_apis")

