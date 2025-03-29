from asesoria.filmicos.models import RegistroFilmico
from helpers.FormBase import FormBase
from django import forms


class RegistroFilmicoForm(FormBase):
    fecha_solicitud = FormBase.create_date_field(
        "fecha_solicitud", "Fecha de Solicitud"
    )
    fecha_culminacion = FormBase.create_date_field(
        "fecha_culminacion", "Fecha de Culminacion"
    )

    class Meta:
        model = RegistroFilmico
        fields = [
            "estatus",
            "direccion",
            "camara",
            "motivo_solicitud",
            "ente_solicita",
            "fecha_solicitud",
            "fecha_culminacion",
        ]
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
            "estatus": forms.Select(attrs={"placeholder": "Seleccione el estatus"}),
            "direccion": forms.TextInput(attrs={"placeholder": "Ingrese la dirección"}),
            "camara": forms.TextInput(attrs={"placeholder": "Ingrese la cámara"}),
            "motivo_solicitud": forms.TextInput(
                attrs={"placeholder": "Ingrese el motivo de la solicitud"}
            ),
            "ente_solicita": forms.TextInput(
                attrs={"placeholder": "Ingrese el ente que solicita"}
            ),
        }
