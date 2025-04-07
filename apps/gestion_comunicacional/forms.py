from django.forms import TextInput, Textarea
from gestion_comunicacional.models import GestionComunicacional
from helpers.FormBase import FormBase

# from django import forms
# from helpers.models import BOOLEAN_CHOICES


class GestionComunicacionalForm(FormBase):
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
        model = GestionComunicacional
        fields = [
            "nombre_actividad",
            "actividad_realizada",
            "descripcion_actividad",
            "actividad_preventiva",
            "municipio",
            "parroquia",
            "estrategias_metodologicas",
            "ambito_accion",
            "poblacion_abordada",
            "municipio_priorizado",
            "equipo_social",
            "cedula",
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
