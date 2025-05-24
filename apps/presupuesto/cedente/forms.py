from django import forms
from presupuesto.cedente.models import Cedente
from helpers.FormBase import FormBase


class CedenteForm(FormBase):
    caufechac = FormBase.create_date_field("caufechac", "Causado a la fecha")

    class Meta:
        model = Cedente
        fields = (
            "partida",
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
                    "placeholder": "Ej: CED-001 (mín. 4 caracteres)",
                    "maxlength": "100",
                }
            ),
            "partidac": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ej: PC-2023-001 (mín. 4 caracteres)",
                    "maxlength": "64",
                }
            ),
            "generalc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Número entre 1 y 255",
                    "min": "1",
                }
            ),
            "espefc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Número entre 1 y 255",
                    "min": "1",
                }
            ),
            "subespefc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Número entre 1 y 255",
                    "min": "1",
                }
            ),
            "denomc": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ej: Proyecto de Infraestructura (mín. 4 caracteres)",
                    "maxlength": "255",
                }
            ),
            "presuacorc": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "dispc": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "montocc": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "saldofc": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "direccionc": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ej: Av. Principal, Edificio Municipal",
                    "maxlength": "255",
                }
            ),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
