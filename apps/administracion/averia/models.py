from administracion.departamentos.models import Departamento
from django.db.models import CASCADE, CharField, ForeignKey, TextField
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator, UnicodeAlphaSpaceValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class TipoAveria(BaseModel):
    nombre = CharField(max_length=255)

    class Meta:
        permissions = [
            ("listar_tipo_averia", "Puede listar tipos de averias"),
            ("agregar_tipo_averia", "Puede agregar tipo de averia"),
            ("ver_tipo_averia", "Puede ver tipo de averia"),
            ("editar_tipo_averia", "Puede actualizar tipo de averia"),
            ("eliminar_tipo_averia", "Puede eliminar tipo de averia"),
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
    problema = CharField(
        "Problema",
        max_length=255,
        validators=[MinLengthValidator(9), MaxLengthValidator(255), TextValidator()],
    )
    ubicacion = CharField(
        "Ubicación",
        max_length=255,
        validators=[MinLengthValidator(9), MaxLengthValidator(255), TextValidator()],
    )
    serial = CharField(
        "Serial",
        max_length=255,
        validators=[
            MinLengthValidator(6),
            MaxLengthValidator(255),
            UnicodeAlphaSpaceValidator(extra_chars="-"),
        ],
    )
    codigo_bn = CharField(
        "Código BN",
        max_length=255,
        validators=[MinLengthValidator(5), MaxLengthValidator(255), TextValidator()],
    )

    class Meta:
        permissions = [
            ("listar_averia", "Puede listar averias"),
            ("agregar_averia", "Puede agregar averia"),
            ("ver_averia", "Puede ver averia"),
            ("editar_averia", "Puede actualizar averia"),
            ("eliminar_averia", "Puede eliminar averia"),
        ]

    def __str__(self):
        return self.problema
