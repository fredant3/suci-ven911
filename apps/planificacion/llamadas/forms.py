from django import forms
from django.forms.fields import DateTimeInput
from planificacion.llamadas.models import Llamada


class LlamadaForm(forms.ModelForm):
    class Meta:
        model = Llamada
        fields = (
            # "estado",
            # "mes",
            # "informativa",
            # "falsa",
            # "realesno",
            # "realesf",
            # "videop",
        )
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
