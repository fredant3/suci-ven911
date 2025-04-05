from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)

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
)


class TipoSueldo(BaseModel):
    tipo = models.CharField("Tipo de Sueldo", max_length=21, choices=TIPO_CHOICES)
    monto = models.DecimalField("Monto Asignado", max_digits=10, decimal_places=2)
    descripcion = models.CharField(
        "Descripción Detallada",
        max_length=50,
        blank=True,
        null=True,
        validators=[MinLengthValidator(9), MaxLengthValidator(255), TextValidator()],
    )
    estatus = models.CharField("Estado Actual", max_length=3, choices=ESTATUS_CHOICES)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = "tipo de empleado"
        verbose_name_plural = "tipos de empleados"
        permissions = [
            ("listar_tipo_sueldos", "Listar tipos de sueldos"),
            ("agregar_tipo_sueldo", "Agregar tipos de sueldos"),
            ("ver_tipo_sueldo", "Ver tipos de sueldos"),
            ("modificar_tipo_sueldo", "Modificar tipos de sueldos"),
            ("eliminar_tipo_sueldo", "Eliminar tipos de sueldos"),
            ("exel_tipo_sueldo", "Exportar tipos de sueldos a excel"),
        ]
