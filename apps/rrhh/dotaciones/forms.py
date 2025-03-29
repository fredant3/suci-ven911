from django import forms
from rrhh.dotaciones.models import Dotacion
from helpers.FormBase import FormBase


class DotacionForm(FormBase):
    class Meta:
        model = Dotacion
        fields = (
            "camisa",
            "pantalon",
            "zapato",
            "empleado",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
        widgets = {
            "camisa": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: M, L, XL o 40-42"}
            ),
            "pantalon": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: 32, 34, 36 o Mediano",
                }
            ),
            "zapato": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: 40, 41, 42 o 8.5US"}
            ),
            "empleado": forms.Select(
                attrs={"class": "form-control", "placeholder": "Seleccione un empleado"}
            ),
        }
