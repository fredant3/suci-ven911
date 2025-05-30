from administracion.departamentos.models import Departamento
from django.db.models import CASCADE, CharField, ForeignKey, TextField
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)
from administracion.tipo_averia.models import TipoAveria
from helpers.BaseModelMixin import BaseModel, DEP_AVERIA


class ReportesAdministracion(BaseModel):
    tipo_averia = ForeignKey(
        TipoAveria, on_delete=CASCADE, verbose_name="Tipo de avería"
    )
    departamento = ForeignKey(
        Departamento, on_delete=CASCADE, verbose_name="Departamento"
    )
    problema = TextField(
        "Problema",
        max_length=180,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )

    serial = CharField(
        "Serial",
        max_length=30,
        validators=[
            MinLengthValidator(6),
            MaxLengthValidator(30),
            TextValidator(),
        ],
    )
    codigo_bn = CharField(
        "Código BN",
        max_length=30,
        validators=[MinLengthValidator(6), MaxLengthValidator(30), TextValidator()],
    )
    observaciones = TextField(
        "Observaciones",
        max_length=180,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
        null=True,
    )
    quien_reporta = CharField(
        "Depertamento que reporta Averia", max_length=2, choices=DEP_AVERIA
    )

    class Meta:
        permissions = [
            ("listar_reporteadministracion", "Puede listar reporte"),
            ("agregar_reporteadministracion", "Puede agregar reporte"),
            ("ver_reporteadministracion", "Puede ver reporte"),
            ("editar_reporteadministracion", "Puede editar reporte"),
            ("eliminar_reporteadministracion", "Puede eliminar reporte"),
        ]
        db_table = "reportes_administracion"
        verbose_name = "Reporte Administración"
        verbose_name_plural = "Reportes administraciones"
        ordering = ["-created_at"]

    def __str__(self):
        return self.problema
