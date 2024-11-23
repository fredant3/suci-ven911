from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Asignacion(BaseModel):
    nombredir = models.CharField(max_length=64, verbose_name="Nombre de la dirección:")
    presuasig = models.CharField(max_length=64, verbose_name="Presupuesto asignado:")
    objeanual = models.CharField(max_length=64, verbose_name="Objetivo general anual:")
    numpartida = models.CharField(max_length=10, verbose_name="Número de partida:")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.numpartida

    class Meta:
        verbose_name = "Asignacion"
        verbose_name_plural = "Asignaciones"
