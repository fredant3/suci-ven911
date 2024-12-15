from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Infraestructura(BaseModel):
    mes = models.CharField(max_length=64, verbose_name="Mes:", default="")
    estado = models.CharField(max_length=120, verbose_name="Estado:")
    infraestructura = models.CharField(
        max_length=64, verbose_name="Infraestrutuctura:", default=""
    )
    cantidad = models.CharField(max_length=64, verbose_name="Cantidad:", default="")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.ente

    class Meta:
        verbose_name = "infraestructura"
        verbose_name_plural = "infraestructuras"
