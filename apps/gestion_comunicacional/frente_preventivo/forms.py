from django.forms import TextInput, Textarea, Select
from gestion_comunicacional.frente_preventivo.models import FrentePreventivo
from helpers.FormBase import FormBase

# from django import forms
# from helpers.models import BOOLEAN_CHOICES


class FrentePreventivoForm(FormBase):
    # municipio_priorizado = forms.BooleanField(
    #     initial=False,
    #     required=False,
    #     widget=forms.CheckboxInput(
    #         attrs={"class": "form-check-input", "role": "switch", "value": "False"}
    #     ),
    #     choices=BOOLEAN_CHOICES,
    #     default=True,
    # )

    class Meta:
        model = FrentePreventivo
        fields = [
            "donde_desarrollo",
            "personas_beneficiadas",
            "tipo_actividad",
            "fecha_realizo",
            "observaciones",
        ]
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]
        widgets = {
            "donde_desarrollo": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ejem. vuelvan caras",
                }
            ),
            "personas_beneficiadas": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descripción de la actividad",
                }
            ),
            "tipo_actividad": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "nombre de la población abordada",
                }
            ),
            "observaciones": Textarea(
                attrs={
                    "placeholder": "Ingrese las observaciones",
                }
            ),
        }
