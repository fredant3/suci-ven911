from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.models import ESTADO_CIVIL_CHOICES, SEXO_CHOICES
from rrhh.empleados.models import Empleado
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db.models import CharField, BooleanField
from helpers.validForm import (
    CedulaVenezolanaValidator,
    TextValidator,
    UnicodeAlphaSpaceValidator,
)

PARENTEZCO = (
    ("hermano", "Hermana|Hermano"),
    ("pareja", "Conyugue"),
    ("mama", "Madre"),
    ("papa", "Padre"),
    ("hijo", "Hija|Hijo"),
)
TIPO_HIJO = (
    ("menor_12", "Hijo menor de 12"),
    ("hijos_13_18", "Hijo entre 13 y 18"),
    ("mayor_18", "Hijo mayor de 18"),
)


class Familiar(BaseModel):
    parentezco = models.CharField("Parentezco", max_length=7, choices=PARENTEZCO)
    tipo_hijo = models.CharField(
        "Tipo de hijo", max_length=11, choices=TIPO_HIJO, null=True, blank=True
    )
    discapacidad = BooleanField(default=False)
    nombres = models.CharField(
        "Nombres del Familiar",
        max_length=90,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(90),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    apellidos = models.CharField(
        "Apellidos del Familiar",
        max_length=90,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(90),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    cedula = CharField(
        "Cédula de identidad",
        max_length=15,
        unique=True,
        validators=[
            MinLengthValidator(7),
            MaxLengthValidator(14),
            CedulaVenezolanaValidator(),
        ],
    )
    fecha_nacimiento = models.DateField("Fecha de nacimiento")
    sexo = models.CharField("Genero", max_length=1, choices=SEXO_CHOICES)
    estado_civil = models.CharField(
        "Estado civil", max_length=1, choices=ESTADO_CIVIL_CHOICES
    )
    empleado = models.ForeignKey(
        Empleado, on_delete=models.CASCADE, verbose_name="Empleado"
    )
    observacion = models.CharField(
        "Observaciones",
        max_length=150,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(150),
            TextValidator(),
        ],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "familiar"
        verbose_name_plural = "familiares"
        permissions = [
            ("listar_familiares", "Listar familiares"),
            ("agregar_familiar", "Agregar familiares"),
            ("ver_familiar", "Ver familiares"),
            ("modificar_familiar", "Modificar familiares"),
            ("eliminar_familiar", "Eliminar familiares"),
            ("exel_familiar", "Exportar familiares a excel"),
        ]
