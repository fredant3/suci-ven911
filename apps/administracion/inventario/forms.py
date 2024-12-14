from administracion.inventario.models import Articulo
from django import forms


class ArticuloForm(forms.ModelForm):
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
            # "tipo_articulo",
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
            # "tipo_articulo": "Tipo de artículo",
        }
        widgets = {
            "fecha_adq": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Selecciona una fecha", "type": "date"},
            ),
        }


class TecnologiaForm(forms.ModelForm):
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
            "fecha_adq": "Fecha de adquisición",
        }
        widgets = {
            "fecha_adq": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Selecciona una fecha", "type": "date"},
            ),
        }


class ConsumibleForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ["descripcion", "marca", "serial", "cantidad", "fecha_adq"]
        labels = {
            "descripcion": "Descripción",
            "marca": "Marca",
            "serial": "Serial",
            "cantidad": "Cantidad",
            "fecha_adq": "Fecha de adquisición",
        }
        widgets = {
            "fecha_adq": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Selecciona una fecha", "type": "date"},
            ),
        }


class MobiliarioForm(forms.ModelForm):
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
            "fecha_adq": "Fecha de adquisición",
        }
        widgets = {
            "fecha_adq": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Selecciona una fecha", "type": "date"},
            ),
        }


class VehiculoForm(forms.ModelForm):
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
            "fecha_adq": "Fecha de adquisición",
        }
        widgets = {
            "fecha_adq": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Selecciona una fecha", "type": "date"},
            ),
        }
