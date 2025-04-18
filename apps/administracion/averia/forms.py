from administracion.averia.models import Averia
from helpers.FormBase import FormBase
from django.forms import TextInput


class AveriaForm(FormBase):
    class Meta:
        model = Averia
        fields = [
            "problema",
            "tipo_averia",
            "departamento",
            "ubicacion",
            "serial",
            "codigo_bn",
            "observaciones",
        ]
        widgets = {
            "problema": TextInput(
                attrs={"placeholder": "Describa el problema (mínimo 9 caracteres)"}
            ),
            "ubicacion": TextInput(
                attrs={
                    "placeholder": "Ingrese la ubicación exacta (mínimo 9 caracteres)"
                }
            ),
            "serial": TextInput(
                attrs={"placeholder": "Ingrese el número de serie (6-30 caracteres)"}
            ),
            "codigo_bn": TextInput(
                attrs={"placeholder": "Ingrese el código BN (6-30 caracteres)"}
            ),
            "observaciones": TextInput(
                attrs={"placeholder": "Ingrese observaciones (mínimo 10 caracteres)"}
            ),
        }
