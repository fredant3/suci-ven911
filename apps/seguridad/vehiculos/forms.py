from django import forms

from seguridad.vehiculos.models import Vehiculo


class VehiculoForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))
    hora = forms.CharField(widget=forms.TextInput(attrs={"type": "time"}))

    class Meta:
        model = Vehiculo
        fields = (
            "nombre",
            "apellido",
            "cedula",
            "modelo",
            "vehiculo",
            "motivo",
            "capagasolina",
            "cantigasolina",
            "placa",
            "fecha",
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
