from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.models import Estado


class Incidencia(BaseModel):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    sede = models.CharField(max_length=300)
    departamento = models.CharField(max_length=300)
    tipoincidencia = models.CharField(verbose_name="Tipo Incidencia", max_length=300)
    usuario = models.CharField(max_length=300)
    observaciones = models.CharField(max_length=300)
    tiposolicitud = models.CharField(max_length=350, verbose_name="Tipo Solicitud")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
