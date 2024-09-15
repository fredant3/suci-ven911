from django.db import models


class Averia(models.Model):
    bienes = models.TextField(max_length=64, verbose_name="Bienes:", default="")
    sintomas = models.CharField(max_length=64, verbose_name="Sintomas:", default="")
    departamento_ave = models.CharField(
        max_length=64, verbose_name="Departamento:", default=""
    )
    problema = models.CharField(max_length=64, verbose_name="Problema:", default="")
    condicion = models.CharField(max_length=64, verbose_name="Condición:", default="")
    ubicacion = models.CharField(max_length=64, verbose_name="Ubicación:", default="")
    codigo_bn = models.CharField(max_length=64, verbose_name="Código BN:", default="")
