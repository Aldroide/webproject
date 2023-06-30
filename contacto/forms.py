from django import forms


class FormularioContacto(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    contenido = forms.CharField(
        label="Contenido", widget=forms.Textarea)
