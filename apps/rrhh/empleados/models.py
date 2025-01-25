from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.models import (
    ESTADO_CIVIL_CHOICES,
    GENERO_CHOICES,
    NACIONALIDAD_CHOICES,
    TIPO_SANGRE_CHOICES,
)

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("vac", "En vacaciones"),
    ("sus", "Suspendido"),
    ("des", "Se despedio"),
    ("ren", "Ha renunciado"),
)


class Empleado(BaseModel):
    estatus = models.CharField(max_length=3, choices=ESTATUS_CHOICES)
    nombres = models.CharField(max_length=90)
    apellidos = models.CharField(max_length=90)
    nacionalidad = models.CharField(max_length=2, choices=NACIONALIDAD_CHOICES)
    cedula = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=GENERO_CHOICES)
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)
    tipo_sangre = models.CharField(max_length=3, choices=TIPO_SANGRE_CHOICES)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=180)
    estudia = models.BooleanField()
    discapacitado = models.BooleanField()
    contratos = models.IntegerField()

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = "empleados"
