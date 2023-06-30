from django.shortcuts import render
from carrito.carrito import Carrito


# Create your views here.


def home(request):
    carrito = Carrito(request)
    return render(request, "Webprojectapp/home.html")
