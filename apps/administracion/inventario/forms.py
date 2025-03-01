from administracion.inventario.models import Articulo
from helpers.FormBase import FormBase


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
            "cantidad",  # Asegúrate de que esta línea esté alineada correctamente
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


class TecnologiaForm(FormBase):
    fecha_adq = FormBase.create_date_field("fecha_adq")

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


class ConsumibleForm(FormBase):
    fecha_adq = FormBase.create_date_field("fecha_adq")

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


class MobiliarioForm(FormBase):
    fecha_adq = FormBase.create_date_field("fecha_adq")

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


class VehiculoForm(FormBase):
    fecha_adq = FormBase.create_date_field("fecha_adq")

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
