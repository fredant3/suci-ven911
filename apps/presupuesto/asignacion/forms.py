from django import forms

from presupuesto.asignacion.models import Asignacion
from helpers.FormBase import FormBase


class AsignacionForm(FormBase):
    class Meta:
        model = Asignacion
        fields = ("departamento", "presupuesto", "objetivo", "numero_partida")
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
