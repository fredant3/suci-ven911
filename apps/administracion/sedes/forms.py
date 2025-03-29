from helpers.FormBase import FormBase
from administracion.sedes.models import Sede
from django import forms


class SedeForm(FormBase):
    class Meta:
        model = Sede
        fields = (
            "sede",
            "estatus",
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
            "sede": "Sede",
            "estatus": "Estatus",
        }
        widgets = {
            "sede": forms.TextInput(
                attrs={"placeholder": "Ingrese el nombre de la sede"}
            ),
            "estatus": forms.Select(attrs={"placeholder": "Seleccione el estatus"}),
        }
