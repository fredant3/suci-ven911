from django import forms
from presupuesto.models import Accion

from django.forms.fields import DateTimeInput
from helpers.FormBase import FormBase


class AccionForm(FormBase):
    fecha_inicio = FormBase.create_date_field("fecha_inicio")
    fecha_culminacion = FormBase.create_date_field("fecha_culminacion")

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
