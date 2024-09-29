from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.models import Estado


class Infraestructura(BaseModel):
    mes = models.CharField(max_length=64, verbose_name="Mes:", default="")
    # estado = models.CharField(max_length=64, verbose_name="Estado:", default="")
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
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
