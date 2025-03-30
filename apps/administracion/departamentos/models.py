from django.db import models
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import UnicodeAlphaSpaceValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class Departamento(BaseModel):
    nombre = models.CharField(
        "Departamento",
        max_length=30,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(30),
            UnicodeAlphaSpaceValidator(),
        ],
    )

    class Meta:
        permissions = [
            ("listar_departamento", "Puede listar departamentos"),
            ("agregar_departamento", "Puede agregar departamentos"),
            ("ver_departamento", "Puede ver detalles de departamentos"),
            ("editar_departamento", "Puede editar departamentos"),
            ("eliminar_departamento", "Puede eliminar departamentos"),
        ]

    def __str__(self):
        return self.nombre
