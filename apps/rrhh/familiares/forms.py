from django import forms
from rrhh.familiares.models import Familiar
from helpers.FormBase import FormBase
from rrhh.empleados.models import Empleado


class FamiliarForm(FormBase):
    fecha_nacimiento = FormBase.create_date_field("fecha_nacimiento")

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
        labels = {
            "empleado": "Empleado",
        }
        widgets = {}
