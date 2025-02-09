from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Salida(BaseModel):
    name = models.CharField(max_length=64, verbose_name="Nombre:", default="")
    apellido = models.CharField(max_length=64, verbose_name="Apellido:", default="")
    cedula = models.CharField(max_length=64, verbose_name="Cédula:", default="")
    telefono = models.CharField(max_length=64, verbose_name="Teléfono:", default="")
    fecha = models.DateField(verbose_name="Fecha")
    direccion = models.CharField(max_length=64, verbose_name="Dirección:", default="")
    cargo = models.CharField(max_length=64, verbose_name="Cargo:", default="")
    hora = models.CharField(max_length=64, verbose_name="Hora de Entrada:", default="")
    permissions = [
        ("listar_salidas", "Listar salidas"),
        ("agregar_salida", "Agregar salida"),
        ("ver_salida", "Ver salida"),
        ("modificar_salida", "Modificar salida"),
        ("eliminar_salida", "Eliminar salida"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.name, self.apellido)

    class Meta:
        verbose_name = "salida"
        verbose_name_plural = "salidas"
