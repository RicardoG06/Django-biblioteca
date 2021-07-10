from django.urls import path
from .views import crearAutor

urlpatterns = [
    path('crear_autor/' , crearAutor , name = 'crear_autor')
]
