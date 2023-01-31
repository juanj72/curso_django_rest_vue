from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import datetime as tm
from django.http.response import JsonResponse as js
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


def inicio(request):
    mensaje=[
    {'name':'juan',
    'apellido':'jara',
    'rol':'estudiante'},
    {'name':'jorge',
    'apellido':'vargas',
    'rol':'dev'}

    ]

    return js(mensaje,safe=False)


class ventanas_apis():
    def modulo1(request):
        return HttpResponse("este es una prueba desde un metodo de la clase ventanas_apis")

    def ventana_htm(request):
        zona=tm.datetime.now()
        mensaje=f'hola desde el controlador de la vista{zona}'

        return render(request,'index.html',{'mensaje':mensaje})



class First_app_view(APIView):
    def get(self,request,*args,**kwargs):
        post_m=post.objects.all()
        serializer=postSerializer(post_m,many=True)
        return Response(serializer.data)


class postDetailView(APIView):
    def get(self,request,slug_v,*args,**kwargs):
        if slug_v==None:
            slug_v='1'
        #post_m=post.objects.get(slug=slug_v)
        post_m=get_object_or_404(post,slug=slug_v)
        serializer=postSerializer(post_m)


        return Response(serializer.data)