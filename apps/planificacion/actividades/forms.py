from django import forms
from planificacion.actividades.models import Actividad
from helpers.FormBase import FormBase


class ActividadForm(FormBase):
    fechai = FormBase.create_date_field("date")
    fechaf = FormBase.create_date_field("date")

    class Meta:
        model = Actividad
        fields = (
            "fechai",
            "fechaf",
            "objetiv",
            "meta",
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
