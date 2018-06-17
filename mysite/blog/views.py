from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return HttpResponse("Bem Vindo ao Blog!!")

def index(request):
    return render(request, 'blog/index.html', {})

def perfil(request):
    return render(request, 'blog/perfil.html', {})
