from django import forms
from .models import Sueldo
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_general_text,
    validate_codigo_bn,
    validate_url,
    validate_decimal_number,
)


class SueldoForm(FormBase):
    fecha_inicio = FormBase.create_date_field(
        "fecha_inicio", title="Fecha de Inicio", attrs={"placeholder": "DD/MM/AAAA"}
    )
    fecha_culminacion = FormBase.create_date_field(
        "fecha_culminacion",
        title="Fecha de Culminación",
        attrs={"placeholder": "DD/MM/AAAA"},
    )

    class Meta:
        model = Sueldo
        fields = (
            "colegio",
            "codigo_titulo",
            "titulo",
            "area_conocimiento",
            "fecha_inicio",
            "fecha_culminacion",
            "enlace_certificado",
            "personal",
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
            "colegio": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Colegio de Ingenieros de Venezuela",
                }
            ),
            "codigo_titulo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: T-2023-001"}
            ),
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Ingeniero Senior Nivel III",
                }
            ),
            "area_conocimiento": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Ingeniería de Sistemas",
                }
            ),
            "enlace_certificado": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://certificados.com/ejemplo.pdf",
                }
            ),
            "personal": forms.Select(
                attrs={"class": "form-control", "placeholder": "Seleccione un empleado"}
            ),
        }

    def clean_codigo_titulo(self):
        data = self.cleaned_data.get("codigo_titulo")
        validate_codigo_bn(
            data, "El código del título solo permite letras, números y guiones"
        )
        return data

    def clean_enlace_certificado(self):
        data = self.cleaned_data.get("enlace_certificado")
        validate_url(
            data,
            "Ingrese una URL válida para el certificado (ej: https://ejemplo.com/certificado.pdf)",
        )
        return data

    def clean_colegio(self):
        data = self.cleaned_data.get("colegio")
        validate_general_text(
            data,
            "El nombre del colegio solo permite caracteres alfanuméricos y símbolos comunes",
        )
        return data

    def clean_titulo(self):
        data = self.cleaned_data.get("titulo")
        validate_general_text(data, "El título contiene caracteres no permitidos")
        return data

    def clean_personal(self):
        data = self.cleaned_data.get("personal")
        if not data or not data.pk:
            raise forms.ValidationError("Seleccione un empleado válido")
        return data

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_culminacion = cleaned_data.get("fecha_culminacion")

        if fecha_inicio and fecha_culminacion:
            if fecha_culminacion < fecha_inicio:
                self.add_error(
                    "fecha_culminacion",
                    "La fecha de culminación no puede ser anterior a la fecha de inicio",
                )

        return cleaned_data
