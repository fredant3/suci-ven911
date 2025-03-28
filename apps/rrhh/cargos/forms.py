from django import forms
from rrhh.cargos.models import Cargo
from helpers.FormBase import FormBase
from helpers.validForm import validate_ente, validate_condicion


class CargoForm(FormBase):
    class Meta:
        model = Cargo
        fields = (
            "cargo",
            "estatus",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
        labels = {"cargo": "Nombre del Cargo", "estatus": "Estado del Cargo"}
        widgets = {
            "cargo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del Cargo"}
            ),
            "estatus": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Estado del Cargo"}
            ),
        }

    def clean_cargo(self):
        cargo = self.cleaned_data.get("cargo")
        validate_ente(
            cargo,
            "El nombre del cargo solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return cargo

    def clean_estatus(self):
        estatus = self.cleaned_data.get("estatus")
        validate_condicion(
            estatus,
            "El estado solo puede contener letras, números, espacios y los caracteres .,-.",
        )
        return estatus
