from django.db import models
from helpers.BaseModelMixin import BaseModel
from users.auth.models import User

tipoconsidcion = (("N", "Nuevo"), ("U", "Usado"), ("D", "Deteriorado"))


class TipoArticulo(BaseModel):
    nombre = models.CharField(max_length=255)


class Articulo(BaseModel):
    descripcion = models.TextField(max_length=255)
    marca = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    placa = models.CharField(max_length=255, blank=True, null=True)
    cantidad_combustible = models.IntegerField(blank=True, null=True)
    codigo_bn = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField()
    tipo_articulo = models.ForeignKey(TipoArticulo, on_delete=models.CASCADE)
    condicion = models.CharField(max_length=1, choices=tipoconsidcion)
    fecha_adq = models.DateField()
    asignado = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion + " - " + str(self.marca) + " - " + str(self.modelo)
