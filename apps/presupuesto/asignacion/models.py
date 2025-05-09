from django.db.models import CharField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class Asignacion(BaseModel):
    departamento = CharField(
        "Nombre de la dirección",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(64), TextValidator()],
    )
    presupuesto = CharField("Presupuesto asignado", max_length=64)
    objetivo = CharField(
        "Objetivo general anual",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(64), TextValidator()],
    )
    numero_partida = CharField(
        "Número de partida presupuestaria",
        max_length=10,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(10),
            TextValidator(extra_chars="-"),
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
