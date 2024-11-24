from administracion.averia.models import Averia
from django import forms


class AveriaForm(forms.ModelForm):
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
        labels = {
            "problema": "Problema",
            "tipo_averia": "Tipo de avería",
            "departamento": "Departamento",
            "ubicacion": "Ubicación",
            "serial": "Serial",
            "codigo_bn": "Código BN",
        }
        widgets = {}
