from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import UnicodeAlphaSpaceValidator, TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class Gestion(BaseModel):
    name = models.CharField(
        "Nombre",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(255),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    apellido = models.CharField(
        "Apellido",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(255),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    cedula = models.CharField(
        "Cédula",
        max_length=64,
    )
    tipo = models.CharField(
        "Tipo de Gestión",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(255), TextValidator()],
    )
    descripcion = models.CharField(
        "Descripción",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(255), TextValidator()],
    )
    fecha = models.DateField("Fecha")
    direccion = models.CharField(
        "Dirección",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(255), TextValidator()],
    )
    cargo = models.CharField(
        "Cargo",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(255), TextValidator()],
    )
    hora = models.CharField(
        "Hora de Entrada",
        max_length=64,
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.name, self.apellido)

    class Meta:
        verbose_name = "gestion"
        verbose_name_plural = "gestiones"
        permissions = [
            ("listar_gestiones", "Listar gestiones"),
            ("agregar_gestion", "Agregar gestion"),
            ("ver_gestion", "Ver gestion"),
            ("modificar_gestion", "Modificar gestion"),
            ("eliminar_gestion", "Eliminar gestion"),
        ]
