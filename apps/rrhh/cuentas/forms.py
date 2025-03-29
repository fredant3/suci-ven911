from django import forms
from rrhh.cuentas.models import Cuenta
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_codigo_bn,
    validate_telefono,
    validate_basic_text,
    validate_cantidad,
    validate_general_text,
)
from rrhh.empleados.models import Empleado


class CuentaForm(FormBase):
    pago_movil = forms.BooleanField(
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
        labels = {
            "empleado": "Empleado",
            "pago_movil": "¿Activar pago móvil?",
            "numero_cuenta": "Número de cuenta",
            "telefono": "Teléfono móvil",
        }
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

    def clean_numero_cuenta(self):
        numero = self.cleaned_data.get("numero_cuenta")
        validate_codigo_bn(
            numero, "El número de cuenta solo puede contener números y guiones"
        )
        return numero

    def clean_telefono(self):
        telefono = self.cleaned_data.get("telefono")
        validate_telefono(
            telefono,
            "Formato de teléfono inválido. Use números y guiones (Ej: 0412-1234567)",
        )
        return telefono

    def clean_banco(self):
        banco = self.cleaned_data.get("banco")
        validate_basic_text(banco, "Seleccione un banco válido de la lista")
        return banco

    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        validate_general_text(tipo, "Seleccione un tipo de cuenta válido")
        return tipo

    def clean_empleado(self):
        empleado = self.cleaned_data.get("empleado")
        # Validación básica de que el empleado existe
        if not Empleado.objects.filter(id=empleado.id).exists():
            raise forms.ValidationError("Seleccione un empleado válido")
        return empleado

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
