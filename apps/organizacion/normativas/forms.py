from django import forms
from organizacion.normativas.models import Normativa
from helpers.FormBase import FormBase


class NormativaForm(FormBase):
    estado = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"value": "True"})
    )

    def clean_estado(self):
        estado = self.cleaned_data.get("estado")
        return estado if estado is not None else False

    date = FormBase.create_date_field("date")

    class Meta:
        model = Normativa
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
