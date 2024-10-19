from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("ina", "Inactivo"),
    ("inv", "Invalido"),
    ("cer", "Cerrado"),
)


class TipoEmpleado(BaseModel):
    tipo_personal = models.CharField(max_length=60)
    estatus = models.CharField(max_length=3, choices=ESTATUS_CHOICES)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.tipo_personal

    class Meta:
        verbose_name = "tipo de empleado"
        verbose_name_plural = "tipos de empleados"