from django import forms
from django.forms import ModelForm
from .models import *
from .models import Emergency


class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = [
            "denunciante",
            "telefono_denunciante",
            "id_estado",
            "id_municipio",
            "id_parroquia",
            "id_incidencia",
            "direccion_incidencia",
            "id_organismo",
            "observaciones",
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
            "id_estado": forms.Select(attrs={"class": "form-select mb-3"}),
            "id_municipio": forms.Select(attrs={"class": "form-select mb-3"}),
            "id_parroquia": forms.Select(attrs={"class": "form-select mb-3"}),
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
