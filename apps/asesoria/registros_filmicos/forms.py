from django import forms

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
