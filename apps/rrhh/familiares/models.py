from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.models import ESTADO_CIVIL_CHOICES, GENERO_CHOICES
from rrhh.empleados.models import Empleado

PARENTEZCO = (
    ("hermano", "Hermana|Hermano"),
    ("pareja", "Conyugue"),
    ("mama", "Madre"),
    ("papa", "Padre"),
    ("hijo", "Hija|Hijo"),
)
TIPO_HIJO = (
    ("menor_12", "Hijo menor de 12"),
    ("hijos_13_18", "Hijo entre 13 y 18"),
    ("mayor_18", "Hijo mayor de 18"),
)


class Familiar(BaseModel):
    parentezco = models.CharField(max_length=7, choices=PARENTEZCO)
    tipo_hijo = models.CharField(
        max_length=11, choices=TIPO_HIJO, null=True, blank=True
    )
    discapacidad = models.BooleanField(default=False)
    nombres = models.CharField(max_length=90)
    apellidos = models.CharField(max_length=90)
    cedula = models.IntegerField(null=True, blank=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=GENERO_CHOICES)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=150, blank=True, null=True)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.name, self.apellido)

    class Meta:
        verbose_name = "familiar"
        verbose_name_plural = "familiares"
