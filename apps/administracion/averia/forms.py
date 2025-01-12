from administracion.averia.models import Averia
from helpers.FormBase import FormBase


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
        labels = {
            "problema": "Problema",
            "tipo_averia": "Tipo de avería",
            "departamento": "Departamento",
            "ubicacion": "Ubicación",
            "serial": "Serial",
            "codigo_bn": "Código BN",
        }
        widgets = {}
