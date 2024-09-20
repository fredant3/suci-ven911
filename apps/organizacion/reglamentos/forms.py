from django import forms
from django.forms.fields import DateTimeInput

from .models import Reglamento


class ReglamentoForm(forms.ModelForm):
    class Meta:
        model = Reglamento
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
