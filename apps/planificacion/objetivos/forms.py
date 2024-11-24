from django import forms
from django.forms.fields import DateTimeInput
from planificacion.objetivos.models import Objetivo


class ObjetivoForm(forms.ModelForm):
    class Meta:
        model = Objetivo
        fields = (
            "fechai",
            "fechaf",
            "objetiv",
            "meta",
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
            "fechai": DateTimeInput(attrs={"type": "date"}),
            "fechaf": DateTimeInput(attrs={"type": "date"}),
        }
