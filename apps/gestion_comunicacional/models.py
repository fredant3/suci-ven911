from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES
from helpers.models import (
    ESTRATEGIAS_METODOLOGICAS,
    AMBITO_ACCION,
    ACTIVIDAD_PREVENTIVA,
    BOOLEAN_CHOICES,
)
from django.db.models import CharField, BooleanField
from helpers.validForm import CedulaVenezolanaValidator, TextValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator


class GestionComunicacional(BaseModel):
    nombre_actividad = models.TextField(
        "Nombre de la actividad",
        max_length=180,
        blank=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )
    actividad_realizada = models.TextField(
        "Nombre de la actividad",
        max_length=180,
        blank=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )
    descripcion_actividad = models.TextField(
        "descripción actividad",
        max_length=180,
        blank=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )
    actividad_preventiva = CharField(max_length=3, choices=AMBITO_ACCION)
    estado = models.CharField(
        "Estado", name="estado", max_length=2, choices=ESTADOS_CHOICES
    )
    municipio = models.CharField("Municipio", name="municipio", max_length=90)
    parroquia = models.CharField("Parroquia", name="parroquia", max_length=90)
    estrategias_metodologicas = CharField(
        max_length=2, choices=ESTRATEGIAS_METODOLOGICAS
    )
    ambito_accion = CharField(max_length=2, choices=ACTIVIDAD_PREVENTIVA)
    poblacion_abordada = models.TextField(
        "población abordada",
        max_length=180,
        blank=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )
    equipo_social = models.TextField(
        "equipo social",
        max_length=180,
        blank=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )
    realizado_por = models.TextField(
        "Realizado por",
        max_length=180,
        blank=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )
    validado_por = models.TextField(
        "Validado por",
        max_length=180,
        blank=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
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
    observaciones = models.TextField(
        "Observaciones",
        max_length=180,
        blank=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )
    # Localizacion_sede soon
    municipio_priorizado = BooleanField(
        "Municipio priorizado",
        choices=BOOLEAN_CHOICES,
        default=BOOLEAN_CHOICES[1],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.nombre_actividad + " by-" + self.created_by

    class Meta:
        verbose_name = "Gestion Comunicacional"
        verbose_name_plural = "Gestiones Comunicacionales"
        permissions = [
            ("listar_gestion_comunicacional", "Puede listar gestion comunicacional"),
            ("agregar_gestion_comunicacional", "Puede agregar gestion comunicacional"),
            ("ver_gestion_comunicacional", "Puede ver gestion comunicacional"),
            (
                "editar_gestion_comunicacional",
                "Puede actualizar gestion comunicacional",
            ),
            (
                "eliminar_gestion_comunicacional",
                "Puede eliminar gestion comunicacional",
            ),
        ]
