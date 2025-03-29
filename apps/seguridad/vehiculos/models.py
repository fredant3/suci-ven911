from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import UnicodeAlphaSpaceValidator, TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class Vehiculo(BaseModel):
    nombre = models.CharField(
        "Nombre",
        max_length=64,
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(255),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    apellido = models.CharField(
        "Apellido",
        max_length=64,
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(255),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    cedula = models.CharField("Cédula de identidad", max_length=64)
    modelo = models.CharField(
        "Modelo",
        max_length=64,
        validators=[MinLengthValidator(9), MaxLengthValidator(64), TextValidator()],
    )
    vehiculo = models.CharField(
        "Tipo de vehiculo",
        max_length=64,
        validators=[MinLengthValidator(9), MaxLengthValidator(64), TextValidator()],
    )
    motivo = models.CharField(
        "Motivo",
        max_length=64,
        validators=[MinLengthValidator(9), MaxLengthValidator(64), TextValidator()],
    )
    capagasolina = models.CharField("Capacidad de Gasolina", max_length=64)
    cantigasolina = models.CharField("Cantidad de Gasolina", max_length=64)
    placa = models.CharField("Placa", max_length=64)
    fecha = models.DateField("Fecha")
    hora = models.CharField("Hora", max_length=64)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.apellido)

    class Meta:
        verbose_name = "vehiculo"
        verbose_name_plural = "vehiculos"
        permissions = [
            ("listar_vehiculos", "Listar vehiculos"),
            ("agregar_vehiculo", "Agregar vehiculo"),
            ("ver_vehiculo", "Ver vehiculo"),
            ("modificar_vehiculo", "Modificar vehiculo"),
            ("eliminar_vehiculo", "Eliminar vehiculo"),
        ]
