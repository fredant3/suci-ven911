from django import forms
from planificacion.llamadas.models import Llamada
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_basic_text,
    validate_cantidad,
    validate_decimal_number,
)


class LlamadaForm(FormBase):
    fecha_denuncia = FormBase.create_date_field(
        "fecha_denuncia", title="Fecha de denuncia"
    )
    fecha_incidente = FormBase.create_date_field(
        "fecha_incidente", title="Fecha de incidente"
    )

    class Meta:
        model = Llamada
        fields = (
            "estado",
            "mes",
            "informativa",
            "falsa",
            "realesno",
            "realesf",
            "videop",
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
            "estado": "Estado de la llamada",
            "mes": "Mes de registro",
            "informativa": "Llamadas informativas",
            "falsa": "Llamadas falsas",
            "realesno": "Llamadas reales no atendidas",
            "realesf": "Llamadas reales finalizadas",
            "videop": "Videollamadas programadas",
        }
        widgets = {
            "estado": forms.Select(
                attrs={
                    "class": "form-select mb-3",
                    "placeholder": "Seleccione el estado",
                }
            ),
            "mes": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Mes programado",
                }
            ),
            "informativa": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Número de llamadas informativas",
                }
            ),
            "falsa": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Número de llamadas falsas",
                }
            ),
            "realesno": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Número de llamadas reales no atendidas",
                }
            ),
            "realesf": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Número de llamadas reales finalizadas",
                }
            ),
            "videop": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Número de videollamadas programadas",
                }
            ),
        }

    def clean_generic_number(self, field_name, label):
        value = self.cleaned_data.get(field_name)
        validate_cantidad(value, f"{label} debe ser un número entero positivo")
        return value

    def clean_informativa(self):
        return self.clean_generic_number("informativa", "Las llamadas informativas")

    def clean_falsa(self):
        return self.clean_generic_number("falsa", "Las llamadas falsas")

    def clean_realesno(self):
        return self.clean_generic_number("realesno", "Las llamadas reales no atendidas")

    def clean_realesf(self):
        return self.clean_generic_number("realesf", "Las llamadas reales finalizadas")

    def clean_videop(self):
        return self.clean_generic_number("videop", "Las videollamadas programadas")

    def clean_estado(self):
        estado = self.cleaned_data.get("estado")
        validate_basic_text(
            estado,
            "El estado solo puede contener letras, números, espacios y los caracteres .,-.",
        )
        return estado

    def clean_mes(self):
        mes = self.cleaned_data.get("mes")
        validate_cantidad(mes, "El mes debe ser un número entre 1 y 12")
        if not (1 <= int(mes) <= 12):
            raise forms.ValidationError("El mes debe estar entre 1 y 12")
        return mes

    def clean(self):
        cleaned_data = super().clean()
        fecha_incidente = cleaned_data.get("fecha_incidente")
        fecha_denuncia = cleaned_data.get("fecha_denuncia")

        if fecha_incidente and fecha_denuncia:
            if fecha_incidente > fecha_denuncia:
                self.add_error(
                    "fecha_incidente",
                    "La fecha de incidente no puede ser posterior a la fecha de denuncia",
                )

        return cleaned_data
