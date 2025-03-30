from administracion.departamentos.models import Departamento
from django.db.models import CASCADE, CharField, ForeignKey, TextField
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class TipoAveria(BaseModel):
    nombre = CharField(
        max_length=200,
        validators=[MinLengthValidator(3), MaxLengthValidator(200), TextValidator()],
    )

    class Meta:
        permissions = [
            ("listar_tipo_averia", "Puede listar tipos de averías"),
            ("agregar_tipo_averia", "Puede agregar tipo de avería"),
            ("ver_tipo_averia", "Puede ver tipo de avería"),
            ("editar_tipo_averia", "Puede editar tipo de avería"),
            ("eliminar_tipo_averia", "Puede eliminar tipo de avería"),
        ]

    def __str__(self):
        return self.nombre


class Averia(BaseModel):
    tipo_averia = ForeignKey(
        TipoAveria, on_delete=CASCADE, verbose_name="Tipo de avería"
    )
    departamento = ForeignKey(
        Departamento, on_delete=CASCADE, verbose_name="Departamento"
    )
    problema = TextField(
        "Problema",
        max_length=180,
        validators=[MinLengthValidator(9), MaxLengthValidator(180), TextValidator()],
    )
    ubicacion = TextField(
        "Ubicación",
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

    class Meta:
        permissions = [
            ("listar_averia", "Puede listar averías"),
            ("agregar_averia", "Puede agregar avería"),
            ("ver_averia", "Puede ver avería"),
            ("editar_averia", "Puede editar avería"),
            ("eliminar_averia", "Puede eliminar avería"),
        ]

    def __str__(self):
        return self.problema
