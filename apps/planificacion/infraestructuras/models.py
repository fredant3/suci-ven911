from django.db.models import CharField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES, MONTH_CHOICES
from helpers.validForm import PositiveIntegerValidator, TextValidator
from django.core.validators import (
    MinValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)


class Infraestructura(BaseModel):
    estado = CharField(
        "Estado de la infraestructura",
        name="estado",
        max_length=2,
        choices=ESTADOS_CHOICES,
    )
    mes = CharField("Mes programado", max_length=3, choices=MONTH_CHOICES)
    infraestructura = CharField(
        "Nombre de la infraestructura",
        max_length=64,
        validators=[MinLengthValidator(9), MaxLengthValidator(64), TextValidator()],
    )
    cantidad = CharField(
        "Cantidad estimada",
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
        verbose_name = "infraestructura"
        verbose_name_plural = "infraestructuras"
        permissions = [
            ("listar_infraestructura", "Puede listar infraestructura"),
            ("agregar_infraestructura", "Puede agregar infraestructura"),
            ("ver_infraestructura", "Puede ver infraestructura"),
            ("editar_infraestructura", "Puede actualizar infraestructura"),
            ("eliminar_infraestructura", "Puede eliminar infraestructura"),
        ]
