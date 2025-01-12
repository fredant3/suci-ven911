from django import forms

from seguridad.entradas.models import Entrada


class EntradaForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))
    hora = forms.CharField(widget=forms.TextInput(attrs={"type": "time"}))

    class Meta:
        model = Entrada
        fields = (
            "name",
            "apellido",
            "cedula",
            "telefono",
            "fecha",
            "direccion",
            "cargo",
            "hora",
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
