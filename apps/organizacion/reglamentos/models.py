from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTATUS_CHOICES


class Reglamento(BaseModel):
    name = models.CharField("Nombre de Reglamento:", max_length=64)
    file = models.FileField("Archivo", upload_to="reglamentos/")
    date = models.DateField("Fecha", blank=True)
    progre = models.CharField("Progreso:", max_length=64, default="0")
    estado = models.CharField(max_length=8, choices=ESTATUS_CHOICES, default="inactivo")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "reglamento"
        verbose_name_plural = "reglamentos"
        permissions = [
            ("listar_reglamento", "Puede listar reglamentos"),
            ("agregar_reglamento", "Puede agregar reglamento"),
            ("ver_reglamento", "Puede ver reglamento"),
            ("editar_reglamento", "Puede actualizar reglamento"),
            ("eliminar_reglamento", "Puede eliminar reglamento"),
        ]
