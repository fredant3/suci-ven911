from administracion.compras.model import Compra
from helpers.FormBase import FormBase
from helpers.validForm import validate_decimal_number
from django import forms


class CompraForm(FormBase):
    class Meta:
        model = Compra
        fields = ["articulo", "n_orden", "valor_bs"]
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

    def clean_valor_bs(self):
        valor_bs = self.cleaned_data.get("valor_bs")
        validate_decimal_number(valor_bs, "El valor en BS debe ser un número positivo.")
        return valor_bs
