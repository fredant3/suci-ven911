from django import forms

from .models import TipoEmpleado


class TipoEmpleadoForm(forms.ModelForm):
    class Meta:
        model = TipoEmpleado
        fields = (
            "tipo_personal",
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
