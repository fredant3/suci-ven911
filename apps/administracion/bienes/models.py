from django.db import models


class Bienes(models.Model):
    descripcion = models.TextField(
        max_length=64, verbose_name="Descripción:", default=""
    )
    marca = models.CharField(max_length=64, verbose_name="Marca:", default="")
    modelo = models.CharField(max_length=64, verbose_name="Modelo:", default="")
    serial = models.CharField(max_length=64, verbose_name="Serial:", default="")
    cantidad = models.CharField(max_length=64, verbose_name="Cantidad:", default="")
    asignado = models.CharField(max_length=64, verbose_name="Asignado:", default="")
    valor = models.CharField(max_length=64, verbose_name="Valor:", default="")
    condicion = models.CharField(max_length=64, verbose_name="Condición:", default="")
    ubicacion = models.CharField(max_length=64, verbose_name="Ubicación:", default="")
    fecha_adq = models.DateField(verbose_name="Fecha")
    garantia = models.DateField(max_length=64, verbose_name="Garantía:", default="")
