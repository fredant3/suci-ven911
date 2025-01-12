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
