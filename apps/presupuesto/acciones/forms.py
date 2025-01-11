from django import forms
from presupuesto.models import Accion

from django.forms.fields import DateTimeInput


class AccionForm(forms.ModelForm):
    class Meta:
        model = Accion
        fields = (
            "proyecto",
            "fecha_inicio",
            "fecha_culminacion",
            "situacion_presupuestaria",
            "monto",
            "responsable_gerente",
            "responsable_tecnico",
            "responsable_registrador",
            "responsable_administrativo",
            "estatus",
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
            "fecha_inicio": DateTimeInput(attrs={"type": "date"}),
            "fecha_culminacion": DateTimeInput(attrs={"type": "date"}),
        }
