from django import forms
from organizacion.normativas.models import Normativa
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_nombre,
)


class NormativaForm(FormBase):
    date = FormBase.create_date_field("date", "Fecha de publicación")

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields.pop("file")

    class Meta:
        model = Normativa
        fields = [
            "name",
            "file",
            "date",
            "progre",
            "estado",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre de la normativa",
                }
            ),
            "file": forms.FileInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Seleccione el archivo",
                }
            ),
            "progre": forms.Select(
                attrs={
                    "class": "form-select mb-3",
                    "placeholder": "Seleccione el progreso",
                }
            ),
            "estado": forms.Select(
                attrs={
                    "class": "form-select mb-3",
                    "placeholder": "Seleccione el estado",
                }
            ),
        }
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        validate_nombre(
            name,
            "El nombre de la normativa solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return name
