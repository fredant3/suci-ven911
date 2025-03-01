from django import forms

from .models import Contrato
from helpers.FormBase import FormBase


class ContratoForm(FormBase):
    class Meta:
        model = Contrato
        fields = (
            "tipo",
            "comision_servicio",
            "pnb",
            "departamento",
            "tipo_personal",
            "cargo",
            "sede",
            "fecha_ingreso_911",
            "fecha_ingreso_apn",
            "fasmij",
            "fecha_ingreso",
            "fecha_culminacion",
            "empleado",
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
