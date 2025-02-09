from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Asignacion(BaseModel):
    departamento = models.CharField("Nombre de la dirección:", max_length=64)
    presupuesto = models.CharField("Presupuesto asignado:", max_length=64)
    objetivo = models.CharField("Objetivo general anual:", max_length=64)
    numero_partida = models.CharField("Número de partida:", max_length=10)
    permissions = [
        ("listar_asignacion", "Puede listar asignacion"),
        ("agregar_asignacion", "Puede agregar asignacion"),
        ("ver_asignacion", "Puede ver asignacion"),
        ("editar_asignacion", "Puede actualizar asignacion"),
        ("eliminar_asignacion", "Puede eliminar asignacion"),
        ("pdf_asignacion", "Puede generar pdf de asignacion"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.numero_partida

    class Meta:
        verbose_name = "Asignacion"
        verbose_name_plural = "Asignaciones"
