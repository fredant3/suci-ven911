from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)

ESTATUS_CHOICES = (
    ("reg", "Registrado"),
    ("pro", "En Proceso"),
    ("nop", "No Procede"),
)


class RegistroFilmico(BaseModel):
    estatus = models.CharField(max_length=3, choices=ESTATUS_CHOICES)
    camara = models.CharField(
        "Cámara",
        max_length=50,
        blank=True,
        null=True,
        validators=[MinLengthValidator(5), MaxLengthValidator(50), TextValidator()],
    )
    motivo_solicitud = models.TextField(
        "Motivo de Solicitud",
        max_length=400,
        validators=[MinLengthValidator(5), MaxLengthValidator(400), TextValidator()],
    )
    ente_solicita = models.CharField(
        "Ente que Solicita",
        max_length=50,
        blank=True,
        null=True,
        validators=[MinLengthValidator(9), MaxLengthValidator(50), TextValidator()],
    )
    direccion = models.CharField(
        "Dirección",
        max_length=150,
        blank=True,
        null=True,
        validators=[MinLengthValidator(9), MaxLengthValidator(150), TextValidator()],
    )
    fecha_solicitud = models.DateField(blank=True, null=True)
    fecha_culminacion = models.DateField(blank=True, null=True)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.camara

    class Meta:
        verbose_name = "registro_filmico"
        verbose_name_plural = "registro_filmicos"
        permissions = [
            ("listar_registroFilmico", "Puede listar registros filmicos"),
            ("agregar_registroFilmico", "Puede agregar registro filmico"),
            ("ver_registroFilmico", "Puede ver registro filmico"),
            ("editar_registroFilmico", "Puede actualizar registro filmico"),
            ("eliminar_registroFilmico", "Puede eliminar registro filmico"),
            ("exel_registroFilmico", "Puede exportar a exel registro filmico"),
        ]
