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


class Salida(BaseModel):
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
    cedula = models.CharField("Cédula:", max_length=64)
    telefono = models.CharField(
        "Teléfono:",
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
        verbose_name = "salida"
        verbose_name_plural = "salidas"
        permissions = [
            ("listar_salidas", "Listar salidas"),
            ("agregar_salida", "Agregar salida"),
            ("ver_salida", "Ver salida"),
            ("modificar_salida", "Modificar salida"),
            ("eliminar_salida", "Eliminar salida"),
        ]
