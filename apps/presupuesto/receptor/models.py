from django.db.models import CharField
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
    idr = CharField(
        "Identificador Receptor",
        max_length=100,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(100),
            TextValidator(),
        ],
    )
    partidar = CharField(
        "Partida Contable",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )
    generalr = CharField(
        "General",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
        ],
    )
    espefr = CharField(
        "Específicaciones",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
        ],
    )
    subespefr = CharField(
        "Sub-Especialidad",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
        ],
    )
    denomr = CharField(
        "Denomincación",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )
    presuacorr = CharField(
        "Presupuesto acordado",
        max_length=64,
    )
    caufechar = CharField(
        "Causado a la fecha",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )
    dispr = CharField(
        "Disponible a causar",
        max_length=64,
    )
    montocr = CharField(
        "Monto a ceder",
        max_length=64,
    )
    saldofr = CharField(
        "Saldo final",
        max_length=64,
    )
    direccionr = CharField(
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
