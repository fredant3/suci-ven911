from django import forms
from django.forms.fields import DateTimeInput
from organizacion.reglamentos.models import Reglamento
from helpers.FormBase import FormBase


class ReglamentoForm(FormBase):
    estado = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"value": "True"})
    )

    date = FormBase.create_date_field("date")

    def clean_estado(self):
        estado = self.cleaned_data.get("estado")
        return estado if estado is not None else False

    class Meta:
        model = Reglamento
        fields = [
            "name",
            "file",
            "date",
            "progre",
            "estado",
        ]
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]
