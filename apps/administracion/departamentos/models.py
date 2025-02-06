from django.db import models
from helpers.BaseModelMixin import BaseModel


class Departamento(BaseModel):
    nombre = models.CharField(max_length=255)
    permissions = [
        ("listar_departamento", "Puede listar departamentos"),
        ("agregar_departamento", "Puede agregar departamento"),
        ("ver_departamento", "Puede ver departamento"),
        ("editar_departamento", "Puede actualizar departamento"),
        ("eliminar_departamento", "Puede eliminar departamento"),
    ]

    def __str__(self):
        return self.nombre
