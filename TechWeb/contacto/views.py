from django.shortcuts import render
from servicios.models import Servicio
from TechApp import views


def contacto(request):
    return render (request, "contacto/contacto.html")
    # return render (request, "servicios/servicios.html", {"servicios":servicios})