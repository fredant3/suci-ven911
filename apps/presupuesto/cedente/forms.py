from django import forms
from presupuesto.cedente.models import Cedente
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_codigo_bn,
    validate_cantidad,
    validate_ente,
    validate_valor_bs,
    validate_direccion,
)


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
        labels = {
            "idc": "Identificador Cedente",
            "partidac": "Partida Contable",
            "denomc": "Denominación",
            "presuacorc": "Presupuesto Asignado",
            "montocc": "Monto Comprometido",
            "saldofc": "Saldo Final",
        }
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
                }
            ),
            "espefc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el código específico",
                }
            ),
            "subespefc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el subcódigo específico",
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
                }
            ),
            "saldofc": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el saldo final",
                }
            ),
            "direccionc": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la dirección",
                }
            ),
        }

    def clean_idc(self):
        data = self.cleaned_data.get("idc")
        validate_codigo_bn(data, "El ID debe contener solo letras, números y guiones")
        return data

    def clean_partidac(self):
        data = self.cleaned_data.get("partidac")
        validate_codigo_bn(
            data, "La partida contable solo permite letras, números y guiones"
        )
        return data

    def clean_generalc(self):
        data = self.cleaned_data.get("generalc")
        validate_cantidad(data, "El código general debe ser un número entero positivo")
        return data

    def clean_espefc(self):
        data = self.cleaned_data.get("espefc")
        validate_cantidad(
            data, "El código específico debe ser un número entero positivo"
        )
        return data

    def clean_subespefc(self):
        data = self.cleaned_data.get("subespefc")
        validate_cantidad(
            data, "El subcódigo específico debe ser un número entero positivo"
        )
        return data

    def clean_denomc(self):
        data = self.cleaned_data.get("denomc")
        validate_ente(
            data, "La denominación solo permite letras, números y caracteres .,-!?()"
        )
        return data

    def clean_presuacorc(self):
        data = self.cleaned_data.get("presuacorc")
        validate_valor_bs(
            str(data), "El presupuesto debe ser un valor positivo con 2 decimales"
        )
        return data

    def clean_caufechac(self):
        data = self.cleaned_data.get("caufechac")
        validate_ente(data, "Formato de fecha no válido. Use caracteres permitidos")
        return data

    def clean_dispc(self):
        data = self.cleaned_data.get("dispc")
        validate_ente(
            data, "Formato de disposición no válido. Use caracteres permitidos"
        )
        return data

    def clean_montocc(self):
        data = self.cleaned_data.get("montocc")
        validate_valor_bs(
            str(data), "El monto comprometido debe ser un valor con 2 decimales"
        )
        return data

    def clean_saldofc(self):
        data = self.cleaned_data.get("saldofc")
        validate_valor_bs(str(data), "El saldo final debe ser un valor con 2 decimales")
        return data

    def clean_direccionc(self):
        data = self.cleaned_data.get("direccionc")
        validate_direccion(data, "La dirección contiene caracteres no permitidos")
        return data
