from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES


class Llamada(BaseModel):
    mes = models.CharField(max_length=64, verbose_name="Mes:", default="")
    estado = models.CharField(
        "Estado", name="estado", max_length=2, choices=ESTADOS_CHOICES
    )
    informativa = models.CharField(
        max_length=64, verbose_name="Informativa:", default=""
    )
    falsa = models.CharField(max_length=64, verbose_name="Falsa:", default="")
    realesno = models.CharField(
        max_length=64, verbose_name="Reales no Efectivas:", default=""
    )
    realesf = models.CharField(
        max_length=64, verbose_name="Reales Efectivas:", default=""
    )
    videop = models.CharField(
        max_length=64, verbose_name="Video Protección:", default=""
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.ente

    class Meta:
        verbose_name = "llamada"
        verbose_name_plural = "llamadas"
