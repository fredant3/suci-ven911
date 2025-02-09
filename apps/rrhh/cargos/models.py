from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("ina", "Inactivo"),
    ("inv", "Invalido"),
    ("cer", "Cerrado"),
)


class Cargo(BaseModel):
    cargo = models.CharField(max_length=60)
    estatus = models.CharField(max_length=3, choices=ESTATUS_CHOICES)
    permissions = [
        ("listar_cargo", "Puede listar cargos"),
        ("agregar_cargo", "Puede agregar cargo"),
        ("ver_cargo", "Puede ver cargo"),
        ("editar_cargo", "Puede actualizar cargo"),
        ("eliminar_cargo", "Puede eliminar cargo"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.cargo

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
