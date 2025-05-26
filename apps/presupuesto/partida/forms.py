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
                    "placeholder": "Formato: 000-00-00-00 (4 grupos de números separados por espacios o guiones)",
                }
            ),
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese título (mínimo 6 caracteres)",
                }
            ),
        }
