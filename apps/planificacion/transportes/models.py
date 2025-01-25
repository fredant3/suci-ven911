from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES


class Transporte(BaseModel):
    mes = models.CharField(max_length=64, verbose_name="Mes:", default="")
    estado = models.CharField(
        "Estado", name="estado", max_length=2, choices=ESTADOS_CHOICES
    )
    transporte = models.CharField(max_length=64, verbose_name="Transporte:", default="")
    cantidad = models.CharField(max_length=64, verbose_name="Cantidad:", default="")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.ente

    class Meta:
        verbose_name = "transporte"
        verbose_name_plural = "transportes"
