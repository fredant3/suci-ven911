from administracion.departamentos.models import Departamento
from helpers.FormBase import FormBase
from helpers.validForm import validate_nombre
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

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        validate_nombre(
            nombre, "El nombre solo puede contener letras, números y espacios."
        )
        return nombre
