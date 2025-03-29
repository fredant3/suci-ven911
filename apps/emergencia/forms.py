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
                    "class": "form-control mb-3",
                    "placeholder": "Ejem. George Harris",
                }
            ),
            "telefono_denunciante": forms.TextInput(
                attrs={"class": "form-control mb-3", "placeholder": "Ejem. 04125248935"}
            ),
            "estado": forms.Select(
                attrs={
                    "class": "form-select mb-3",
                    "placeholder": "Seleccione el estado",
                }
            ),
            "municipio": forms.Select(
                attrs={
                    "class": "form-select mb-3",
                    "placeholder": "Seleccione el municipio",
                }
            ),
            "parroquia": forms.Select(
                attrs={
                    "class": "form-select mb-3",
                    "placeholder": "Seleccione la parroquia",
                }
            ),
            "incidencia": forms.Select(
                attrs={
                    "class": "form-select mb-3",
                    "placeholder": "Seleccione la incidencia",
                }
            ),
            "organismo": forms.Select(
                attrs={
                    "class": "form-select mb-3",
                    "placeholder": "Seleccione el organismo",
                }
            ),
            "direccion_incidencia": forms.Textarea(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ejem. Urbanización Lomas de Urdaneta",
                }
            ),
            "telefono_cuadrante_paz": forms.TextInput(
                attrs={"class": "form-control mb-3", "placeholder": "Ejem. 04125248935"}
            ),
            "observaciones": forms.Textarea(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese las observaciones",
                }
            ),
        }
