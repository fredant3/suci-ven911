from asesoria.filmicos.models import RegistroFilmico
from helpers.FormBase import FormBase
from django.forms.fields import DateTimeInput


class RegistroFilmicoForm(FormBase):
    fecha_solicitud = FormBase.create_date_field("fecha_solicitud")
    fecha_culminacion = FormBase.create_date_field("fecha_culminacion")

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
