from django import forms
from presupuesto.partida.models import Partida
from helpers.FormBase import FormBase


class PartidaForm(FormBase):
    class Meta:
        model = Partida
        fields = ("codigo", "titulo")
        widgets = {
            "codigo": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese código (mínimo 6 caracteres)",
                }
            ),
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese título (mínimo 6 caracteres)",
                }
            ),
        }
