from administracion.inventario.models import Articulo
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_basic_text,
    validate_basic_text,
    validate_basic_text,
    validate_serial,
    validate_placa,
    validate_decimal_number,
    validate_codigo_bn,
    validate_cantidad,
    validate_basic_text,
)
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
        labels = {
            "descripcion": "Descripción",
            "marca": "Marca",
            "modelo": "Modelo",
            "serial": "Serial",
            "placa": "Placa",
            "cantidad_combustible": "Cantidad de combustible máx. En litros",
            "codigo_bn": "Código BN",
            "cantidad": "Cantidad",
            "condicion": "Condición",
            "fecha_adq": "Fecha de adquisición",
        }
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
            "condicion": forms.TextInput(attrs={"placeholder": "Ingrese la condición"}),
            "fecha_adq": forms.DateInput(
                attrs={"placeholder": "Seleccione la fecha de adquisición"}
            ),
        }

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        validate_basic_text(
            descripcion,
            "La descripción solo puede contener letras, números y espacios.",
        )
        return descripcion

    def clean_marca(self):
        marca = self.cleaned_data.get("marca")
        validate_basic_text(
            marca, "La marca solo puede contener letras, números y espacios."
        )
        return marca

    def clean_modelo(self):
        modelo = self.cleaned_data.get("modelo")
        validate_basic_text(
            modelo, "El modelo solo puede contener letras, números y espacios."
        )
        return modelo

    def clean_serial(self):
        serial = self.cleaned_data.get("serial")
        validate_serial(
            serial, "El serial solo puede contener letras, números y guiones."
        )
        return serial

    def clean_placa(self):
        placa = self.cleaned_data.get("placa")
        validate_placa(placa, "La placa solo puede contener letras, números y guiones.")
        return placa

    def clean_cantidad_combustible(self):
        cantidad_combustible = self.cleaned_data.get("cantidad_combustible")
        validate_decimal_number(
            cantidad_combustible,
            "La cantidad de combustible debe ser un número positivo.",
        )
        return cantidad_combustible

    def clean_codigo_bn(self):
        codigo_bn = self.cleaned_data.get("codigo_bn")
        validate_codigo_bn(
            codigo_bn, "El código BN solo puede contener letras, números y guiones."
        )
        return codigo_bn

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        validate_cantidad(cantidad, "La cantidad debe ser un número entero positivo.")
        return cantidad

    def clean_condicion(self):
        condicion = self.cleaned_data.get("condicion")
        validate_basic_text(
            condicion, "La condición solo puede contener letras, números y espacios."
        )
        return condicion


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
        labels = {
            "descripcion": "Descripción",
            "marca": "Marca",
            "modelo": "Modelo",
            "serial": "Serial",
            "codigo_bn": "Código BN",
            "cantidad": "Cantidad",
            "condicion": "Condición",
        }
        widgets = {
            "descripcion": forms.TextInput(
                attrs={"placeholder": "Ingrese la descripción"}
            ),
            "marca": forms.TextInput(attrs={"placeholder": "Ingrese la marca"}),
            "modelo": forms.TextInput(attrs={"placeholder": "Ingrese el modelo"}),
            "serial": forms.TextInput(attrs={"placeholder": "Ingrese el serial"}),
            "codigo_bn": forms.TextInput(attrs={"placeholder": "Ingrese el código BN"}),
            "cantidad": forms.NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "condicion": forms.TextInput(attrs={"placeholder": "Ingrese la condición"}),
            "fecha_adq": forms.DateInput(
                attrs={
                    "placeholder": "Seleccione la fecha de adquisición",
                }
            ),
        }

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        validate_basic_text(
            descripcion,
            "La descripción solo puede contener letras, números y espacios.",
        )
        return descripcion

    def clean_marca(self):
        marca = self.cleaned_data.get("marca")
        validate_basic_text(
            marca, "La marca solo puede contener letras, números y espacios."
        )
        return marca

    def clean_modelo(self):
        modelo = self.cleaned_data.get("modelo")
        validate_basic_text(
            modelo, "El modelo solo puede contener letras, números y espacios."
        )
        return modelo

    def clean_serial(self):
        serial = self.cleaned_data.get("serial")
        validate_serial(
            serial, "El serial solo puede contener letras, números y guiones."
        )
        return serial

    def clean_codigo_bn(self):
        codigo_bn = self.cleaned_data.get("codigo_bn")
        validate_codigo_bn(
            codigo_bn, "El código BN solo puede contener letras, números y guiones."
        )
        return codigo_bn

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        validate_cantidad(cantidad, "La cantidad debe ser un número entero positivo.")
        return cantidad

    def clean_condicion(self):
        condicion = self.cleaned_data.get("condicion")
        validate_basic_text(
            condicion, "La condición solo puede contener letras, números y espacios."
        )
        return condicion


class ConsumibleForm(FormBase):
    fecha_adq = FormBase.create_date_field("fecha_adq", title="Fecha de adquisición")

    class Meta:
        model = Articulo
        fields = ["descripcion", "marca", "serial", "cantidad", "fecha_adq"]
        labels = {
            "descripcion": "Descripción",
            "marca": "Marca",
            "serial": "Serial",
            "cantidad": "Cantidad",
        }
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

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        validate_basic_text(
            descripcion,
            "La descripción solo puede contener letras, números y espacios.",
        )
        return descripcion

    def clean_marca(self):
        marca = self.cleaned_data.get("marca")
        validate_basic_text(
            marca, "La marca solo puede contener letras, números y espacios."
        )
        return marca

    def clean_serial(self):
        serial = self.cleaned_data.get("serial")
        validate_serial(
            serial, "El serial solo puede contener letras, números y guiones."
        )
        return serial

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        validate_cantidad(cantidad, "La cantidad debe ser un número entero positivo.")
        return cantidad


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
        labels = {
            "descripcion": "Descripción",
            "serial": "Serial",
            "codigo_bn": "Código BN",
            "cantidad": "Cantidad",
            "condicion": "Condición",
        }
        widgets = {
            "descripcion": forms.TextInput(
                attrs={"placeholder": "Ingrese la descripción"}
            ),
            "serial": forms.TextInput(attrs={"placeholder": "Ingrese el serial"}),
            "codigo_bn": forms.TextInput(attrs={"placeholder": "Ingrese el código BN"}),
            "cantidad": forms.NumberInput(attrs={"placeholder": "Ingrese la cantidad"}),
            "condicion": forms.TextInput(attrs={"placeholder": "Ingrese la condición"}),
            "fecha_adq": forms.DateInput(
                attrs={"placeholder": "Seleccione la fecha de adquisición"}
            ),
        }

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        validate_basic_text(
            descripcion,
            "La descripción solo puede contener letras, números y espacios.",
        )
        return descripcion

    def clean_serial(self):
        serial = self.cleaned_data.get("serial")
        validate_serial(
            serial, "El serial solo puede contener letras, números y guiones."
        )
        return serial

    def clean_codigo_bn(self):
        codigo_bn = self.cleaned_data.get("codigo_bn")
        validate_codigo_bn(
            codigo_bn, "El código BN solo puede contener letras, números y guiones."
        )
        return codigo_bn

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        validate_cantidad(cantidad, "La cantidad debe ser un número entero positivo.")
        return cantidad

    def clean_condicion(self):
        condicion = self.cleaned_data.get("condicion")
        validate_basic_text(
            condicion, "La condición solo puede contener letras, números y espacios."
        )
        return condicion


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
        labels = {
            "descripcion": "Descripción",
            "marca": "Marca",
            "modelo": "Modelo",
            "placa": "Placa",
            "cantidad_combustible": "Cantidad de combustible máx. En litros",
            "codigo_bn": "Código BN",
            "cantidad": "Cantidad",
            "condicion": "Condición",
        }
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
            "condicion": forms.TextInput(attrs={"placeholder": "Ingrese la condición"}),
            "fecha_adq": forms.DateInput(
                attrs={"placeholder": "Seleccione la fecha de adquisición"}
            ),
        }

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        validate_basic_text(
            descripcion,
            "La descripción solo puede contener letras, números y espacios.",
        )
        return descripcion

    def clean_marca(self):
        marca = self.cleaned_data.get("marca")
        validate_basic_text(
            marca, "La marca solo puede contener letras, números y espacios."
        )
        return marca

    def clean_modelo(self):
        modelo = self.cleaned_data.get("modelo")
        validate_basic_text(
            modelo, "El modelo solo puede contener letras, números y espacios."
        )
        return modelo

    def clean_placa(self):
        placa = self.cleaned_data.get("placa")
        validate_placa(placa, "La placa solo puede contener letras, números y guiones.")
        return placa

    def clean_cantidad_combustible(self):
        cantidad_combustible = self.cleaned_data.get("cantidad_combustible")
        validate_decimal_number(
            cantidad_combustible,
            "La cantidad de combustible debe ser un número positivo.",
        )
        return cantidad_combustible

    def clean_codigo_bn(self):
        codigo_bn = self.cleaned_data.get("codigo_bn")
        validate_codigo_bn(
            codigo_bn, "El código BN solo puede contener letras, números y guiones."
        )
        return codigo_bn

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        validate_cantidad(cantidad, "La cantidad debe ser un número entero positivo.")
        return cantidad

    def clean_condicion(self):
        condicion = self.cleaned_data.get("condicion")
        validate_basic_text(
            condicion, "La condición solo puede contener letras, números y espacios."
        )
        return condicion
