from django.shortcuts import render
from servicios.models import Servicio
from TechApp import views

def servicios(request):
    servicios=Servicio.objects.all()
    return render (request, "servicios/servicios.html", {"servicios":servicios})
