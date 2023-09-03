from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente

# Create your views here.
def cliente(req, nombre, apellido, telefono, email):

    cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono, email=email)
    cliente.save()

    return HttpResponse(f"""
        <p>Cliente: {Cliente.nombre} - Apellido: {Cliente.apellido} - Telefono{Cliente.telefono} - Email: {Cliente.email} agregado exitosamente!</p>
    """)

def lista_clientes(req):

    lista = Cliente.objects.all()
    return render(req, "lista_clientes.html", {"lista_clientes": lista})
