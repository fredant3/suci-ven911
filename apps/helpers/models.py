# from administracion.cupaz.models import CuadrantePaz
from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel

NACIONALIDAD_CHOICES = (
    ("ve", "Venezolano"),
    ("ex", "Extranjero"),
)
GENERO_CHOICES = (
    ("f", "Femenino"),
    ("m", "Masculino"),
)
ESTADO_CIVIL_CHOICES = (
    ("s", "Soltero"),
    ("c", "Casado"),
    ("d", "Divorviado"),
    ("v", "Viudo"),
)
TIPO_SANGRE_CHOICES = (
    ("a+", "A+ (Rh positivo)"),
    ("a-", "A- (Rh negativo)"),
    ("b+", "B+ (Rh positivo)"),
    ("b-", "B- (Rh negativo)"),
    ("ab+", "AB+ (Rh positivo)"),
    ("ab-", "AB- (Rh negativo)"),
    ("o+", "O+ (Rh positivo)"),
    ("o-", "O- (Rh negativo)"),
)


class Estado(BaseModel):
    nombre = models.CharField(max_length=150)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0}".format(self.nombre)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"


class Municipio(BaseModel):
    nombre = models.CharField(max_length=150)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0}".format(self.nombre)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"


class Parroquia(BaseModel):
    nombre = models.CharField(max_length=255)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    # id_cuadrante_paz = models.ForeignKey(CuadrantePaz, on_delete=models.CASCADE)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0}".format(self.nombre)

    class Meta:
        verbose_name = "Parroquia"
        verbose_name_plural = "Parroquias"
