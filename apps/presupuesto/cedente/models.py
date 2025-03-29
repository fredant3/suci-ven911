from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import (
    TextValidator,
    UnicodeAlphaSpaceValidator,
    PositiveIntegerValidator,
)
from django.core.validators import (
    MinValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)


class Cedente(BaseModel):
    idc = models.CharField(
        "Identificador Cedente:",
        max_length=100,
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(255),
            UnicodeAlphaSpaceValidator(extra_chars="-"),
        ],
    )
    partidac = models.CharField(
        "Partida Contable",
        max_length=64,
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(255),
            UnicodeAlphaSpaceValidator(extra_chars="-"),
        ],
    )
    generalc = models.CharField(
        "General",
        max_length=64,
        validators=[
            MinValueValidator(1),
            MaxLengthValidator(255),
            PositiveIntegerValidator(),
        ],
    )
    espefc = models.CharField(
        "Específicaciones",
        max_length=64,
        validators=[
            MinValueValidator(1),
            MaxLengthValidator(255),
            PositiveIntegerValidator(),
        ],
    )
    subespefc = models.CharField(
        "Sub-Especialidad",
        max_length=64,
        validators=[
            MinValueValidator(1),
            MaxLengthValidator(255),
            PositiveIntegerValidator(),
        ],
    )
    denomc = models.CharField(
        "Denominación",
        max_length=64,
        validators=[MinLengthValidator(9), MaxLengthValidator(255), TextValidator()],
    )
    presuacorc = models.CharField("Presupuesto asignado", max_length=64)
    caufechac = models.CharField("Causado a la fecha", max_length=64)
    dispc = models.CharField("Disponible a causar", max_length=64)
    montocc = models.CharField("Monto comprometido", max_length=64)
    saldofc = models.CharField("Saldo final", max_length=64)
    direccionc = models.CharField(
        "Dirección cedente",
        max_length=64,
        validators=[MinLengthValidator(9), MaxLengthValidator(255), TextValidator()],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.partidac, self.generalc)

    class Meta:
        verbose_name = "Cedente"
        verbose_name_plural = "Cedentes"
        permissions = [
            ("listar_cedente", "Puede listar cedente"),
            ("agregar_cedente", "Puede agregar cedente"),
            ("ver_cedente", "Puede ver cedente"),
            ("editar_cedente", "Puede actualizar cedente"),
            ("eliminar_cedente", "Puede eliminar cedente"),
            ("pdf_cedente", "Puede generar pdf de cedente"),
        ]
