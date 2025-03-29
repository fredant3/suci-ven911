from django import forms
from planificacion.infraestructuras.models import Infraestructura
from helpers.FormBase import FormBase


class InfraestructuraForm(FormBase):
    class Meta:
        model = Infraestructura
        fields = (
            "estado",
            "mes",
            "infraestructura",
            "cantidad",
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
        #     "estado": "Estado de la infraestructura",
        #     "mes": "Mes programado",
        #     "infraestructura": "Nombre de la infraestructura",
        #     "cantidad": "Cantidad estimada",
        # }
        widgets = {
            "estado": forms.TextInput(
                attrs={
                    "placeholder": "Estado de la infraestructura",
                }
            ),
            "mes": forms.TextInput(
                attrs={
                    "placeholder": "Mes programado",
                }
            ),
            "infraestructura": forms.TextInput(
                attrs={
                    "placeholder": "Nombre de la infraestructura",
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={
                    "placeholder": "Cantidad estimada",
                }
            ),
        }
