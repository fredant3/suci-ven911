from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Uri(BaseModel):
    nombre_apellido = models.CharField(
        "Nombre completo", max_length=120, blank=True, null=True
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Unidad de repuesta inmediata"
        verbose_name_plural = "Unidades de repuestas inmediatas"
