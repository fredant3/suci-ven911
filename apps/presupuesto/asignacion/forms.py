from django import forms

from .models import Asignacion


class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ("nombredir", "presuasig", "objeanual", "numpartida")
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
