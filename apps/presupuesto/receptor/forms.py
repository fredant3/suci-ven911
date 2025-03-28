from django import forms
from presupuesto.receptor.models import Receptor
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_codigo_bn,
    validate_cantidad,
    validate_ente,
    validate_valor_bs,
    validate_direccion,
)


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
        labels = {
            "idr": "Identificador Receptor",
            "partidar": "Partida Contable",
            "denomr": "Denominación",
            "presuacorr": "Presupuesto Asignado",
            "montocr": "Monto Comprometido",
            "saldofr": "Saldo Final",
        }
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

    def clean_idr(self):
        data = self.cleaned_data.get("idr")
        validate_codigo_bn(data, "El ID debe contener solo letras, números y guiones")
        return data

    def clean_partidar(self):
        data = self.cleaned_data.get("partidar")
        validate_codigo_bn(
            data, "La partida contable solo permite letras, números y guiones"
        )
        return data

    def clean_generalr(self):
        data = self.cleaned_data.get("generalr")
        validate_cantidad(data, "El código general debe ser un número entero positivo")
        return data

    def clean_espefr(self):
        data = self.cleaned_data.get("espefr")
        validate_cantidad(
            data, "El código específico debe ser un número entero positivo"
        )
        return data

    def clean_subespefr(self):
        data = self.cleaned_data.get("subespefr")
        validate_cantidad(
            data, "El subcódigo específico debe ser un número entero positivo"
        )
        return data

    def clean_denomr(self):
        data = self.cleaned_data.get("denomr")
        validate_ente(
            data, "La denominación solo permite letras, números y caracteres .,-!?()"
        )
        return data

    def clean_presuacorr(self):
        data = self.cleaned_data.get("presuacorr")
        validate_valor_bs(
            str(data), "El presupuesto debe ser un valor positivo con 2 decimales"
        )
        return data

    def clean_caufechar(self):
        data = self.cleaned_data.get("caufechar")
        validate_ente(data, "Formato de fecha no válido. Use caracteres permitidos")
        return data

    def clean_dispr(self):
        data = self.cleaned_data.get("dispr")
        validate_ente(
            data, "Formato de disposición no válido. Use caracteres permitidos"
        )
        return data

    def clean_montocr(self):
        data = self.cleaned_data.get("montocr")
        validate_valor_bs(
            str(data), "El monto comprometido debe ser un valor con 2 decimales"
        )
        return data

    def clean_saldofr(self):
        data = self.cleaned_data.get("saldofr")
        validate_valor_bs(str(data), "El saldo final debe ser un valor con 2 decimales")
        return data

    def clean_direccionr(self):
        data = self.cleaned_data.get("direccionr")
        validate_direccion(data, "La dirección contiene caracteres no permitidos")
        return data
