from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Gestion(BaseModel):
    name = models.CharField(max_length=64, verbose_name="Nombre:", default="")
    apellido = models.CharField(max_length=64, verbose_name="Apellido:", default="")
    cedula = models.CharField(max_length=64, verbose_name="Cédula:", default="")
    tipo = models.CharField(
        max_length=64, verbose_name="Tipo de Incidente:", default=""
    )
    descripcion = models.CharField(
        max_length=64, verbose_name="Descripción:", default=""
    )
    fecha = models.DateField(verbose_name="Fecha")
    direccion = models.CharField(max_length=64, verbose_name="Dirección:", default="")
    cargo = models.CharField(max_length=64, verbose_name="Cargo:", default="")
    hora = models.CharField(max_length=64, verbose_name="Hora de Entrada:", default="")
    permissions = [
        ("listar_gestiones", "Listar gestiones"),
        ("agregar_gestion", "Agregar gestion"),
        ("ver_gestion", "Ver gestion"),
        ("modificar_gestion", "Modificar gestion"),
        ("eliminar_gestion", "Eliminar gestion"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.name, self.apellido)

    class Meta:
        verbose_name = "gestion"
        verbose_name_plural = "gestiones"
