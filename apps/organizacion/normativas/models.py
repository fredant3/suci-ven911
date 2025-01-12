from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Normativa(BaseModel):
    name = models.CharField("Nombre de Normativa", max_length=64)
    file = models.FileField("Archivo", upload_to="normativas/")
    user = models.CharField("Usuario", max_length=64)
    date = models.DateField("Fecha", blank=True)
    progre = models.CharField("Progreso", max_length=64)
    estado = models.BooleanField(default=False)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "normativa"
        verbose_name_plural = "normativas"
