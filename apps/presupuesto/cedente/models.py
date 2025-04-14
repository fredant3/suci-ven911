from django.db.models import CharField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import (
    TextValidator,
)
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Cedente(BaseModel):
    idc = CharField(
        "Identificador Cedente:",
        max_length=100,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(255),
            TextValidator(extra_chars="-"),
        ],
    )
    partidac = CharField(
        "Partida Contable",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(255),
            TextValidator(extra_chars="-"),
        ],
    )
    generalc = CharField(
        "General",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(255),
        ],
    )
    espefc = CharField(
        "Específicaciones",
        max_length=64,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(255),
        ],
    )
    subespefc = CharField(
        "Sub-Especialidad",
        max_length=64,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(255),
        ],
    )
    denomc = CharField(
        "Denominación",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(255), TextValidator()],
    )
    presuacorc = CharField(
        "Presupuesto asignado",
        max_length=64,
        validators=[MinLengthValidator(0)],
    )
    caufechac = CharField("Causado a la fecha", max_length=64)
    dispc = CharField("Disponible a causar", max_length=64)
    montocc = CharField("Monto comprometido", max_length=64)
    saldofc = CharField("Saldo final", max_length=64)
    direccionc = CharField(
        "Dirección cedente",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(255), TextValidator()],
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
