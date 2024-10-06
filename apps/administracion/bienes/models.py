from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel

from apps.administracion.departamentos.models import Departamento
from apps.administracion.sedes.models import Sede

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("ina", "Inactivo"),
)
CONDICION_CHOICES = (
    ("nuevo", "Nuevo"),
    ("usado", "Usado"),
)


class Bien(BaseModel):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    marca = models.CharField(
        max_length=90, verbose_name="Marca:", null=True, blank=True
    )
    modelo = models.CharField(
        max_length=90, verbose_name="Modelo:", null=True, blank=True
    )
    serial = models.CharField(
        max_length=90, verbose_name="Serial:", null=True, blank=True
    )
    descripcion = models.TextField(
        max_length=120, verbose_name="Descripción:", null=True, blank=True
    )
    cantidad = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_adquirido = models.DateField(verbose_name="Fecha de adquisición")
    condicion = models.CharField(
        max_length=5, choices=CONDICION_CHOICES, verbose_name="Condición"
    )
    garantia = models.DateField(
        max_length=60, verbose_name="Garantía", null=True, blank=True
    )
    estatus = models.CharField(max_length=3, choices=ESTATUS_CHOICES)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "bien"
        verbose_name_plural = "bienes"
