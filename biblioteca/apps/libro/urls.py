from django.urls import path
from .views import Home

urlpatterns = [
    path('', Home , name = 'index')
    #parametro 1: texto que recibe cuando escribes en la barra de direcciones (url) , sirve para entrar a la logica de Home
    #parametro 2: funcion de la vista para pintar en html
    #parametro 3: identificador para la url ,es como un recordardo de la url dentro de vistas
]
