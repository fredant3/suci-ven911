from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from rrhh.empleados.models import Empleado

TALLA_CAMISA_CHOICES = (
    ("XS", "Extra Pequena"),
    ("S", "Pequena"),
    ("M", "Mediana"),
    ("L", "Grande"),
    ("XL", "Extra Grande"),
)
TALLA_PANTALON_CHOICES = (
    ("8", "Extra Pequena (Dama)"),
    ("10", "Pequena (Dama)"),
    ("12", "Mediana (Dama)"),
    ("14", "Grande (Dama)"),
    ("16", "Extra Grande (Dama)"),
    ("18", "Super Grande (Dama)"),
    ("20", "Gigante (Dama)"),
    ("28", "Extra Pequena (Caballero)"),
    ("30", "Pequena (Caballero)"),
    ("32", "Mediana (Caballero)"),
    ("34", "Grande (Caballero)"),
    ("36", "Extra Grande (Caballero)"),
    ("38", "Super Grande (Caballero)"),
    ("40", "Gigante (Caballero)"),
    ("42", "Extra Gigante (Caballero)"),
)
TALLA_ZAPATO_CHOICES = (
    ("33", "Talla 33"),
    ("34", "Talla 34"),
    ("35", "Talla 35"),
    ("36", "Talla 36"),
    ("37", "Talla 37"),
    ("38", "Talla 38"),
    ("39", "Talla 39"),
    ("40", "Talla 40"),
    ("41", "Talla 41"),
    ("42", "Talla 42"),
    ("43", "Talla 43"),
    ("44", "Talla 44"),
    ("45", "Talla 45"),
    ("46", "Talla 46"),
)


class Dotacion(BaseModel):
    camisa = models.CharField(max_length=2, choices=TALLA_CAMISA_CHOICES)
    pantalon = models.CharField(max_length=2, choices=TALLA_PANTALON_CHOICES)
    zapato = models.CharField(max_length=2, choices=TALLA_ZAPATO_CHOICES)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.name, self.apellido)

    class Meta:
        verbose_name = "dotacion"
        verbose_name_plural = "dotaciones"
