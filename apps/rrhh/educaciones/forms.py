from django import forms

from rrhh.educaciones.models import Educacion
from helpers.FormBase import FormBase


class EducacionForm(FormBase):
    fecha_inicio = FormBase.create_date_field("fecha_inicio")
    fecha_culminacion = FormBase.create_date_field("fecha_culminacion")

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
