from administracion.departamentos.models import Departamento
from django import forms


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = [
            "nombre",
        ]
        labels = {
            "nombre": "Nombre",
        }
        widgets = {}
