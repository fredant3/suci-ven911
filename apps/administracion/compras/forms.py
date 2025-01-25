from administracion.compras.model import Compra
from helpers.FormBase import FormBase


class CompraForm(FormBase):
    class Meta:
        model = Compra
        fields = ["articulo", "n_orden", "valor_bs"]
        labels = {
            "articulo": "Articulo",
            "n_orden": "N° de orden",
            "valor_bs": "Valor en BS",
        }
        widgets = {}
