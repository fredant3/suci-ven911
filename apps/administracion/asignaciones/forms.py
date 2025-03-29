from administracion.asignaciones.models import Asignacion
from django import forms
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
            "articulo": forms.Select(attrs={"placeholder": "Seleccione un artículo"}),
            "sede": forms.Select(attrs={"placeholder": "Seleccione una sede"}),
            "departamento": forms.Select(
                attrs={"placeholder": "Seleccione un departamento"}
            ),
            "cantidad": forms.NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "descripcion": forms.TextInput(
                attrs={"placeholder": "Ingrese una descripción"}
            ),
            "observaciones": forms.TextInput(
                attrs={"placeholder": "Ingrese observaciones"}
            ),
        }


class AsignacionUpdateForm(forms.ModelForm):
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
            "articulo": forms.Select(
                attrs={
                    "style": "pointer-events: none;",
                    "readonly": "readonly",
                    "placeholder": "Artículo seleccionado",
                }
            ),
            "sede": forms.Select(attrs={"placeholder": "Seleccione una sede"}),
            "departamento": forms.Select(
                attrs={"placeholder": "Seleccione un departamento"}
            ),
            "cantidad": forms.NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "descripcion": forms.TextInput(
                attrs={"placeholder": "Ingrese una descripción"}
            ),
            "observaciones": forms.TextInput(
                attrs={"placeholder": "Ingrese observaciones"}
            ),
        }
