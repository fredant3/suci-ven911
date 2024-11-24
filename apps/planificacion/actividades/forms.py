from django import forms
from planificacion.actividades.models import Actividad


class ActividadForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))
    fechaf = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Actividad
        fields = (
            "fechai",
            "fechaf",
            "objetiv",
            "meta",
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
