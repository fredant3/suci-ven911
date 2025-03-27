from potencia.incidencias.models import Incidencia
from helpers.FormBase import FormBase
from django import forms
from helpers.validForm import (
    validate_condicion,
    validate_sede,
    validate_observaciones,
    validate_ente,
    validate_problema,
)


class IncidenciaForm(FormBase):
    class Meta:
        model = Incidencia
        fields = (
            "estado",
            "sede",
            "departamento",
            "tipo_incidencia",
            "observaciones",
            "tipo_solicitud",
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
            "tipo_incidencia": "Tipo de incidencia",
            "tipo_solicitud": "Tipo de solicitud",
        }
        widgets = {
            "estado": forms.Select(
                attrs={
                    "class": "form-select mb-3",
                    "placeholder": "Seleccione el estado",
                }
            ),
            "sede": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre de la sede",
                }
            ),
            "departamento": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el departamento",
                }
            ),
            "tipo_incidencia": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el tipo de incidencia",
                }
            ),
            "observaciones": forms.Textarea(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese las observaciones",
                }
            ),
            "tipo_solicitud": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el tipo de solicitud",
                }
            ),
        }

    def clean_estado(self):
        estado = self.cleaned_data.get("estado")
        validate_condicion(
            estado,
            "El estado solo puede contener letras, números, espacios y los caracteres .,-.",
        )
        return estado

    def clean_sede(self):
        sede = self.cleaned_data.get("sede")
        validate_sede(
            sede, "El nombre de sede solo puede contener letras, números y espacios."
        )
        return sede

    def clean_departamento(self):
        departamento = self.cleaned_data.get("departamento")
        validate_sede(
            departamento,
            "El departamento solo puede contener letras, números y espacios.",
        )
        return departamento

    def clean_tipo_incidencia(self):
        tipo = self.cleaned_data.get("tipo_incidencia")
        validate_problema(
            tipo,
            "El tipo de incidencia solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return tipo

    def clean_observaciones(self):
        obs = self.cleaned_data.get("observaciones")
        validate_observaciones(
            obs, "Use solo letras, números, espacios y los caracteres .,-!?()."
        )
        return obs

    def clean_tipo_solicitud(self):
        solicitud = self.cleaned_data.get("tipo_solicitud")
        validate_ente(
            solicitud,
            "El tipo de solicitud solo puede contener letras, números, espacios y los caracteres .,-!?().",
        )
        return solicitud
