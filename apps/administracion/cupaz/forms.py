from django import forms

from .models import CuadrantePaz


class CuadrantePazForm(forms.ModelForm):
    class Meta:
        model = CuadrantePaz
        fields = ("nombre",)
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
