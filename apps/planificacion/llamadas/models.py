from django.db.models import CharField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES, MONTH_CHOICES
from helpers.validForm import PositiveIntegerValidator
from django.core.validators import MinValueValidator


class Llamada(BaseModel):
    mes = CharField("Mes:", max_length=3, choices=MONTH_CHOICES)
    estado = CharField("Estado", name="estado", max_length=2, choices=ESTADOS_CHOICES)
    informativa = CharField(
        "Llamadas informativas",
        max_length=64,
        validators=[MinValueValidator(1), PositiveIntegerValidator()],
    )
    falsa = CharField(
        "Llamadas falsas",
        max_length=64,
        validators=[MinValueValidator(1), PositiveIntegerValidator()],
    )
    realesno = CharField(
        "Llamadas reales no atendidas",
        max_length=64,
        validators=[MinValueValidator(1), PositiveIntegerValidator()],
    )
    realesf = CharField(
        "Llamadas reales finalizadas",
        max_length=64,
        validators=[MinValueValidator(1), PositiveIntegerValidator()],
    )
    videop = CharField(
        "Videollamadas protección",
        max_length=64,
        validators=[MinValueValidator(1), PositiveIntegerValidator()],
    )

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        verbose_name = "llamada"
        verbose_name_plural = "llamadas"
        permissions = [
            ("listar_llamada", "Puede listar llamada"),
            ("agregar_llamada", "Puede agregar llamada"),
            ("ver_llamada", "Puede ver llamada"),
            ("editar_llamada", "Puede actualizar llamada"),
            ("eliminar_llamada", "Puede eliminar llamada"),
        ]
