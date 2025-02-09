from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Vehiculo(BaseModel):
    nombre = models.CharField(max_length=64, verbose_name="Nombre:", default="")
    apellido = models.CharField(max_length=64, verbose_name="Apellido:", default="")
    cedula = models.CharField(max_length=64, verbose_name="Cédula:", default="")
    modelo = models.CharField(max_length=64, verbose_name="Modelo:", default="")
    vehiculo = models.CharField(
        max_length=64, verbose_name="Tipo de vehiculo:", default=""
    )
    motivo = models.CharField(max_length=64, verbose_name="Motivo:", default="")
    capagasolina = models.CharField(
        max_length=64, verbose_name="Capacidad de Gasolina:", default=""
    )
    cantigasolina = models.CharField(
        max_length=64, verbose_name="Cantidad de Gasolina:", default=""
    )
    placa = models.CharField(max_length=64, verbose_name="Placa:", default="")
    fecha = models.DateField(verbose_name="Fecha")
    hora = models.CharField(max_length=64, verbose_name="Hora:", default="")
    permissions = [
        ("listar_vehiculos", "Listar vehiculos"),
        ("agregar_vehiculo", "Agregar vehiculo"),
        ("ver_vehiculo", "Ver vehiculo"),
        ("modificar_vehiculo", "Modificar vehiculo"),
        ("eliminar_vehiculo", "Eliminar vehiculo"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.apellido)

    class Meta:
        verbose_name = "vehiculo"
        verbose_name_plural = "vehiculos"
