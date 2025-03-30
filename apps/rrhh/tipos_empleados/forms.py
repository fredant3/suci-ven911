from django import forms
from rrhh.tipos_empleados.models import TipoEmpleado
from helpers.FormBase import FormBase


class TipoEmpleadoForm(FormBase):
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
        widgets = {
            "tipo_personal": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione tipo de personal",
                }
            ),
            "estatus": forms.Select(
                attrs={"class": "form-control", "placeholder": "Seleccione estatus"}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        # Validación adicional para asegurar combinación válida
        tipo_personal = cleaned_data.get("tipo_personal")
        estatus = cleaned_data.get("estatus")

        if tipo_personal and estatus:
            if not TipoEmpleado.objects.filter(
                tipo_personal=tipo_personal, estatus=estatus
            ).exists():
                self.add_error(
                    None, "La combinación de tipo de personal y estatus no es válida"
                )

        return cleaned_data
