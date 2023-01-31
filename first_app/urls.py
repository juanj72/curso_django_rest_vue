from django.urls import path,include
from first_app import views

urlpatterns=[
    path('inicio',views.inicio,name='inicio'),
    path('inicio2',views.ventanas_apis.modulo1,name='modulo1'),
    path('template',views.ventanas_apis.ventana_htm,name='template')
]