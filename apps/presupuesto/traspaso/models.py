from django.db.models import CharField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import (
    TextValidator,
)
from django.core.validators import MinLengthValidator

PROYECTOS_ACCIONES = (
    ("proyecto", "Proyecto"),
    ("accion", "Acciones Centralizadas"),
)


class Traspaso(BaseModel):

    proyecto_acciones = CharField(
        "Proyecto o Acciones Centralizadas",
        max_length=64,
        choices=PROYECTOS_ACCIONES,
        validators=[
            MinLengthValidator(3),
            TextValidator(),
        ],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self) -> str:
        return self.proyecto_acciones

    class Meta:
        app_label = "presupuesto"
        verbose_name = "Traspaso"
        verbose_name_plural = "Traspasos"
        permissions = [
            ("listar_traspaso", "Puede listar traspaso"),
            ("agregar_traspaso", "Puede agregar traspaso"),
            ("ver_traspaso", "Puede ver traspaso"),
            ("editar_traspaso", "Puede actualizar traspaso"),
            ("eliminar_traspaso", "Puede eliminar traspaso"),
            ("exel_traspaso", "Puede generar pdf de traspaso"),
        ]
