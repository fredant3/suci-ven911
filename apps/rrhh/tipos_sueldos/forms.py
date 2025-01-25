from django import forms

from rrhh.tipos_sueldos.models import TipoSueldo
from helpers.FormBase import FormBase


class TipoSueldoForm(FormBase):
    class Meta:
        model = TipoSueldo
        fields = (
            "tipo",
            "monto",
            "descripcion",
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
