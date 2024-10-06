from django import forms

from .models import Accion

# from django.forms.fields import DateTimeInput


class AccionForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Accion
        fields = (
            "nombrep",
            "fechai",
            "fechac",
            "situacionp",
            "montoproyecto",
            "responsableg",
            "responsablet",
            "responsabler",
            "responsablea",
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
        widgets = {
            # "fechai": DateTimeInput(attrs={"type": "date"}),
            # "fechac": DateTimeInput(attrs={"type": "date"}),
        }
