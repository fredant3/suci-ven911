from django.db import models

from apps.administracion.cupaz.models import CuadrantePaz

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


class Estado(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=255)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Parroquia(models.Model):
    nombre = models.CharField(max_length=255)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    id_cuadrante_paz = models.ForeignKey(CuadrantePaz, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
