from django.db import models


class Compras(models.Model):
    producto = models.TextField(max_length=64, verbose_name="Producto:", default="")
    serial = models.CharField(max_length=64, verbose_name="Serial:", default="")
    marca = models.CharField(max_length=64, verbose_name="Marca:", default="")
    modelo = models.CharField(max_length=64, verbose_name="Modelo:", default="")
    fecha_adq = models.DateField(verbose_name="Fecha")
    numero_orden = models.CharField(
        max_length=64, verbose_name="Número de orden:", default=""
    )
    valor = models.CharField(max_length=64, verbose_name="Valor:", default="")
    cantidad = models.CharField(max_length=64, verbose_name="Cantidad:", default="")
    proveedor = models.CharField(max_length=64, verbose_name="Proveedor:", default="")
    ubicacion = models.CharField(max_length=64, verbose_name="Ubicación:", default="")
    garantia = models.CharField(max_length=64, verbose_name="Garantía:", default="")
