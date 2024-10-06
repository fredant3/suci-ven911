from django import forms

from .models import Sede


class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = (
            "sede",
            "estatus",
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
