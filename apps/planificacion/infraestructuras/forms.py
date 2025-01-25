from django import forms
from planificacion.infraestructuras.models import Infraestructura
from helpers.FormBase import FormBase


class InfraestructuraForm(FormBase):
    class Meta:
        model = Infraestructura
        fields = (
            # "estado",
            # "mes",
            # "infraestructura",
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
