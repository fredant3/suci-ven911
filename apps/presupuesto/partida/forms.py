from django import forms
from presupuesto.partida.models import Partida
from helpers.FormBase import FormBase


class PartidaForm(FormBase):

    class Meta:
        model = Partida
        fields = (
            "codigo",
            "titulo",
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
            "codigo": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese codigo",
                }
            ),
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el titulo",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data
