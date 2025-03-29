from django.db.models import CharField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES, MONTH_CHOICES
from helpers.validForm import PositiveIntegerValidator, TextValidator
from django.core.validators import (
    MinValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)


class Transporte(BaseModel):
    estado = CharField(
        "Estado del transporte",
        name="estado",
        max_length=2,
        choices=ESTADOS_CHOICES,
    )
    mes = CharField("Mes de operación", max_length=3, choices=MONTH_CHOICES)
    transporte = CharField(
        "Tipo de transporte",
        max_length=64,
        validators=[MinLengthValidator(9), MaxLengthValidator(64), TextValidator()],
    )
    cantidad = CharField(
        "Cantidad de unidades",
        max_length=64,
        validators=[
            MinValueValidator(1),
            MaxLengthValidator(64),
            PositiveIntegerValidator(),
        ],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.ente

    class Meta:
        verbose_name = "transporte"
        verbose_name_plural = "transportes"
        permissions = [
            ("listar_transporte", "Puede listar transporte"),
            ("agregar_transporte", "Puede agregar transporte"),
            ("ver_transporte", "Puede ver transporte"),
            ("editar_transporte", "Puede actualizar transporte"),
            ("eliminar_transporte", "Puede eliminar transporte"),
        ]
