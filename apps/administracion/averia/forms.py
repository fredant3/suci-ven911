from administracion.averia.models import Averia
from helpers.FormBase import FormBase
from django import forms


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
        ]
        widgets = {
            "problema": forms.TextInput(attrs={"placeholder": "Ingrese el problema"}),
            "tipo_averia": forms.Select(
                attrs={"placeholder": "Seleccione el tipo de avería"}
            ),
            "departamento": forms.Select(
                attrs={"placeholder": "Seleccione el departamento"}
            ),
            "ubicacion": forms.TextInput(attrs={"placeholder": "Ingrese la ubicación"}),
            "serial": forms.TextInput(attrs={"placeholder": "Ingrese el serial"}),
            "codigo_bn": forms.TextInput(attrs={"placeholder": "Ingrese el código BN"}),
        }
