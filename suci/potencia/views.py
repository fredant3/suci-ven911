from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpRequest
from .forms import FormularioIncidencias
from .models import Incidencias

def Home(request):
    return render (request, "home.html")

class FormularioIncidencias(HttpRequest):
    def index(request):
        Incidencias = FormularioIncidencias()
        return render(request, "incidencia.html")
    
    def procesar_incidencia(request):
        Incidencias = FormularioIncidencias()
        if Incidencia.is_valid():
            Incidencia.save()
            Incidencia = FormularioIncidencias()

        return render(request, "incidencia.html", {"form": Incidencia, "mensaje": 'Perfecto'})    

def Incidencia(request):
    return render (request, "incidencia.html")

def Estatus(request):
    return render (request, "estatus.html")

def Reportes(request):
    return render (request, "reportes.html")

