from administracion.departamentos.models import Departamento
from helpers.FormBase import FormBase


class DepartamentoForm(FormBase):
    class Meta:
        model = Departamento
        fields = [
            "nombre",
        ]
        labels = {
            "nombre": "Nombre",
        }
        widgets = {}
