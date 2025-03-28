from helpers.FormBase import FormBase
from seguridad.entradas.models import Entrada
from django import forms
from helpers.validForm import (
    validate_nombres_apellidos,
    validate_cedula,
    validate_telefono,
    validate_direccion,
    validate_general_text,
)
from django.utils import timezone


class EntradaForm(FormBase):
    fecha = FormBase.create_date_field(
        "fecha",
        title="Fecha de entrada",
    )
    hora = FormBase.create_time_field(
        "hora",
        title="Hora de entrada",
    )

    class Meta:
        model = Entrada
        fields = (
            "name",
            "apellido",
            "cedula",
            "telefono",
            "fecha",
            "direccion",
            "cargo",
            "hora",
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
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre completo",
                }
            ),
            "apellido": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ingrese los apellidos"}
            ),
            "cedula": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: V-12345678"}
            ),
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: 0412-1234567"}
            ),
            "direccion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Av. Principal, Edificio X",
                }
            ),
            "cargo": forms.Select(
                attrs={"class": "form-control", "placeholder": "Seleccione un cargo"}
            ),
        }

    def clean_name(self):
        data = self.cleaned_data.get("name")
        validate_nombres_apellidos(
            data, "El nombre solo puede contener letras y espacios"
        )
        return data

    def clean_apellido(self):
        data = self.cleaned_data.get("apellido")
        validate_nombres_apellidos(
            data, "Los apellidos solo pueden contener letras y espacios"
        )
        return data

    def clean_cedula(self):
        data = self.cleaned_data.get("cedula")
        validate_cedula(data, "Formato de cédula inválido. Use: V-12345678")
        return data

    def clean_telefono(self):
        data = self.cleaned_data.get("telefono")
        validate_telefono(data, "Formato de teléfono inválido. Use: 0412-1234567")
        return data

    def clean_direccion(self):
        data = self.cleaned_data.get("direccion")
        validate_direccion(data, "La dirección contiene caracteres no permitidos")
        return data

    def clean_cargo(self):
        data = self.cleaned_data.get("cargo")
        validate_general_text(data, "Seleccione un cargo válido")
        return data

    def clean_fecha(self):
        data = self.cleaned_data.get("fecha")
        if data and data > timezone.now().date():
            raise forms.ValidationError("La fecha no puede ser futura")
        return data

    def clean_hora(self):
        data = self.cleaned_data.get("hora")
        if data and data > timezone.now().time():
            raise forms.ValidationError("La hora no puede ser futura")
        return data
