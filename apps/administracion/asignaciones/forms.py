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
            "articulo": forms.Select(
                attrs={"class": "form-select", "placeholder": "Seleccione un artículo"}
            ),
            "sede": forms.Select(
                attrs={"class": "form-select", "placeholder": "Seleccione una sede"}
            ),
            "departamento": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Seleccione un departamento",
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese la cantidad",
                    "min": "1",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese una descripción",
                    "rows": "3",
                }
            ),
            "observaciones": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese observaciones",
                    "rows": "3",
                }
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
                    "class": "form-select",
                    "style": "pointer-events: none; background-color: #e9ecef;",
                    "readonly": "readonly",
                    "placeholder": "Artículo seleccionado",
                }
            ),
            "sede": forms.Select(
                attrs={"class": "form-select", "placeholder": "Seleccione una sede"}
            ),
            "departamento": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Seleccione un departamento",
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese la cantidad",
                    "min": "1",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese una descripción",
                    "rows": "3",
                }
            ),
            "observaciones": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese observaciones",
                    "rows": "3",
                }
            ),
        }
