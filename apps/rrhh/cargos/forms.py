from django import forms

from .models import Cargo


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = (
            "cargo",
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
