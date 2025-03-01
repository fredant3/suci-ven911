from django import forms
from planificacion.transportes.models import Transporte
from helpers.FormBase import FormBase


class TransporteForm(FormBase):
    class Meta:
        model = Transporte
        fields = (
            # "estado",
            # "mes",
            # "transporte",
            # "cantidad",
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
