from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator, UnicodeAlphaSpaceValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Accion(BaseModel):
    proyecto = models.CharField("Nombre del Proyecto:", max_length=64)
    fecha_inicio = models.DateField("Fecha de Inicio")
    fecha_culminacion = models.DateField("Fecha de Culminación")
    situacion_presupuestaria = models.CharField(
        "Situación Presupuestaria:",
        max_length=64,
        validators=[
            MinLengthValidator(6),
            MaxLengthValidator(64),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    monto = models.CharField("Monto asignado:", max_length=64)
    responsable_gerente = models.CharField(
        "Responsable Gerente:",
        max_length=64,
        validators=[MinLengthValidator(6), MaxLengthValidator(64), TextValidator()],
    )
    responsable_tecnico = models.CharField(
        "Responsable Técnico:",
        max_length=64,
        validators=[MinLengthValidator(6), MaxLengthValidator(64), TextValidator()],
    )
    responsable_registrador = models.CharField(
        "Responsable Registrador:",
        max_length=64,
        validators=[MinLengthValidator(6), MaxLengthValidator(64), TextValidator()],
    )
    responsable_administrativo = models.CharField(
        "Responsable Administrativo:",
        max_length=64,
        validators=[MinLengthValidator(6), MaxLengthValidator(64), TextValidator()],
    )
    estatus = models.CharField(
        "Estatus del Proyecto:",
        max_length=64,
        validators=[MinLengthValidator(6), MaxLengthValidator(64), TextValidator()],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.proyecto

    class Meta:
        verbose_name = "Accion"
        verbose_name_plural = "Acciones"
        permissions = [
            ("listar_accion", "Puede listar acciones"),
            ("agregar_accion", "Puede agregar accion"),
            ("ver_accion", "Puede ver accion"),
            ("editar_accion", "Puede actualizar accion"),
            ("eliminar_accion", "Puede eliminar accion"),
            ("pdf_accion", "Puede generar pdf de accion"),
        ]
