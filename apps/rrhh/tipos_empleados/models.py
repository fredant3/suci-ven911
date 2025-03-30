from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)
from django.core.exceptions import ValidationError

TIPO_PERSONAL_CHOICES = (
    ("per", "Permanente"),
    ("con", "Contrato"),
    ("int", "Internado"),
    ("est", "Estudiante"),
)

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("ina", "Inactivo"),
    ("inv", "Invalido"),
    ("cer", "Cerrado"),
)


class TipoEmpleado(BaseModel):
    tipo_personal = models.CharField(max_length=3, choices=TIPO_PERSONAL_CHOICES)
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

    class TipoEmpleado(models.Model):
        tipo_personal = models.CharField(max_length=255)
        estatus = models.CharField(max_length=255)

        def clean(self):
            combinaciones_validas = [
                ("per", "act"),
                ("per", "ina"),
            ]
            if (self.tipo_personal, self.estatus) not in combinaciones_validas:
                raise ValidationError(
                    "La combinación de tipo de personal y estatus no es válida."
                )
