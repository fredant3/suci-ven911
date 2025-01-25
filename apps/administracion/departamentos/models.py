from django.db import models
from helpers.BaseModelMixin import BaseModel


class Departamento(BaseModel):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
