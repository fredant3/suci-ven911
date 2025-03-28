from django import forms
from rrhh.empleados.models import Empleado
from rrhh.dotaciones.models import Dotacion
from helpers.FormBase import FormBase
from helpers.validForm import validate_ente


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
        labels = {
            "empleado": "Empleado",
            "camisa": "Talla de Camisa",
            "pantalon": "Talla de Pantalón",
            "zapato": "Talla de Zapato",
        }
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

    def clean_camisa(self):
        data = self.cleaned_data.get("camisa")
        validate_ente(
            data,
            "La talla de camisa solo puede contener letras, números y los caracteres -/",
        )
        return data

    def clean_pantalon(self):
        data = self.cleaned_data.get("pantalon")
        validate_ente(
            data,
            "La talla de pantalón solo puede contener letras, números y los caracteres -/",
        )
        return data

    def clean_zapato(self):
        data = self.cleaned_data.get("zapato")
        validate_ente(
            data,
            "La talla de zapato solo puede contener letras, números y los caracteres -/.",
        )
        return data

    def clean_empleado(self):
        empleado = self.cleaned_data.get("empleado")
        if not Empleado.objects.filter(id=empleado.id).exists():
            raise forms.ValidationError("Seleccione un empleado válido")
        return empleado
