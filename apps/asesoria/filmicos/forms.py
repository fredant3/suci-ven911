from asesoria.filmicos.models import RegistroFilmico
from helpers.FormBase import FormBase
from django.forms.fields import DateTimeInput
from helpers.validForm import (
    validate_direccion,
    validate_general_text,
    validate_general_text_solicitud,
    validate_general_text_solicita,
)
from django import forms


class RegistroFilmicoForm(FormBase):
    fecha_solicitud = FormBase.create_date_field("fecha_solicitud")
    fecha_culminacion = FormBase.create_date_field("fecha_culminacion")

    class Meta:
        model = RegistroFilmico
        fields = [
            "estatus",
            "direccion",
            "camara",
            "motivo_solicitud",
            "ente_solicita",
            "fecha_solicitud",
            "fecha_culminacion",
        ]
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
        widgets = {
            "estatus": forms.Select(attrs={"placeholder": "Seleccione el estatus"}),
            "direccion": forms.TextInput(attrs={"placeholder": "Ingrese la dirección"}),
            "camara": forms.TextInput(attrs={"placeholder": "Ingrese la cámara"}),
            "motivo_solicitud": forms.TextInput(
                attrs={"placeholder": "Ingrese el motivo de la solicitud"}
            ),
            "ente_solicita": forms.TextInput(
                attrs={"placeholder": "Ingrese el ente que solicita"}
            ),
        }

    def clean_direccion(self):
        direccion = self.cleaned_data.get("direccion")
        validate_direccion(
            direccion,
            "La dirección solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return direccion

    def clean_camara(self):
        camara = self.cleaned_data.get("camara")
        validate_general_text(
            camara,
            "El campo cámara solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return camara

    def clean_motivo_solicitud(self):
        motivo_solicitud = self.cleaned_data.get("motivo_solicitud")
        validate_general_text_solicitud(
            motivo_solicitud,
            "El motivo de la solicitud solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return motivo_solicitud

    def clean_ente_solicita(self):
        ente_solicita = self.cleaned_data.get("ente_solicita")
        validate_general_text_solicita(
            ente_solicita,
            "El ente que solicita solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return ente_solicita
