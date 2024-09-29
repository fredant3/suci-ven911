from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.models import Estado, Municipio, Parroquia


class Incidencia(models.Model):
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo


class OrganismoCompetente(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Emergencia(BaseModel):
    denunciante = models.CharField(max_length=255)
    telefono_denunciante = models.CharField(max_length=255, blank=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    id_parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
    id_incidencia = models.ForeignKey(Incidencia, on_delete=models.CASCADE)
    direccion_incidencia = models.TextField(blank=True)
    id_organismo = models.ForeignKey(OrganismoCompetente, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True)
    # Localizacion_sede soon
    datecompleted = models.DateTimeField(null=True, blank=True)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.denunciante + " by-" + self.created_by.username

    class Meta:
        verbose_name = "emergencia"
        verbose_name_plural = "emergencias"
