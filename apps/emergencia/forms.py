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
            "id_incidencia",
            "direccion_incidencia",
            "id_organismo",
            "observaciones",
            "datecompleted",
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
            "estado": forms.Select(attrs={"class": "form-select mb-3"}),
            "municipio": forms.Select(attrs={"class": "form-select mb-3"}),
            "parroquia": forms.Select(attrs={"class": "form-select mb-3"}),
            "id_incidencia": forms.Select(attrs={"class": "form-select mb-3"}),
            "direccion_incidencia": forms.Textarea(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ejem. Urbanización Lomas de Urdaneta",
                }
            ),
            "id_organismo": forms.Select(attrs={"class": "form-select mb-3"}),
            "observaciones": forms.Textarea(attrs={"class": "form-control mb-3"}),
        }
