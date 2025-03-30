from django import forms
from rrhh.tipos_empleados.models import TipoEmpleado
from helpers.FormBase import FormBase

COMBINACIONES_VALIDAS = [
    ("per", "act"),
    ("per", "ina"),
]


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
        print(self.cleaned_data)
        cleaned_data = super().clean()
        tipo_personal = cleaned_data.get("tipo_personal")
        estatus = cleaned_data.get("estatus")

        if (tipo_personal, estatus) not in COMBINACIONES_VALIDAS:
            raise forms.ValidationError(
                "La combinación de tipo de personal y estatus no es válida."
            )

        return cleaned_data
