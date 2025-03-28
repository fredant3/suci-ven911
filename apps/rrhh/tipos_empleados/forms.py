from django import forms
from rrhh.tipos_empleados.models import TipoEmpleado
from helpers.FormBase import FormBase
from helpers.validForm import validate_condicion, validate_ente


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
        labels = {"tipo_personal": "Tipo de Personal", "estatus": "Estado Actual"}

    def clean_tipo_personal(self):
        data = self.cleaned_data.get("tipo_personal")
        validate_ente(
            data,
            "El tipo de personal solo puede contener letras, números y caracteres especiales válidos",
        )
        return data

    def clean_estatus(self):
        data = self.cleaned_data.get("estatus")
        validate_condicion(
            data, "Seleccione un estatus válido para el tipo de personal"
        )
        return data

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
