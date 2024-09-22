from django import forms
from django.forms.fields import DateTimeInput

from .models import Normativa


class NormativaForm(forms.ModelForm):
    estado = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"value": "True"})
    )

    def clean_estado(self):
        estado = self.cleaned_data.get("estado")
        return estado if estado is not None else False

    class Meta:
        model = Normativa
        fields = [
            "name",
            "file",
            "user",
            "date",
            "progre",
            "estado",
        ]
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
        widgets = {
            "date": DateTimeInput(attrs={"type": "date"}),
        }
