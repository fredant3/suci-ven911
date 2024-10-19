from django import forms

from .models import Bien


class BienForm(forms.ModelForm):
    class Meta:
        model = Bien
        fields = (
            "bien",
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
