from administracion.departamentos.models import Departamento
from helpers.FormBase import FormBase
from django import forms


class DepartamentoForm(FormBase):
    class Meta:
        model = Departamento
        fields = [
            "nombre",
        ]
        labels = {
            "nombre": "Nombre",
        }
        widgets = {
            "nombre": forms.TextInput(
                attrs={"placeholder": "Ingrese el nombre del departamento"}
            ),
        }
