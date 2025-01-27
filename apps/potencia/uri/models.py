from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Uri(BaseModel):
    fecha_atencion = models.DateField("Fecha de Atencion")
    nroreporte = models.CharField(
        "Numero de Reporte", max_length=10, blank=True, null=True
    )
    placa = models.CharField("Placa", max_length=10, blank=True, null=True)
    institucion = models.CharField("Institucion", max_length=300, blank=True, null=True)
    tipounidad = models.CharField(
        "Tipo de Unidad", max_length=10, blank=True, null=True
    )
    num_interna = models.CharField(
        "Numeracion Interna", max_length=10, blank=True, null=True
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Unidad de repuesta inmediata"
        verbose_name_plural = "Unidades de repuestas inmediatas"
