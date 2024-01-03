from django import forms
from django.core.exceptions import ValidationError

class AsociateForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    edad = forms.IntegerField(label="Edad", required=True)
    mail = forms.EmailField(label="Mail de contacto", required=True)
    celular = forms.IntegerField(label="Celular de contacto", required=True)

    def clean_edad(self):
        if self.cleaned_data["edad"] < 18:
            raise ValidationError("Servicio válido para mayores de edad solamente")
        return self.cleaned_data["edad"]
    
    def clean(self):
        # SIMULACIÓN DE BÚSQUEDA EN LA BASE DE DATOS
        if self.cleaned_data["nombre"] == "Eugenia" and self.cleaned_data["apellido"] == "De Palma":
            raise ValidationError("Este nombre ya está registrado")
        # Si el usuario no existe, se da de alta
        return self.cleaned_data
