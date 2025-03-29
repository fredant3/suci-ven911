from django import forms
from rrhh.empleados.models import Empleado
from rrhh.educaciones.models import Educacion
from helpers.FormBase import FormBase
from helpers.validForm import validate_general_text, validate_codigo_bn, validate_url


class EducacionForm(FormBase):
    fecha_inicio = FormBase.create_date_field(
        "fecha_inicio",
        title="Fecha de Inicio",
    )
    fecha_culminacion = FormBase.create_date_field(
        "fecha_culminacion",
        title="Fecha de Culminación",
    )

    class Meta:
        model = Educacion
        fields = (
            "colegio",
            "codigo_titulo",
            "titulo",
            "area_conocimiento",
            "fecha_inicio",
            "fecha_culminacion",
            "enlace_certificado",
            "empleado",
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
            "codigo_titulo": "Código del Título",
            "area_conocimiento": "Área de Conocimiento",
            "enlace_certificado": "Enlace al Certificado",
        }
        widgets = {
            "colegio": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Universidad Central de Venezuela",
                }
            ),
            "codigo_titulo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: T-2023-001"}
            ),
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Licenciatura en Administración",
                }
            ),
            "area_conocimiento": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Ciencias Administrativas",
                }
            ),
            "enlace_certificado": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://ejemplo.com/certificado.pdf",
                }
            ),
            "empleado": forms.Select(
                attrs={"class": "form-control", "placeholder": "Seleccione un empleado"}
            ),
        }

    def clean_colegio(self):
        data = self.cleaned_data.get("colegio")
        validate_general_text(
            data,
            "El nombre de la institución solo puede contener letras, números y caracteres especiales comunes",
        )
        return data

    def clean_codigo_titulo(self):
        data = self.cleaned_data.get("codigo_titulo")
        validate_codigo_bn(
            data, "El código del título solo permite letras, números y guiones"
        )
        return data

    def clean_titulo(self):
        data = self.cleaned_data.get("titulo")
        validate_general_text(
            data, "El título académico contiene caracteres no permitidos"
        )
        return data

    def clean_area_conocimiento(self):
        data = self.cleaned_data.get("area_conocimiento")
        validate_general_text(
            data, "El área de conocimiento contiene caracteres no permitidos"
        )
        return data

    def clean_enlace_certificado(self):
        data = self.cleaned_data.get("enlace_certificado")
        validate_url(
            data,
            "Ingrese una URL válida para el certificado (ej: https://ejemplo.com/certificado.pdf)",
        )
        return data

    def clean_empleado(self):
        empleado = self.cleaned_data.get("empleado")
        if not Empleado.objects.filter(id=empleado.id).exists():
            raise forms.ValidationError("Seleccione un empleado válido")
        return empleado

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
