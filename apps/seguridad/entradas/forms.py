from django import forms

from .models import Entrada
from helpers.FormBase import FormBase


class EntradaForm(FormBase):
    fecha = FormBase.create_date_field("fecha")
    hora = FormBase.create_time_field("hora")

    class Meta:
        model = Entrada
        fields = (
            "name",
            "apellido",
            "cedula",
            "telefono",
            "fecha",
            "direccion",
            "cargo",
            "hora",
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
