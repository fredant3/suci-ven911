from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator, UnicodeAlphaSpaceValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class Asignacion(BaseModel):
    departamento = models.CharField(
        "Nombre de la dirección",
        max_length=64,
        validators=[MinLengthValidator(9), MaxLengthValidator(64), TextValidator()],
    )
    presupuesto = models.CharField("Presupuesto asignado", max_length=64)
    objetivo = models.CharField(
        "Objetivo general anual",
        max_length=64,
        validators=[MinLengthValidator(9), MaxLengthValidator(64), TextValidator()],
    )
    numero_partida = models.CharField(
        "Número de partida presupuestaria",
        max_length=10,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(10),
            UnicodeAlphaSpaceValidator(extra_chars="-"),
        ],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.numero_partida

    class Meta:
        verbose_name = "Asignacion"
        verbose_name_plural = "Asignaciones"
        permissions = [
            ("listar_asignar_presupuesto", "Puede listar asignaciones"),
            ("agregar_asignar_presupuesto", "Puede agregar asignacion"),
            ("ver_asignar_presupuesto", "Puede ver asignacion"),
            ("editar_asignar_presupuesto", "Puede actualizar asignacion"),
            ("eliminar_asignar_presupuesto", "Puede eliminar asignacion"),
            ("pdf_asignar_presupuesto", "Puede generar pdf de asignacion"),
        ]
