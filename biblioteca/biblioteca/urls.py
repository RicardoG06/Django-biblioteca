"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #include incluye urls pertenecientes a apps del proyecto
from apps.libro.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libro/', include(('apps.libro.urls','libro'))),
    path('home/', Home , name = 'index')
    #parametro 1: texto que recibe cuando escribes en la barra de direcciones (url) , sirve para entrar a la logica de Home
    #parametro 2: funcion de la vista para pintar en html
    #parametro 3: identificador para la url ,es como un recordardo de la url dentro de vistas

]
