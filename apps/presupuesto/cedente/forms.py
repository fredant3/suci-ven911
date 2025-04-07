from django import forms
from presupuesto.cedente.models import Cedente
from helpers.FormBase import FormBase


class CedenteForm(FormBase):
    class Meta:
        model = Cedente
        fields = (
            "idc",
            "partidac",
            "generalc",
            "espefc",
            "subespefc",
            "denomc",
            "presuacorc",
            "caufechac",
            "dispc",
            "montocc",
            "saldofc",
            "direccionc",
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
            "idc": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el ID",
                }
            ),
            "partidac": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la partida contable",
                }
            ),
            "generalc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el código general",
                    "min": "0",
                }
            ),
            "espefc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el código específico",
                    "min": "0",
                }
            ),
            "subespefc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el subcódigo específico",
                    "min": "0",
                }
            ),
            "denomc": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la denominación",
                }
            ),
            "presuacorc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el presupuesto asignado",
                    "min": "0",
                    "step": "1",
                }
            ),
            "caufechac": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la fecha de compromiso",
                }
            ),
            "dispc": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la disposición",
                }
            ),
            "montocc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el monto comprometido",
                    "min": "0",
                    "step": "1",
                }
            ),
            "saldofc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el saldo final",
                    "min": "0",
                    "step": "1",
                }
            ),
            "direccionc": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la dirección",
                }
            ),
        }
