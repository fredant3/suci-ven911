from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("ina", "Inactivo"),
    ("inv", "Invalido"),
    ("cer", "Cerrado"),
)


class TipoEmpleado(BaseModel):
    tipo_personal = models.CharField(
        "Tipo de personal",
        max_length=60,
        validators=[MinLengthValidator(9), MaxLengthValidator(255), TextValidator()],
    )
    estatus = models.CharField("Estatus", max_length=3, choices=ESTATUS_CHOICES)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.tipo_personal

    class Meta:
        verbose_name = "tipo de empleado"
        verbose_name_plural = "tipos de empleados"
        permissions = [
            ("listar_tipo_empleados", "Listar tipos de empleados"),
            ("agregar_tipo_empleado", "Agregar tipos de empleados"),
            ("ver_tipo_empleado", "Ver tipos de empleados"),
            ("modificar_tipo_empleado", "Modificar tipos de empleados"),
            ("eliminar_tipo_empleado", "Eliminar tipos de empleados"),
            ("exel_tipo_empleado", "Exportar tipos de empleados a excel"),
        ]
