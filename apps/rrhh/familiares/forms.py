from django import forms
from rrhh.familiares.models import Familiar
from helpers.FormBase import FormBase
from rrhh.empleados.models import Empleado
from helpers.validForm import (
    validate_nombres_apellidos,
    validate_cedula,
    validate_observaciones,
    validate_condicion,
)
from django.utils import timezone


class FamiliarForm(FormBase):
    fecha_nacimiento = FormBase.create_date_field(
        "fecha_nacimiento",
        title="Fecha de nacimiento",
    )

    class Meta:
        model = Familiar
        fields = (
            "parentezco",
            "tipo_hijo",
            "discapacidad",
            "nombres",
            "apellidos",
            "cedula",
            "fecha_nacimiento",
            "sexo",
            "estado_civil",
            "empleado",
            "observacion",
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
        labels = {
            "empleado": "Empleado",
            "tipo_hijo": "Tipo de hijo",
            "observacion": "Observaciones",
        }
        widgets = {
            "parentezco": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione el parentesco",
                }
            ),
            "tipo_hijo": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione tipo de hijo",
                }
            ),
            "nombres": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese nombres completos",
                }
            ),
            "apellidos": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese apellidos completos",
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
            "empleado": forms.Select(
                attrs={"class": "form-control", "placeholder": "Seleccione empleado"}
            ),
            "observacion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese observaciones relevantes",
                    "rows": 3,
                }
            ),
            "discapacidad": forms.CheckboxInput(
                attrs={"class": "form-check-input", "role": "switch"}
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
        validate_cedula(data, "Formato de cédula inválido. Use: V-12345678")
        return data

    def clean_observacion(self):
        data = self.cleaned_data.get("observacion") or ""
        validate_observaciones(
            data, "Las observaciones contienen caracteres no permitidos"
        )
        return data

    def clean_parentezco(self):
        data = self.cleaned_data.get("parentezco")
        validate_condicion(data, "Seleccione un parentesco válido")
        return data

    def clean_empleado(self):
        empleado = self.cleaned_data.get("empleado")
        if not Empleado.objects.filter(id=empleado.id).exists():
            raise forms.ValidationError("Seleccione un empleado válido")
        return empleado

    def clean_fecha_nacimiento(self):
        data = self.cleaned_data.get("fecha_nacimiento")
        if data and data > timezone.now().date():
            raise forms.ValidationError("La fecha de nacimiento no puede ser futura")
        return data

    def clean(self):
        cleaned_data = super().clean()
        discapacidad = cleaned_data.get("discapacidad")
        observacion = cleaned_data.get("observacion", "")

        if discapacidad and not observacion:
            self.add_error(
                "observacion",
                "Debe agregar una observación cuando existe una discapacidad",
            )

        return cleaned_data
