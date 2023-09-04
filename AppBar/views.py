from django.http import HttpResponse
from django.shortcuts import render


def inicio(req):
    return render(req, "inicio.html")

def productos(req):
    return render(req, 'productos.html')

def inicio(request):
    return render(request, 'inicio.html')
