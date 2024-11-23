from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel

TIPO_CHOICES = (
    ("ticket", "Cesta Ticket"),
    ("guerra", "Bono de Guerra"),
    ("discapacidad", "Prima por discapacidad"),
    ("menor_12", "Prima por dependecias menores de 12"),
    ("hijos_13_18", "Prima por dependecias menores de 13 a 18"),
    ("hijos_discapacidad", "Prima por dependecias menores con discapacidad"),
    ("profesionalismo", "Prima por Profesionalismo"),
    ("minimo", "Sueldo Minimo"),
)

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("sup", "Suspendido"),
    ("des", "Desactivado"),
)


class TipoSueldo(BaseModel):
    tipo = models.CharField(max_length=21, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    estatus = models.CharField(max_length=3, choices=ESTATUS_CHOICES)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.tipo_personal

    class Meta:
        verbose_name = "tipo de empleado"
        verbose_name_plural = "tipos de empleados"
