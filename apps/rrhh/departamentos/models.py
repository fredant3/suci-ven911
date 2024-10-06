from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("ina", "Inactivo"),
    ("cer", "Cerrado"),
)


class Departamento(BaseModel):
    departamento = models.CharField(max_length=90)
    estatus = models.CharField(max_length=3, choices=ESTATUS_CHOICES)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.departamento

    class Meta:
        verbose_name = "departamento"
        verbose_name_plural = "departamentos"
