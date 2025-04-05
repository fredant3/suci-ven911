from django import forms
from rrhh.cuentas.models import Cuenta
from helpers.FormBase import FormBase


class CuentaForm(FormBase):
    pago_movil = forms.BooleanField(label="Pago Móvil",
        required=False,
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input", "role": "switch", "value": "False"}
        ),
    )

    class Meta:
        model = Cuenta
        fields = (
            "banco",
            "tipo",
            "numero_cuenta",
            "pago_movil",
            "telefono",
            "empleado",
        )
        widgets = {
            "banco": forms.Select(
                attrs={"class": "form-control", "placeholder": "Seleccione un banco"}
            ),
            "tipo": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione el tipo de cuenta",
                }
            ),
            "numero_cuenta": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: 01234567890123456789",
                    "inputmode": "numeric",
                }
            ),
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: 0412-1234567"}
            ),
            "empleado": forms.Select(
                attrs={"class": "form-control", "placeholder": "Seleccione un empleado"}
            ),
        }

    # Validación adicional para campos relacionados
    def clean(self):
        cleaned_data = super().clean()

        # Validar que si pago_movil está activado, el teléfono sea obligatorio
        if cleaned_data.get("pago_movil") and not cleaned_data.get("telefono"):
            self.add_error(
                "telefono",
                "Debe ingresar un número de teléfono para activar el pago móvil",
            )

        return cleaned_data
