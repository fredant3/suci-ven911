from django import forms
from organizacion.normativas.models import Normativa
from helpers.FormBase import FormBase


class NormativaForm(FormBase):
    # estado = forms.BooleanField(
    #     widget=forms.CheckboxInput(attrs={"value": "True"}), required=False
    # )

    # def clean_estado(self):
    #     estado = self.cleaned_data.get("estado")
    #     return estado if estado is not None else False

    date = FormBase.create_date_field("date")

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields.pop("file")

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
