from django.db import models


class Consumible(models.Model):
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
    observaciones = models.TextField(
        max_length=64, verbose_name="Observaciones:", default=""
    )
