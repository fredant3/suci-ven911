from helpers.FormBase import FormBase
from seguridad.gestiones.models import Gestion
from django import forms
from django.utils import timezone
from helpers.validForm import (
    validate_nombres_apellidos,
    validate_cedula,
    validate_direccion,
    validate_ente,
    validate_observaciones,
)


class GestionForm(FormBase):
    fecha = FormBase.create_date_field(
        "fecha",
        title="Fecha de gestión",
    )
    hora = FormBase.create_time_field(
        "hora",
        title="Hora de gestión",
    )

    class Meta:
        model = Gestion
        fields = (
            "name",
            "apellido",
            "cedula",
            "tipo",
            "descripcion",
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
            "tipo": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione tipo de gestión",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Detalle de la gestión...",
                    "rows": 3,
                }
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
        labels = {"tipo": "Tipo de Gestión", "descripcion": "Descripción Detallada"}

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

    def clean_tipo(self):
        data = self.cleaned_data.get("tipo")
        validate_ente(data, "Seleccione un tipo de gestión válido")
        return data

    def clean_descripcion(self):
        data = self.cleaned_data.get("descripcion")
        validate_observaciones(data, "La descripción contiene caracteres no permitidos")
        return data

    def clean_direccion(self):
        data = self.cleaned_data.get("direccion")
        validate_direccion(data, "La dirección contiene caracteres no permitidos")
        return data

    def clean_cargo(self):
        data = self.cleaned_data.get("cargo")
        validate_ente(data, "Seleccione un cargo válido")
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

    def clean(self):
        cleaned_data = super().clean()
        # Validación adicional si es necesario
        if cleaned_data.get("tipo") == "urgente" and not cleaned_data.get(
            "descripcion"
        ):
            self.add_error(
                "descripcion", "Las gestiones urgentes requieren descripción detallada"
            )

        return cleaned_data
