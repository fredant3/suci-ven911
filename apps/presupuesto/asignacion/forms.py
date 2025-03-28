from django import forms
from presupuesto.asignacion.models import Asignacion
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_sede,
    validate_decimal_number,
    validate_general_text,
    validate_codigo_bn,
)


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
        labels = {"numero_partida": "Número de partida presupuestaria"}
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

    def clean_departamento(self):
        departamento = self.cleaned_data.get("departamento")
        validate_sede(
            departamento,
            "El departamento solo puede contener letras, números y espacios.",
        )
        return departamento

    def clean_presupuesto(self):
        presupuesto = self.cleaned_data.get("presupuesto")
        validate_decimal_number(
            str(presupuesto),
            "El presupuesto debe ser un valor positivo con hasta dos decimales.",
        )
        return presupuesto

    def clean_objetivo(self):
        objetivo = self.cleaned_data.get("objetivo")
        validate_general_text(
            objetivo,
            "El objetivo solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return objetivo

    def clean_numero_partida(self):
        partida = self.cleaned_data.get("numero_partida")
        validate_codigo_bn(
            partida,
            "El número de partida solo puede contener letras, números y guiones.",
        )
        return partida
