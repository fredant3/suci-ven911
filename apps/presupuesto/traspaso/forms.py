from django import forms
from presupuesto.traspaso.models import PROYECTOS_ACCIONES, Traspaso
from presupuesto.cedente.models import Cedente
from helpers.FormBase import FormBase


class TraspasoForm(FormBase):

    class Meta:
        model = Traspaso
        fields = ["proyecto_acciones"]
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
            # "proyecto_acciones": forms.Select(
            #     choices=PROYECTOS_ACCIONES
            # )
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
