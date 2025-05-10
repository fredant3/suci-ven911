from django import forms
from presupuesto.cedente.models import Cedente
from helpers.FormBase import FormBase


class CedenteForm(FormBase):
    caufechac = FormBase.create_date_field("caufechac", "Causado a la fecha")

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
            "presuacorc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ej: 50000.00 (solo números positivos)",
                    "min": "0",
                    "step": "0.01",
                }
            ),
            "dispc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ej: 25000.00 (solo números positivos)",
                    "min": "0",
                    "step": "0.01",
                }
            ),
            "montocc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ej: 10000.00 (solo números positivos)",
                    "min": "0",
                    "step": "0.01",
                }
            ),
            "saldofc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ej: 15000.00 (solo números positivos)",
                    "min": "0",
                    "step": "0.01",
                }
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
