from administracion.compras.model import Compra
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_n_orden,
    validate_valor_bs,
)
from django import forms


class CompraForm(FormBase):
    class Meta:
        model = Compra
        fields = ["articulo", "n_orden", "valor_bs"]
        labels = {
            "articulo": "Artículo",
            "n_orden": "N° de orden",
            "valor_bs": "Valor en BS",
        }
        widgets = {
            "articulo": forms.Select(attrs={"placeholder": "Seleccione un artículo"}),
            "n_orden": forms.TextInput(
                attrs={"placeholder": "Ingrese el número de orden"}
            ),
            "valor_bs": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese el valor en BS con la estrucura Bs. 0,00"
                }
            ),
        }

    def clean_n_orden(self):
        n_orden = self.cleaned_data.get("n_orden")
        validate_n_orden(
            n_orden, "El número de orden debe contener solo números y guiones."
        )
        return n_orden

    def clean_valor_bs(self):
        valor_bs = self.cleaned_data.get("valor_bs")
        validate_valor_bs(valor_bs, "El valor en BS debe ser un número positivo.")
        return valor_bs
