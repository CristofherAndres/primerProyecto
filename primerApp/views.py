from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, 'usuarios/login.html')

def registro(request):
    return render(request, 'usuarios/registro.html')

def perfil(request):
    return render(request, 'usuarios/profile.html')

def primeraVista(request):
    return render(request, 'segunda.html')

def segundaVista(request):
    return render(request, 'tercera.html')

def tablaVista(request):
    return render(request, 'tabla.html')