from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import (
    PositiveIntegerValidator,
    TextValidator,
    UnicodeAlphaSpaceValidator,
)
from django.core.validators import (
    MinValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)


class Receptor(BaseModel):
    idr = models.CharField(
        "Identificador Receptor",
        max_length=100,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(100),
            UnicodeAlphaSpaceValidator(extra_chars="-"),
        ],
    )
    partidar = models.CharField(
        "Partida Contable",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
            UnicodeAlphaSpaceValidator(extra_chars="-"),
        ],
    )
    generalr = models.CharField(
        "General",
        max_length=64,
        validators=[
            MinValueValidator(100),
            MinLengthValidator(3),
            MaxLengthValidator(64),
            PositiveIntegerValidator(),
        ],
    )
    espefr = models.CharField(
        "Específicaciones",
        max_length=64,
        validators=[
            MinValueValidator(100),
            MinLengthValidator(3),
            MaxLengthValidator(64),
            PositiveIntegerValidator(),
        ],
    )
    subespefr = models.CharField(
        "Sub-Especialidad",
        max_length=64,
        validators=[
            MinValueValidator(100),
            MinLengthValidator(3),
            MaxLengthValidator(64),
            PositiveIntegerValidator(),
        ],
    )
    denomr = models.CharField(
        "Denomincación",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )
    presuacorr = models.CharField(
        "Presupuesto acordado",
        max_length=64,
    )
    caufechar = models.CharField(
        "Causado a la fecha",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )
    dispr = models.CharField(
        "Disponible a causar",
        max_length=64,
    )
    montocr = models.CharField(
        "Monto a ceder",
        max_length=64,
    )
    saldofr = models.CharField(
        "Saldo final",
        max_length=64,
    )
    direccionr = models.CharField(
        "Dirección cedente",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.partidar, self.generalr)

    class Meta:
        verbose_name = "Receptor"
        verbose_name_plural = "Receptores"
        permissions = [
            ("listar_receptor", "Puede listar receptor"),
            ("agregar_receptor", "Puede agregar receptor"),
            ("ver_receptor", "Puede ver receptor"),
            ("editar_receptor", "Puede actualizar receptor"),
            ("eliminar_receptor", "Puede eliminar receptor"),
            ("pdf_receptor", "Puede generar pdf de receptor"),
        ]
