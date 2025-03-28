from django import forms
from planificacion.transportes.models import Transporte
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_basic_text,
    validate_cantidad,
    validate_general_text,
)


class TransporteForm(FormBase):
    class Meta:
        model = Transporte
        fields = (
            "estado",
            "mes",
            "transporte",
            "cantidad",
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
            "estado": "Estado del transporte",
            "mes": "Mes de operación",
            "transporte": "Tipo de transporte",
            "cantidad": "Cantidad de unidades",
        }
        widgets = {
            "estado": forms.Select(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Estado del transporte",
                }
            ),
            "mes": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Mes de operación",
                }
            ),
            "transporte": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Tipo de transporte",
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Cantidad de unidades",
                }
            ),
        }

    def clean_estado(self):
        estado = self.cleaned_data.get("estado")
        validate_basic_text(
            estado,
            "El estado solo puede contener letras, números, espacios y los caracteres .,-.",
        )
        return estado

    def clean_mes(self):
        mes = self.cleaned_data.get("mes")
        validate_cantidad(mes, "El mes debe ser un número entre 1 y 12")
        if not (1 <= int(mes) <= 12):
            raise forms.ValidationError("El mes debe estar entre 1 y 12")
        return mes

    def clean_transporte(self):
        transporte = self.cleaned_data.get("transporte")
        validate_general_text(
            transporte,
            "El tipo de transporte solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return transporte

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        validate_cantidad(cantidad, "La cantidad debe ser un número entero positivo.")
        return cantidad
