from django.shortcuts import render
from servicios.models import Servicio
from TechApp import views


def home(request):
    return render (request, "TechApp/home.html")

