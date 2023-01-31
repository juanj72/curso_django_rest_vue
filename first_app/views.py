from django.shortcuts import render
from django.http import HttpResponse
import datetime as tm
from django.http.response import JsonResponse as js


def inicio(request):
    mensaje={
    'name':'juan',
    'apellido':'jara',
    'rol':'estudiante'

    }

    return js(mensaje)


class ventanas_apis():
    def modulo1(request):
        return HttpResponse("este es una prueba desde un metodo de la clase ventanas_apis")

    def ventana_htm(request):
        zona=tm.datetime.now()
        mensaje=f'hola desde el controlador de la vista{zona}'

        return render(request,'index.html',{'mensaje':mensaje})

