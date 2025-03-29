from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from rrhh.empleados.models import Empleado
from helpers.validForm import UnicodeAlphaSpaceValidator, TextValidator
from django.core.validators import (
    MinValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)


class Educacion(BaseModel):
    colegio = models.CharField(
        "Nombre del colegio",
        max_length=120,
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(120),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    codigo_titulo = models.CharField(
        "Código del Título",
        max_length=120,
        validators=[MinLengthValidator(9), MaxLengthValidator(120), TextValidator()],
    )
    titulo = models.CharField(
        "Titulo obtenido",
        max_length=120,
        validators=[MinLengthValidator(9), MaxLengthValidator(120), TextValidator()],
    )
    area_conocimiento = models.CharField(
        "Área de Conocimiento",
        max_length=120,
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(120),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    fecha_inicio = models.DateField("Fecha de inicio")
    fecha_culminacion = models.DateField("Fecha de culminacion")
    enlace_certificado = models.CharField(
        "Enlace al Certificado",
        max_length=120,
        null=True,
        blank=True,
        validators=[MinLengthValidator(9), MaxLengthValidator(120), TextValidator()],
    )
    empleado = models.ForeignKey(
        Empleado, on_delete=models.CASCADE, verbose_name="Empleado"
    )

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        verbose_name = "educacion"
        verbose_name_plural = "educaciones"
        permissions = [
            ("listar_educacion", "Puede listar educacion"),
            ("agregar_educacion", "Puede agregar educacion"),
            ("ver_educacion", "Puede ver educacion"),
            ("editar_educacion", "Puede actualizar educacion"),
            ("eliminar_educacion", "Puede eliminar educacion"),
            ("exel_educacion", "Puede exportar educacion a excel"),
        ]
