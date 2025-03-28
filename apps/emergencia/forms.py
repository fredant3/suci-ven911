from django import forms
from emergencia.models import Emergencia
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_nombre,
    validate_telefono,
    validate_direccion,
    validate_basic_text,
)


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

    def clean_denunciante(self):
        denunciante = self.cleaned_data.get("denunciante")
        validate_nombre(
            denunciante,
            "El nombre del denunciante solo puede contener letras y espacios.",
        )
        return denunciante

    def clean_telefono_denunciante(self):
        telefono_denunciante = self.cleaned_data.get("telefono_denunciante")
        validate_telefono(
            telefono_denunciante,
            "El teléfono del denunciante solo puede contener números y guiones.",
        )
        return telefono_denunciante

    def clean_direccion_incidencia(self):
        direccion_incidencia = self.cleaned_data.get("direccion_incidencia")
        validate_direccion(
            direccion_incidencia,
            "La dirección de la incidencia solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return direccion_incidencia

    def clean_telefono_cuadrante_paz(self):
        telefono_cuadrante_paz = self.cleaned_data.get("telefono_cuadrante_paz")
        validate_telefono(
            telefono_cuadrante_paz,
            "El teléfono del cuadrante de paz solo puede contener números y guiones.",
        )
        return telefono_cuadrante_paz

    def clean_observaciones(self):
        observaciones = self.cleaned_data.get("observaciones")
        validate_basic_text(
            observaciones,
            "Las observaciones solo pueden contener letras, números, espacios y los caracteres .,-!?().",
        )
        return observaciones
