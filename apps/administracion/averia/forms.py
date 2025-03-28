from administracion.averia.models import Averia
from helpers.FormBase import FormBase
from django import forms
from helpers.validForm import (
    validate_problema,
    validate_ubicacion,
    validate_serial,
    validate_codigo_bn,
)


class AveriaForm(FormBase):
    class Meta:
        model = Averia
        fields = [
            "problema",
            "tipo_averia",
            "departamento",
            "ubicacion",
            "serial",
            "codigo_bn",
        ]
        labels = {
            "problema": "Problema",
            "tipo_averia": "Tipo de avería",
            "departamento": "Departamento",
            "ubicacion": "Ubicación",
            "serial": "Serial",
            "codigo_bn": "Código BN",
        }
        widgets = {
            "problema": forms.TextInput(attrs={"placeholder": "Ingrese el problema"}),
            "tipo_averia": forms.Select(
                attrs={"placeholder": "Seleccione el tipo de avería"}
            ),
            "departamento": forms.Select(
                attrs={"placeholder": "Seleccione el departamento"}
            ),
            "ubicacion": forms.TextInput(attrs={"placeholder": "Ingrese la ubicación"}),
            "serial": forms.TextInput(attrs={"placeholder": "Ingrese el serial"}),
            "codigo_bn": forms.TextInput(attrs={"placeholder": "Ingrese el código BN"}),
        }

    def clean_problema(self):
        problema = self.cleaned_data.get("problema")
        validate_problema(
            problema,
            "El problema solo puede contener letras, números, espacios y los caracteres .,-",
        )
        return problema

    def clean_ubicacion(self):
        ubicacion = self.cleaned_data.get("ubicacion")
        validate_ubicacion(
            ubicacion,
            "La ubicación solo puede contener letras, números, espacios y los caracteres .,-",
        )
        return ubicacion

    def clean_serial(self):
        serial = self.cleaned_data.get("serial")
        validate_serial(
            serial,
            "El serial solo puede contener letras, números y el caracter -",
        )
        return serial

    def clean_codigo_bn(self):
        codigo_bn = self.cleaned_data.get("codigo_bn")
        validate_codigo_bn(
            codigo_bn,
            "El código BN solo puede contener letras, números y el caracter -",
        )
        return codigo_bn
