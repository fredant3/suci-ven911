from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import (
    UnicodeAlphaSpaceValidator,
    TextValidator,
    PhoneNumberValidator,
)
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class Entrada(BaseModel):
    name = models.CharField(
        "Nombre",
        max_length=64,
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(64),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    apellido = models.CharField(
        "Apellido",
        max_length=64,
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(64),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    cedula = models.CharField("Cédula", max_length=64)
    telefono = models.CharField(
        "Teléfono",
        max_length=20,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(20),
            PhoneNumberValidator(),
        ],
    )
    fecha = models.DateField("Fecha")
    direccion = models.CharField(
        "Dirección",
        max_length=64,
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )
    cargo = models.CharField("Cargo", max_length=64)
    hora = models.CharField("Hora de Entrada", max_length=64)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.name, self.apellido)

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        permissions = [
            ("listar_entradas", "Listar entradas"),
            ("agregar_entrada", "Agregar entrada"),
            ("ver_entrada", "Ver entrada"),
            ("modificar_entrada", "Modificar entrada"),
            ("eliminar_entrada", "Eliminar entrada"),
        ]
