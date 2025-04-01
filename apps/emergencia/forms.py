from django import forms
from emergencia.models import Emergencia
from helpers.FormBase import FormBase


class EmergenciaForm(FormBase):
    class Meta:
        model = Emergencia
        fields = [
            "denunciante",
            "telefono_denunciante",
            "estado",
            "municipio",
            "parroquia",
            "incidencia",
            "organismo",
            "direccion_incidencia",
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
            "denunciante": forms.TextInput(
                attrs={
                    "placeholder": "Ejem. George Harris",
                }
            ),
            "telefono_denunciante": forms.TextInput(
                attrs={"placeholder": "Ejem. 04125248935"}
            ),
            "direccion_incidencia": forms.Textarea(
                attrs={
                    "placeholder": "Ejem. Urbanización Lomas de Urdaneta",
                }
            ),
            "telefono_cuadrante_paz": forms.TextInput(
                attrs={"placeholder": "Ejem. 04125248935"}
            ),
            "observaciones": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese las observaciones",
                }
            ),
        }
