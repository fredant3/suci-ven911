from potencia.TipoIncidencia.models import TipoIncidencia
from helpers.FormBase import FormBase


class TipoIncidenciaForm(FormBase):
    class Meta:
        model = Tipo de Incidencia
        fields = [
            "tipo",
        ]
        labels = {
            "tipo": "Tipo de Incidencia",
        }
        widgets = {}
