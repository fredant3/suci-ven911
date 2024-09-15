from django.db import models


class Asignacion(models.Model):
    inventario = models.CharField(max_length=64, verbose_name="Inventario:", default="")
    departamento = models.CharField(
        max_length=64, verbose_name="Departamento:", default=""
    )
    descripcion = models.CharField(
        max_length=64, verbose_name="Descripción:", default=""
    )
    articulo = models.CharField(max_length=64, verbose_name="Articulo:", default="")
    cantidad = models.CharField(max_length=64, verbose_name="Cantidad:", default="")
    observaciones = models.CharField(
        max_length=64, verbose_name="Observaciones:", default=""
    )
