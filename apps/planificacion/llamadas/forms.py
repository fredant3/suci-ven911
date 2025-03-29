from django import forms
from planificacion.llamadas.models import Llamada
from helpers.FormBase import FormBase


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
        # labels = {
        #     "estado": "Estado de la llamada",
        #     "mes": "Mes de registro",
        #     "informativa": "Llamadas informativas",
        #     "falsa": "Llamadas falsas",
        #     "realesno": "Llamadas reales no atendidas",
        #     "realesf": "Llamadas reales finalizadas",
        #     "videop": "Videollamadas programadas",
        # }
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
