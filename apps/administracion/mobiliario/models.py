from django.db import models


class Mobiliario(models.Model):
    descripcion = models.TextField(
        max_length=64, verbose_name="Descripción:", default=""
    )
    marca = models.CharField(max_length=64, verbose_name="Marca:", default="")
    serial = models.CharField(max_length=64, verbose_name="Serial:", default="")
    cantidad = models.CharField(max_length=64, verbose_name="Cantidad:", default="")
    valor = models.CharField(max_length=64, verbose_name="Valor:", default="")
    condicion = models.CharField(max_length=64, verbose_name="Condición:", default="")
    ubicacion = models.CharField(max_length=64, verbose_name="Ubicación:", default="")
    fecha_adq = models.DateField(verbose_name="Fecha")
    garantia = models.CharField(max_length=64, verbose_name="Garantía:", default="")
    observaciones = models.TextField(
        max_length=64, verbose_name="Observaciones:", default=""
    )
    codigo_bn = models.CharField(max_length=64, verbose_name="Código BN:", default="")
