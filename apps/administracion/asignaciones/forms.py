from administracion.asignaciones.models import Asignacion
from django.forms import TextInput, NumberInput
from helpers.FormBase import FormBase


class AsignacionForm(FormBase):
    class Meta:
        model = Asignacion
        fields = [
            "articulo",
            "sede",
            "departamento",
            "cantidad",
            "descripcion",
            "observaciones",
        ]
        labels = {
            "articulo": "Artículo",
            "sede": "Sede",
            "departamento": "Departamento",
            "cantidad": "Cantidad",
            "descripcion": "Descripción",
            "observaciones": "Observaciones",
        }
        widgets = {
            "cantidad": NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "descripcion": TextInput(attrs={"placeholder": "Ingrese una descripción"}),
            "observaciones": TextInput(attrs={"placeholder": "Ingrese observaciones"}),
        }


class AsignacionUpdateForm(FormBase):
    class Meta:
        model = Asignacion
        fields = [
            "articulo",
            "sede",
            "departamento",
            "cantidad",
            "descripcion",
            "observaciones",
        ]
        labels = {
            "articulo": "Artículo (Solo lectura)",
            "sede": "Sede",
            "departamento": "Departamento",
            "cantidad": "Cantidad",
            "descripcion": "Descripción",
            "observaciones": "Observaciones",
        }
        widgets = {
            "cantidad": NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "descripcion": TextInput(attrs={"placeholder": "Ingrese una descripción"}),
            "observaciones": TextInput(attrs={"placeholder": "Ingrese observaciones"}),
        }
