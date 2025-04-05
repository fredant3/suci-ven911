from django import forms
from rrhh.empleados.models import Empleado
from helpers.FormBase import FormBase
from helpers.validForm import validate_email
from datetime import date


class EmpleadoForm(FormBase):
    fecha_nacimiento = FormBase.create_date_field(
        "fecha_nacimiento",
        title="Fecha de nacimiento",
    )
    estudia = forms.BooleanField(
        initial=False,
        required=False,
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input", "role": "switch", "value": "False"}
        ),
    )
    discapacitado = forms.BooleanField(
        initial=False,
        required=False,
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input", "role": "switch", "value": "False"}
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
            "tipo_contrato",
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
                raise forms.ValidationError("Debe ser mayor de edad (18+ años).")

        return fecha

    def clean_discapacitado(self):
        print(self.cleaned_data.get("discapacitado", False))
        return self.cleaned_data.get("discapacitado", False)

    def clean_estudia(self):
        print(self.cleaned_data.get("estudia", False))
        return self.cleaned_data.get("estudia", False)

    def clean(self):
        cleaned_data = super().clean()

        # Validación adicional si es discapacitado
        if cleaned_data.get("discapacitado") and not cleaned_data.get("tipo_sangre"):
            self.add_error(
                "tipo_sangre",
                "Debe especificar tipo de sangre para personas con discapacidad",
            )

        return cleaned_data
