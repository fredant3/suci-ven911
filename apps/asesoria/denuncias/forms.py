from django import forms
from django.forms.fields import DateTimeInput

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
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
        widgets = {
            "fecha_denuncia": DateTimeInput(attrs={"type": "date"}),
            "fecha_incidente": DateTimeInput(attrs={"type": "date"}),
        }
