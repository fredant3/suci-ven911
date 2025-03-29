from django import forms
from presupuesto.asignacion.models import Asignacion
from helpers.FormBase import FormBase
from helpers.validForm import validate_decimal_number


class AsignacionForm(FormBase):
    class Meta:
        model = Asignacion
        fields = ("departamento", "presupuesto", "objetivo", "numero_partida")
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
            "departamento": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del departamento",
                }
            ),
            "presupuesto": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el presupuesto",
                }
            ),
            "objetivo": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el objetivo",
                }
            ),
            "numero_partida": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el número de partida",
                }
            ),
        }

    def clean_presupuesto(self):
        presupuesto = self.cleaned_data.get("presupuesto")
        validate_decimal_number(
            str(presupuesto),
            "El presupuesto debe ser un valor positivo con hasta dos decimales.",
        )
        return presupuesto
