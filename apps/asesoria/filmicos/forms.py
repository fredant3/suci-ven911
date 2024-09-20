from django import forms
from django.forms.fields import DateTimeInput

from .models import RegistroFilmico


class RegistroFilmicoForm(forms.ModelForm):
    class Meta:
        model = RegistroFilmico
        fields = [
            "estatus",
            "direccion",
            "camara",
            "motivo_solicitud",
            "ente_solicita",
            "fecha_solicitud",
            "fecha_culminacion",
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
            "fecha_solicitud": DateTimeInput(attrs={"type": "date"}),
            "fecha_culminacion": DateTimeInput(attrs={"type": "date"}),
        }
