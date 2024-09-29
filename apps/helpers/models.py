from django.db import models


class CuadrantePaz(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


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
