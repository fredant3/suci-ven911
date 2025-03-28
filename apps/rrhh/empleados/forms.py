from django import forms
from rrhh.empleados.models import Empleado
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_nombres_apellidos,
    validate_cedula,
    validate_telefono,
    validate_email,
    validate_direccion,
    validate_basic_text,
)
import datetime


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
            "contratos": forms.SelectMultiple(
                attrs={
                    "class": "form-control select2-multiple",
                    "placeholder": "Seleccione contratos asociados",
                }
            ),
        }

    def clean_nombres(self):
        data = self.cleaned_data.get("nombres")
        validate_nombres_apellidos(
            data, "Los nombres solo pueden contener letras y espacios"
        )
        return data

    def clean_apellidos(self):
        data = self.cleaned_data.get("apellidos")
        validate_nombres_apellidos(
            data, "Los apellidos solo pueden contener letras y espacios"
        )
        return data

    def clean_cedula(self):
        data = self.cleaned_data.get("cedula")
        validate_cedula(data, "Formato de cédula inválido. Use el formato: V-12345678")
        return data

    def clean_telefono(self):
        data = self.cleaned_data.get("telefono")
        validate_telefono(data, "Formato de teléfono inválido. Use: 0412-1234567")
        return data

    def clean_email(self):
        data = self.cleaned_data.get("email")
        validate_email(data, "Ingrese un correo electrónico válido")
        return data

    def clean_direccion(self):
        data = self.cleaned_data.get("direccion")
        validate_direccion(data, "La dirección contiene caracteres no permitidos")
        return data

    def clean_fecha_nacimiento(self):
        data = self.cleaned_data.get("fecha_nacimiento")
        if data and data.year > (datetime.date.today().year - 18):
            raise forms.ValidationError("El empleado debe ser mayor de edad")
        return data

    def clean_estatus(self):
        data = self.cleaned_data.get("estatus")
        validate_basic_text(data, "Seleccione un estatus válido")
        return data

    def clean_sexo(self):
        data = self.cleaned_data.get("sexo")
        if data not in [choice[0] for choice in Empleado.SEXO_CHOICES]:
            raise forms.ValidationError("Seleccione un género válido")
        return data

    def clean(self):
        cleaned_data = super().clean()
        # Validación adicional si es discapacitado
        if cleaned_data.get("discapacitado") and not cleaned_data.get("tipo_sangre"):
            self.add_error(
                "tipo_sangre",
                "Debe especificar tipo de sangre para personas con discapacidad",
            )

        return cleaned_data
