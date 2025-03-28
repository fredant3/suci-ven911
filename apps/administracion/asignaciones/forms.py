from administracion.asignaciones.models import Asignacion
from administracion.inventario.models import Articulo
from django import forms
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_cantidad,
    validate_basic_text,
)


class AsignacionForm(FormBase):
    class Meta:
        model = Asignacion
        fields = [
            "articulo",
            "sede",
            "departamento",
            "cantidad",
            "descripcion",
            "observaciones",
        ]
        labels = {
            "articulo": "Artículo",
            "sede": "Sede",
            "departamento": "Departamento",
            "cantidad": "Cantidad",
            "descripcion": "Descripción",
            "observaciones": "Observaciones",
        }
        widgets = {
            "articulo": forms.Select(attrs={"placeholder": "Seleccione un artículo"}),
            "sede": forms.Select(attrs={"placeholder": "Seleccione una sede"}),
            "departamento": forms.Select(
                attrs={"placeholder": "Seleccione un departamento"}
            ),
            "cantidad": forms.NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "descripcion": forms.TextInput(
                attrs={"placeholder": "Ingrese una descripción"}
            ),
            "observaciones": forms.TextInput(
                attrs={"placeholder": "Ingrese observaciones"}
            ),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        validate_cantidad(cantidad, "La cantidad tiene que ser un numero entero")
        return cantidad

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        validate_basic_text(
            descripcion,
            "La descripción solo puede contener letras, números, espacios y los caracteres .,-",
        )
        return descripcion

    def clean_observaciones(self):
        observaciones = self.cleaned_data.get("observaciones")
        validate_basic_text(
            observaciones,
            "Las observaciones solo pueden contener letras, números, espacios y los caracteres .,-!?()",
        )
        return observaciones


class AsignacionUpdateForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = [
            "articulo",
            "sede",
            "departamento",
            "cantidad",
            "descripcion",
            "observaciones",
        ]
        labels = {
            "articulo": "Artículo (Solo lectura)",
            "sede": "Sede",
            "departamento": "Departamento",
            "cantidad": "Cantidad",
            "descripcion": "Descripción",
            "observaciones": "Observaciones",
        }
        widgets = {
            "articulo": forms.Select(
                attrs={
                    "style": "pointer-events: none;",
                    "readonly": "readonly",
                    "placeholder": "Artículo seleccionado",
                }
            ),
            "sede": forms.Select(attrs={"placeholder": "Seleccione una sede"}),
            "departamento": forms.Select(
                attrs={"placeholder": "Seleccione un departamento"}
            ),
            "cantidad": forms.NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "descripcion": forms.TextInput(
                attrs={"placeholder": "Ingrese una descripción"}
            ),
            "observaciones": forms.TextInput(
                attrs={"placeholder": "Ingrese observaciones"}
            ),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        validate_cantidad(cantidad, "La cantidad tiene que ser un numero entero")
        return cantidad

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        validate_basic_text(
            descripcion,
            "La descripción solo puede contener letras, números, espacios y los caracteres .,-",
        )
        return descripcion

    def clean_observaciones(self):
        observaciones = self.cleaned_data.get("observaciones")
        validate_basic_text(
            observaciones,
            "Las observaciones solo pueden contener letras, números, espacios y los caracteres .,-!?()",
        )
        return observaciones
