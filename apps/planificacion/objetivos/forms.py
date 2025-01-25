from django import forms
from django.forms.fields import DateTimeInput
from planificacion.objetivos.models import Objetivo
from helpers.FormBase import FormBase


class ObjetivoForm(FormBase):
    fechai = FormBase.create_date_field("fechai")
    fechaf = FormBase.create_date_field("fechaf")

    class Meta:
        model = Objetivo
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
