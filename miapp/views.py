from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Estudiante

# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'index.html')

def saludo(request):
    return render(request, 'saludo.html')

def integrantes(request):
    return render(request, 'integrantes.html')

def agregar_estudiante(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        dni = request.POST['dni']
        nombre = request.POST['nombre']
        apepat = request.POST['apepat']
        apemat = request.POST['apemat']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        estado = request.POST['estado'] == 'True'  # Convertir a booleano

        estudiante = Estudiante(
            codigo=codigo,
            dni=dni,
            nombre=nombre,
            apepat=apepat,
            apemat=apemat,
            direccion=direccion,
            telefono=telefono,
            estado=estado
        )
        estudiante.save()
        messages.success(request, f'Se agregó correctamente el estudiante {estudiante.nombre} {estudiante.apepat} {estudiante.apemat}')
        return redirect('estudiantes')  # Redirige a la vista de estudiantes

    return render(request, 'agregar_estudiante.html')

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})

def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    messages.success(request, f'Se eliminó correctamente al estudiante {estudiante.nombre}')
    return redirect('estudiantes')
