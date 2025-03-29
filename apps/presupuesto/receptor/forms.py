from django import forms
from presupuesto.receptor.models import Receptor
from helpers.FormBase import FormBase
from helpers.validForm import validate_decimal_number


class ReceptorForm(FormBase):
    class Meta:
        model = Receptor
        fields = (
            "idr",
            "partidar",
            "generalr",
            "espefr",
            "subespefr",
            "denomr",
            "presuacorr",
            "caufechar",
            "dispr",
            "montocr",
            "saldofr",
            "direccionr",
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
            "idr": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el ID",
                }
            ),
            "partidar": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la partida contable",
                }
            ),
            "generalr": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el código general",
                }
            ),
            "espefr": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el código específico",
                }
            ),
            "subespefr": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el subcódigo específico",
                }
            ),
            "denomr": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la denominación",
                }
            ),
            "presuacorr": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el presupuesto asignado",
                }
            ),
            "caufechar": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la fecha de compromiso",
                }
            ),
            "dispr": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la disposición",
                }
            ),
            "montocr": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el monto comprometido",
                }
            ),
            "saldofr": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el saldo final",
                }
            ),
            "direccionr": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la dirección",
                }
            ),
        }

    def clean_presuacorr(self):
        data = self.cleaned_data.get("presuacorr")
        validate_decimal_number(
            str(data), "El presupuesto debe ser un valor positivo con 2 decimales"
        )
        return data

    def clean_montocr(self):
        data = self.cleaned_data.get("montocr")
        validate_decimal_number(
            str(data), "El monto comprometido debe ser un valor con 2 decimales"
        )
        return data

    def clean_saldofr(self):
        data = self.cleaned_data.get("saldofr")
        validate_decimal_number(
            str(data), "El saldo final debe ser un valor con 2 decimales"
        )
        return data
