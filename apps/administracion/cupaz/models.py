from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class CuadrantePaz(BaseModel):
    nombre = models.CharField(max_length=180)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "cuadrante de paz"
        verbose_name_plural = "cuadrantes de paz"
