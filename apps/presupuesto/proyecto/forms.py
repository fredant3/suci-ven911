from django import forms
from helpers.FormBase import FormBase

from presupuesto.proyecto.models import Proyecto


class ProyectoForm(FormBase):
    fechai = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Proyecto
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
