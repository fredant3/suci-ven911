from django import forms

from rrhh.familiares.models import Familiar
from helpers.FormBase import FormBase


class FamiliarForm(FormBase):
    class Meta:
        model = Familiar
        fields = (
            "parentezco",
            "tipo_hijo",
            "discapacidad",
            "nombres",
            "apellidos",
            "cedula",
            "fecha_nacimiento",
            "sexo",
            "estado_civil",
            "empleado",
            "observacion",
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
