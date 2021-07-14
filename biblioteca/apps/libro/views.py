from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import Autors
from django.core.exceptions import ObjectDoesNotExist

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

def listarAutor(request):
    autores = Autors.objects.filter(estado = True)
    return render (request, 'libro/listar_autor.html',{'autores':autores})

def editarAutor(request , id):
    autor_form = None
    error = None
    try:
        autor = Autors.objects.get(id = id)
        if request.method == 'GET':
            autor_form = AutorForm(instance = autor)
        else:
            autor_form = AutorForm(request.POST , instance = autor)
            if autor_form.is_valid:
                autor_form.save()
                return redirect('index')
    except ObjectDoesNotExist as e:
        error = e

    return render(request ,'libro/crear_autor.html' , {'autor_form':autor_form, 'error':error})

#Eliminar de manera directa - eliminacion definitiva
# def eliminarAutor(request , id):
#     autor = Autors.objects.get(id = id)
#     autor.delete()
#     return redirect('libro:listar_autor')

#Eliminando por post - eliminacion definitiva
# def eliminarAutor(request , id):
#     autor = Autors.objects.get(id = id)
#     if request.method == 'POST':
#         autor.delete()
#         return redirect('libro:listar_autor')
#     return render(request ,'libro/eliminar_autor.html' , {'autor':autor})

#Eliminando logica - eliminacion por estado - la mas recomendable
def eliminarAutor(request , id):
    autor = Autors.objects.get(id = id)
    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')
    return render(request ,'libro/eliminar_autor.html' , {'autor':autor})
