from django import forms

from seguridad.gestiones.models import Gestion


class GestionForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))
    hora = forms.CharField(widget=forms.TextInput(attrs={"type": "time"}))

    class Meta:
        model = Gestion
        fields = (
            "name",
            "apellido",
            "cedula",
            "tipo",
            "descripcion",
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
