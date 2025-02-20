from django import forms

from rrhh.cuentas.models import Cuenta
from helpers.FormBase import FormBase


class CuentaForm(FormBase):
    class Meta:
        model = Cuenta
        fields = (
            "banco",
            "tipo",
            "pago_movil",
            "telefono",
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
