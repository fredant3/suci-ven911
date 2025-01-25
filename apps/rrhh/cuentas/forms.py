from django import forms

from .models import Cuenta
from helpers.FormBase import FormBase


class CuentaForm(FormBase):
    class Meta:
        model = Cuenta
        fields = (
            "colegio",
            "codigo_titulo",
            "titulo",
            "area_conocimiento",
            "fecha_inicio",
            "fecha_culminacion",
            "enlace_certificado",
            "personal",
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
