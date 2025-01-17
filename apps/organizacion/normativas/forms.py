from django import forms
from django.forms.fields import DateTimeInput
from organizacion.normativas.models import Normativa

class NormativaForm(forms.ModelForm):
    class Meta:
        model = Normativa
        fields = [
            "name",
            "file",
            "user",
            "date",
            "progre",
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

class NormativaFormD(forms.ModelForm):
    class Meta:
        model = Normativa
        fields = [
            "name",
            "user",
            "date",
            "progre",
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
