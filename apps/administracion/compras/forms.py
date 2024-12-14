from administracion.compras.model import Compra
from django import forms


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ["articulo", "n_orden", "valor_bs"]
        labels = {
            "articulo": "Articulo",
            "n_orden": "N° de orden",
            "valor_bs": "Valor en BS",
        }
        widgets = {}
