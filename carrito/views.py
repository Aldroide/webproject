from django.shortcuts import render, redirect
from .carrito import Carrito
from store.models import Producto

# Create your views here.


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect("store")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.elminar(producto=producto)
    return redirect("store")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar_producto(producto=producto)
    return redirect("store")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar_carrito()
    return redirect("store")
