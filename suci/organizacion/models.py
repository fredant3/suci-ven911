from django.db import models


# BASE DE DATOS DEL MODULO REGLAMENTOS
class Reglamentos(models.Model):
    name = models.CharField(
        max_length=64, verbose_name="Nombre de Reglamento:", default=""
    )
    file = models.FileField(
        upload_to="reglamentos/", verbose_name="Archivo", default=""
    )
    user = models.CharField(max_length=64, verbose_name="Usuario", default="")
    date = models.DateField(verbose_name="Fecha", blank=True)
    progre = models.CharField(max_length=64, verbose_name="Progreso:", default="")
    estado = models.BooleanField(default=False)


# BASE DE DATOS DEL MODULO NORMATIVAS
class Normativas(models.Model):
    name = models.CharField(
        max_length=64, verbose_name="Nombre de Normativa:", default=""
    )
    file = models.FileField(upload_to="normativas/", verbose_name="Archivo", default="")
    user = models.CharField(max_length=64, verbose_name="Usuario", default="")
    date = models.DateField(verbose_name="Fecha", blank=True)
    progre = models.CharField(max_length=64, verbose_name="Progreso:", default="")
    estado = models.BooleanField(default=False)
