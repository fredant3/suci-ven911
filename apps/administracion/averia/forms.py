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
        ]
        widgets = {
            "problema": TextInput(attrs={"placeholder": "Ingrese el problema"}),
            "ubicacion": TextInput(attrs={"placeholder": "Ingrese la ubicación"}),
            "serial": TextInput(attrs={"placeholder": "Ingrese el serial"}),
            "codigo_bn": TextInput(attrs={"placeholder": "Ingrese el código BN"}),
        }
