from django.shortcuts import render

# Create your views here.
def Home(request): #request Home recibe una peticion por request
    return render(request , 'libro/index.html')
    #parametro 1 : request es la peticion que se realiza
    #parametro 2 : render pinta en un template la informacion 
