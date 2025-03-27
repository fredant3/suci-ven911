from organizacion.reglamentos.models import Reglamento
from helpers.FormBase import FormBase
from django import forms
from helpers.validForm import (
    validate_ente,
    validate_codigo_bn,
    validate_condicion,
)


class ReglamentoForm(FormBase):
    date = FormBase.create_date_field("date", title="Fecha de publicación")

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields.pop("file")

    class Meta:
        model = Reglamento
        fields = [
            "name",
            "file",
            "date",
            "progre",
            "estado",
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
            "name": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del reglamento",
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

    def clean_name(self):
        name = self.cleaned_data.get("name")
        validate_ente(
            name,
            "El nombre solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return name
