from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from potencia.incidencias.models import TipoIncidencia


class OrganismoCompetente(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Emergencia(BaseModel):
    denunciante = models.CharField(max_length=255)
    telefono_denunciante = models.CharField(max_length=255, blank=True)
    estado = models.CharField("Estado", max_length=90)
    municipio = models.CharField("Municipio", max_length=90)
    parroquia = models.CharField("Parroquia", max_length=90)
    id_incidencia = models.ForeignKey(TipoIncidencia, on_delete=models.CASCADE)
    id_organismo = models.ForeignKey(OrganismoCompetente, on_delete=models.CASCADE)
    direccion_incidencia = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    # Localizacion_sede soon
    datecompleted = models.DateTimeField(null=True, blank=True)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.denunciante + " by-" + self.created_by

    class Meta:
        verbose_name = "emergencia"
        verbose_name_plural = "emergencias"
