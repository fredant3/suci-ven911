from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("rem", "Remodelacion"),
    ("cer", "Cerrada"),
)


class Sede(BaseModel):
    sede = models.CharField(max_length=30)
    estatus = models.CharField(max_length=3, choices=ESTATUS_CHOICES)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.sede

    class Meta:
        verbose_name = "sede"
        verbose_name_plural = "sedes"
