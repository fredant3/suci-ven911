from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Objetivo(BaseModel):
    fechai = models.DateField(verbose_name="Fecha de Inicio")
    fechaf = models.DateField(verbose_name="Fecha Final")
    objetiv = models.CharField(max_length=64, verbose_name="Objetivos:", default="")
    meta = models.CharField(max_length=64, verbose_name="Meta:", default="")
    permissions = [
        ("listar_objetivo", "Puede listar objetivos"),
        ("agregar_objetivo", "Puede agregar objetivo"),
        ("ver_objetivo", "Puede ver objetivo"),
        ("editar_objetivo", "Puede actualizar objetivo"),
        ("eliminar_objetivo", "Puede eliminar objetivo"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.ente

    class Meta:
        verbose_name = "objetivo"
        verbose_name_plural = "objetivos"
