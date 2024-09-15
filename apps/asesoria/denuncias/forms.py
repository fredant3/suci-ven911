from django import forms

from .models import Denuncia


class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = [
            "estatus",
            "ente",
            "nombres_d",
            "apellidos_d",
            "cedula_d",
            "telefono",
            "email",
            "direccion_d",
            "nombres_denunciado",
            "apellidos_denunciado",
            "cedula_denunciado",
            "motivo",
            "zona",
            "fecha_denuncia",
            "fecha_incidente",
        ]
