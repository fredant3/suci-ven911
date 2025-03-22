from potencia.tipoIncidencia.models import TipoIncidencia
from helpers.FormBase import FormBase


class TipoIncidenciaForm(FormBase):
    class Meta:
        model = TipoIncidencia
        fields = [
            "tipo",
        ]
        labels = {
            "tipo": "Tipo de Incidencia",
        }
        widgets = {}
