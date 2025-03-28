from django import forms
from planificacion.infraestructuras.models import Infraestructura
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_basic_text,
    validate_cantidad,
    validate_general_text,
)


class InfraestructuraForm(FormBase):
    class Meta:
        model = Infraestructura
        fields = (
            "estado",
            "mes",
            "infraestructura",
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
            "estado": "Estado de la infraestructura",
            "mes": "Mes programado",
            "infraestructura": "Nombre de la infraestructura",
            "cantidad": "Cantidad estimada",
        }
        widgets = {
            "estado": forms.TextInput(
                attrs={
                    "placeholder": "Estado de la infraestructura",
                }
            ),
            "mes": forms.TextInput(
                attrs={
                    "placeholder": "Mes programado",
                }
            ),
            "infraestructura": forms.TextInput(
                attrs={
                    "placeholder": "Nombre de la infraestructura",
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={
                    "placeholder": "Cantidad estimada",
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
        validate_cantidad(mes, "El mes debe ser un número entero entre 1 y 12.")
        if int(mes) < 1 or int(mes) > 12:
            raise forms.ValidationError("El mes debe estar entre 1 y 12")
        return mes

    def clean_infraestructura(self):
        infraestructura = self.cleaned_data.get("infraestructura")
        validate_general_text(
            infraestructura,
            "El nombre debe contener letras, números, espacios y los caracteres .,-!?().",
        )
        return infraestructura

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        validate_cantidad(cantidad, "La cantidad debe ser un número entero positivo.")
        return cantidad
