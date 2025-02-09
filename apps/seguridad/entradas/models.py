from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Entrada(BaseModel):
    name = models.CharField(max_length=64, verbose_name="Nombre:", default="")
    apellido = models.CharField(max_length=64, verbose_name="Apellido:", default="")
    cedula = models.CharField(max_length=64, verbose_name="Cédula:", default="")
    telefono = models.CharField(max_length=64, verbose_name="Teléfono:", default="")
    fecha = models.DateField(verbose_name="Fecha")
    direccion = models.CharField(max_length=64, verbose_name="Dirección:", default="")
    cargo = models.CharField(max_length=64, verbose_name="Cargo:", default="")
    hora = models.CharField(max_length=64, verbose_name="Hora de Entrada:", default="")
    permissions = [
        ("listar_entradas", "Listar entradas"),
        ("agregar_entrada", "Agregar entrada"),
        ("ver_entrada", "Ver entrada"),
        ("modificar_entrada", "Modificar entrada"),
        ("eliminar_entrada", "Eliminar entrada"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.name, self.apellido)

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
