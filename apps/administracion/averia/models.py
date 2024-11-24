from administracion.departamentos.models import Departamento
from django.db import models
from helpers.BaseModelMixin import BaseModel
from users.auth.models import User


class TipoAveria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Averia(BaseModel):
    problema = models.TextField(max_length=255)
    tipo_averia = models.ForeignKey(TipoAveria, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    ubicacion = models.TextField(max_length=255)
    serial = models.CharField(max_length=255)
    codigo_bn = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.problema
