from django import forms
from django.forms.fields import DateTimeInput
from planificacion.llamadas.models import Llamada
from helpers.FormBase import FormBase


class LlamadaForm(FormBase):
    fecha_denuncia = FormBase.create_date_field("fecha_denuncia")
    fecha_incidente = FormBase.create_date_field("fecha_incidente")

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
