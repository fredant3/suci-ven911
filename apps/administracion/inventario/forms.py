from administracion.inventario.models import Articulo
from helpers.FormBase import FormBase
from helpers.validForm import validate_decimal_number
from django import forms


class ArticuloForm(FormBase):
    fecha_adq = FormBase.create_date_field("fecha_adq")

    class Meta:
        model = Articulo
        fields = [
            "descripcion",
            "marca",
            "modelo",
            "serial",
            "placa",
            "cantidad_combustible",
            "codigo_bn",
            "cantidad",
            "condicion",
            "fecha_adq",
        ]
        widgets = {
            "descripcion": forms.TextInput(
                attrs={"placeholder": "Ingrese la descripción"}
            ),
            "marca": forms.TextInput(attrs={"placeholder": "Ingrese la marca"}),
            "modelo": forms.TextInput(attrs={"placeholder": "Ingrese el modelo"}),
            "serial": forms.TextInput(attrs={"placeholder": "Ingrese el serial"}),
            "placa": forms.TextInput(attrs={"placeholder": "Ingrese la placa"}),
            "cantidad_combustible": forms.NumberInput(
                attrs={"placeholder": "Ingrese la cantidad de combustible"}
            ),
            "codigo_bn": forms.TextInput(attrs={"placeholder": "Ingrese el código BN"}),
            "cantidad": forms.NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "condicion": forms.Select(attrs={"placeholder": "Ingrese la condición"}),
            "fecha_adq": forms.DateInput(
                attrs={"placeholder": "Seleccione la fecha de adquisición"}
            ),
        }

    def clean_cantidad_combustible(self):
        cantidad_combustible = self.cleaned_data.get("cantidad_combustible")
        validate_decimal_number(
            cantidad_combustible,
            "La cantidad de combustible debe ser un número positivo.",
        )
        return cantidad_combustible


class TecnologiaForm(FormBase):
    fecha_adq = FormBase.create_date_field("fecha_adq", title="Fecha de adquisición")

    class Meta:
        model = Articulo
        fields = [
            "descripcion",
            "marca",
            "modelo",
            "serial",
            "codigo_bn",
            "cantidad",
            "condicion",
            "fecha_adq",
        ]
        widgets = {
            "descripcion": forms.TextInput(
                attrs={"placeholder": "Ingrese la descripción"}
            ),
            "marca": forms.TextInput(attrs={"placeholder": "Ingrese la marca"}),
            "modelo": forms.TextInput(attrs={"placeholder": "Ingrese el modelo"}),
            "serial": forms.TextInput(attrs={"placeholder": "Ingrese el serial"}),
            "codigo_bn": forms.TextInput(attrs={"placeholder": "Ingrese el código BN"}),
            "cantidad": forms.NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "condicion": forms.Select(attrs={"placeholder": "Ingrese la condición"}),
            "fecha_adq": forms.DateInput(
                attrs={
                    "placeholder": "Seleccione la fecha de adquisición",
                }
            ),
        }


class ConsumibleForm(FormBase):
    fecha_adq = FormBase.create_date_field("fecha_adq", title="Fecha de adquisición")

    class Meta:
        model = Articulo
        fields = ["descripcion", "marca", "serial", "cantidad", "fecha_adq"]
        widgets = {
            "descripcion": forms.TextInput(
                attrs={"placeholder": "Ingrese la descripción"}
            ),
            "marca": forms.TextInput(attrs={"placeholder": "Ingrese la marca"}),
            "serial": forms.TextInput(attrs={"placeholder": "Ingrese el serial"}),
            "cantidad": forms.NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "fecha_adq": forms.DateInput(
                attrs={"placeholder": "Seleccione la fecha de adquisición"}
            ),
        }


class MobiliarioForm(FormBase):
    fecha_adq = FormBase.create_date_field("fecha_adq", title="Fecha de adquisición")

    class Meta:
        model = Articulo
        fields = [
            "descripcion",
            "serial",
            "codigo_bn",
            "cantidad",
            "condicion",
            "fecha_adq",
        ]
        widgets = {
            "descripcion": forms.TextInput(
                attrs={"placeholder": "Ingrese la descripción"}
            ),
            "serial": forms.TextInput(attrs={"placeholder": "Ingrese el serial"}),
            "codigo_bn": forms.TextInput(attrs={"placeholder": "Ingrese el código BN"}),
            "cantidad": forms.NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "condicion": forms.Select(attrs={"placeholder": "Ingrese la condición"}),
            "fecha_adq": forms.DateInput(
                attrs={"placeholder": "Seleccione la fecha de adquisición"}
            ),
        }


class VehiculoForm(FormBase):
    fecha_adq = FormBase.create_date_field("fecha_adq", title="Fecha de adquisición")

    class Meta:
        model = Articulo
        fields = [
            "descripcion",
            "marca",
            "modelo",
            "placa",
            "cantidad_combustible",
            "codigo_bn",
            "cantidad",
            "condicion",
            "fecha_adq",
        ]
        widgets = {
            "descripcion": forms.TextInput(
                attrs={"placeholder": "Ingrese la descripción"}
            ),
            "marca": forms.TextInput(attrs={"placeholder": "Ingrese la marca"}),
            "modelo": forms.TextInput(attrs={"placeholder": "Ingrese el modelo"}),
            "placa": forms.TextInput(attrs={"placeholder": "Ingrese la placa"}),
            "cantidad_combustible": forms.NumberInput(
                attrs={"placeholder": "Ingrese la cantidad de combustible"}
            ),
            "codigo_bn": forms.TextInput(attrs={"placeholder": "Ingrese el código BN"}),
            "cantidad": forms.NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "condicion": forms.Select(attrs={"placeholder": "Ingrese la condición"}),
            "fecha_adq": forms.DateInput(
                attrs={"placeholder": "Seleccione la fecha de adquisición"}
            ),
        }

    def clean_cantidad_combustible(self):
        cantidad_combustible = self.cleaned_data.get("cantidad_combustible")
        validate_decimal_number(
            cantidad_combustible,
            "La cantidad de combustible debe ser un número positivo.",
        )
        return cantidad_combustible
