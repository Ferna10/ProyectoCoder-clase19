from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.from
def curso(request):
    curso=Curso(nombre="Django", comision=939393)
    curso.save()
    texto= f"curso creado: {curso.nombre}, {curso.comision}"
    return HttpResponse(texto)


