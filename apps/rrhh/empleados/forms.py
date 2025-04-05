from django.forms import (
    TextInput,
    EmailInput,
    ValidationError,
)
from rrhh.empleados.models import Empleado
from helpers.FormBase import FormBase
from helpers.validForm import validate_email
from datetime import date


class EmpleadoForm(FormBase):
    fecha_nacimiento = FormBase.create_date_field(
        "fecha_nacimiento",
        title="Fecha de Nacimiento",
    )

    class Meta:
        model = Empleado
        fields = (
            "estatus",
            "nombres",
            "apellidos",
            "nacionalidad",
            "cedula",
            "sexo",
            "fecha_nacimiento",
            "estado_civil",
            "tipo_sangre",
            "email",
            "telefono",
            "direccion",
            "estudia",
            "discapacitado",
            "contratos",
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
            "nombres": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese los nombres completos",
                }
            ),
            "apellidos": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese los apellidos completos",
                }
            ),
            "cedula": TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: V-12345678"}
            ),
<<<<<<< HEAD
            "sexo": forms.Select(
                attrs={"class": "form-control", "placeholder": "Seleccione el Género"}
            ),
            "estado_civil": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione estado civil",
                }
            ),
            "tipo_sangre": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione tipo de sangre",
                }
            ),
            "email": forms.EmailInput(
=======
            "email": EmailInput(
>>>>>>> e31a2b52942413d17d1b2c676ea4316538ac0dee
                attrs={"class": "form-control", "placeholder": "ejemplo@correo.com"}
            ),
            "telefono": TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: 0412-1234567"}
            ),
            "direccion": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Av. Principal, Edificio X, Piso 3",
                }
            ),
        }

    def clean_email(self):
        data = self.cleaned_data.get("email")
        validate_email(data, "Ingrese un correo electrónico válido")
        return data

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get("fecha_nacimiento")

        if fecha:
            hoy = date.today()
            # Calcula la edad exacta
            edad = (
                hoy.year
                - fecha.year
                - ((hoy.month, hoy.day) < (fecha.month, fecha.day))
            )

            if edad < 18:
                raise ValidationError("Debe ser mayor de edad (18+ años).")

        return fecha

    def clean(self):
        cleaned_data = super().clean()

        # Validación adicional si es discapacitado
        if cleaned_data.get("discapacitado") == "si" and not cleaned_data.get(
            "tipo_sangre"
        ):
            self.add_error(
                "tipo_sangre",
                "Debe especificar tipo de sangre para personas con discapacidad",
            )

        return cleaned_data
