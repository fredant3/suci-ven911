from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Incidencia(BaseModel):
    estado = models.CharField("Estado", max_length=120)
    sede = models.CharField(max_length=120)
    departamento = models.CharField(max_length=120)
    tipoincidencia = models.CharField("Tipo Incidencia", max_length=180)
    usuario = models.CharField(max_length=90)
    observaciones = models.CharField(max_length=200)
    tiposolicitud = models.CharField(max_length=80, verbose_name="Tipo Solicitud")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
