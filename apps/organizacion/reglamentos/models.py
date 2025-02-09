from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTATUS_CHOICES


class Reglamento(BaseModel):
    name = models.CharField(
        max_length=64, verbose_name="Nombre de Reglamento:", default=""
    )
    file = models.FileField(
        upload_to="reglamentos/", verbose_name="Archivo", default=""
    )
    user = models.CharField(max_length=64, verbose_name="Usuario", default="")
    date = models.DateField(verbose_name="Fecha", blank=True)
    progre = models.CharField(max_length=64, verbose_name="Progreso:", default="")
    estado = models.CharField(max_length=8, choices=ESTATUS_CHOICES, default="inactivo")

    class Meta:
        permissions = [
            ("listar_reglamento", "Puede listar reglamentos"),
            ("agregar_reglamento", "Puede agregar reglamento"),
            ("ver_reglamento", "Puede ver reglamento"),
            ("editar_reglamento", "Puede actualizar reglamento"),
            ("eliminar_reglamento", "Puede eliminar reglamento"),
        ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "reglamento"
        verbose_name_plural = "reglamentos"
