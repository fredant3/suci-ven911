from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Reglamento(BaseModel):
    name = models.CharField(
        max_length=64, verbose_name="Nombre de Reglamento:", default=""
    )
    file = models.FileField(
        upload_to="reglamentos/", verbose_name="Archivo", default=""
    )
    user = models.CharField(max_length=64, verbose_name="Usuario", default="")
    date = models.DateField(verbose_name="Fecha", blank=True)
    progre = models.CharField(max_length=64, verbose_name="Progreso:", default="")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "reglamento"
        verbose_name_plural = "reglamentos"
