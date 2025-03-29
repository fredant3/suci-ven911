from django import forms
from rrhh.empleados.models import Empleado
from helpers.FormBase import FormBase
from helpers.validForm import validate_cedula, validate_email
from datetime import date


class EmpleadoForm(FormBase):
    fecha_nacimiento = FormBase.create_date_field(
        "fecha_nacimiento",
        title="Fecha de nacimiento",
    )
    estudia = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input", "role": "switch"}
        ),
    )
    discapacitado = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input", "role": "switch"}
        ),
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
            "nombres": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese los nombres completos",
                }
            ),
            "apellidos": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese los apellidos completos",
                }
            ),
            "cedula": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: V-12345678"}
            ),
            "sexo": forms.Select(
                attrs={"class": "form-control", "placeholder": "Seleccione el género"}
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
                attrs={"class": "form-control", "placeholder": "ejemplo@correo.com"}
            ),
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: 0412-1234567"}
            ),
            "direccion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Av. Principal, Edificio X, Piso 3",
                }
            ),
            "nacionalidad": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione nacionalidad",
                }
            ),
            "estatus": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione estatus laboral",
                }
            ),
            "contratos": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione contratos asociados",
                }
            ),
        }

    def clean_cedula(self):
        data = self.cleaned_data.get("cedula")
        validate_cedula(data, "Formato de cédula inválido. Use el formato: V-12345678")
        return data

    def clean_email(self):
        data = self.cleaned_data.get("email")
        validate_email(data, "Ingrese un correo electrónico válido")
        return data

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get("fecha_nacimiento")

        if fecha:
            hoy = date.today()
            # Calcula si ha cumplido 18 años exactos
            mayor_edad = hoy.year - fecha.year >= 18
            cumple_este_año = (hoy.month, hoy.day) >= (fecha.month, fecha.day)

            if not (mayor_edad and cumple_este_año):
                raise forms.ValidationError("Debe ser mayor de edad (18+ años)")

        return fecha

    def clean(self):
        cleaned_data = super().clean()
        # Validación adicional si es discapacitado
        if cleaned_data.get("discapacitado") and not cleaned_data.get("tipo_sangre"):
            self.add_error(
                "tipo_sangre",
                "Debe especificar tipo de sangre para personas con discapacidad",
            )

        return cleaned_data
