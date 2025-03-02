from django import forms
from rrhh.empleados.models import Empleado
from rrhh.dotaciones.models import Dotacion
from helpers.FormBase import FormBase


class DotacionForm(FormBase):
    class Meta:
        model = Dotacion
        fields = (
            "camisa",
            "pantalon",
            "zapato",
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
        labels = {
            "empleado": "Empleado",
        }
        widgets = {}
