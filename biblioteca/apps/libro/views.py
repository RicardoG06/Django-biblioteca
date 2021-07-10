from django.shortcuts import render, redirect
from .forms import AutorForm

# Create your views here.
def Home(request): #request Home recibe una peticion por request
    return render(request , 'index.html')
    #parametro 1 : request es la peticion que se realiza
    #parametro 2 : render pinta en un template la informacion

def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save() #Save : guardar en la bd lo que se envia en el formulario
            return redirect('index')
    else:
        autor_form = AutorForm()
    return render(request , 'libro/crear_autor.html' , {'autor_form':autor_form})
