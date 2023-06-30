from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):
    formulario = FormularioContacto()

    if request.method == "POST":
        formulario = FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get('name')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
            mail = EmailMessage("Mensaje desde app django",
                                f"{nombre} dir {email} envia \n{contenido}",
                                "", ["avilacastro@gmail.com"],
                                reply_to=[email])
            try:
                mail.send()
                return redirect("/contacto/?valido")
            except mail.DoesNotExist:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contact.html",
                  {'miFormulario': formulario})
