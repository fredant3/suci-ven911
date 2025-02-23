from django import forms
from rrhh.cuentas.models import Cuenta
from rrhh.empleados.models import Empleado
from helpers.FormBase import FormBase


class CuentaForm(FormBase):
    pago_movil = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"value": "False"}),
    )

    class Meta:
        model = Cuenta
        fields = (
            "banco",
            "tipo",
            "numero_cuenta",
            "pago_movil",
            "telefono",
            "empleado",
        )
        labels = {
            "empleado": "Empleado",
        }
        widgets = {}
