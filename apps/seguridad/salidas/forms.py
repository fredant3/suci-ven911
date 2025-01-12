from django import forms

from seguridad.salidas.models import Salida


class SalidaForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))
    hora = forms.CharField(widget=forms.TextInput(attrs={"type": "time"}))

    class Meta:
        model = Salida
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
