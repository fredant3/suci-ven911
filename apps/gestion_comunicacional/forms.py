from django.forms import TextInput, Textarea
from gestion_comunicacional.models import GestionComunicacional
from helpers.FormBase import FormBase
from django import forms
from helpers.models import BOOLEAN_CHOICES


class GestionComunicacionalForm(FormBase):
    municipio_priorizado = forms.BooleanField(
        initial=False,
        required=False,
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input", "role": "switch", "value": "False"}
        ),
        choices=BOOLEAN_CHOICES,
        default=BOOLEAN_CHOICES[1],
    )

    class Meta:
        model = GestionComunicacional
        fields = [
            "nombre actividad",
            "actividad realizada",
            "descripcion actividad",
            "actividad preventiva",
            "municipio",
            "parroquia",
            "estrategias metodologicas",
            "ambito accion",
            "poblacion abordada",
            "municipio priorizado",
            "equipo social",
            "cedula",
            "ambito_accion",
            "poblacion abordada",
            "telefono_cuadrante_paz",
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
            "nombre de la actividad": TextInput(
                attrs={
                    "placeholder": "Ejem. Vuelvan caras",
                }
            ),
            "poblacion abordada": Textarea(
                attrs={
                    "placeholder": "Ejem. 5 de Julio",
                }
            ),
            "observaciones": Textarea(
                attrs={
                    "placeholder": "Ingrese las observaciones",
                }
            ),
        }
