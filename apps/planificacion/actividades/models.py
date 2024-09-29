from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Actividad(BaseModel):
    fechai = models.DateField(verbose_name="Fecha de Inicio")
    fechaf = models.DateField(verbose_name="Fecha Final")
    objetiv = models.CharField(max_length=64, verbose_name="Objetivos:", default="")
    meta = models.CharField(max_length=64, verbose_name="Meta:", default="")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.ente

    class Meta:
        verbose_name = "actividad"
        verbose_name_plural = "actividades"
