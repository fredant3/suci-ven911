from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Proyecto(BaseModel):
    nombrep = models.CharField(max_length=64, verbose_name="Nombre del Proyecto:")
    fechai = models.DateField(verbose_name="Fecha de Inicio")
    fechac = models.DateField(verbose_name="Fecha de Culminación")
    situacionp = models.CharField(
        max_length=64, verbose_name="Situación Presupuestaria:"
    )
    montoproyecto = models.CharField(
        max_length=64, verbose_name="Monto Total del Proyecto:"
    )
    responsableg = models.CharField(max_length=64, verbose_name="Responsable Gerente:")
    responsablet = models.CharField(max_length=64, verbose_name="Responsable Técnico:")
    responsabler = models.CharField(
        max_length=64, verbose_name="Responsable Registrador:"
    )
    responsablea = models.CharField(
        max_length=64, verbose_name="Responsable Administrativo:"
    )
    estatus = models.CharField(max_length=64, verbose_name="Estatus del Proyecto:")
    permissions = [
        ("listar_proyecto", "Puede listar proyectos"),
        ("agregar_proyecto", "Puede agregar proyecto"),
        ("ver_proyecto", "Puede ver proyecto"),
        ("editar_proyecto", "Puede actualizar proyecto"),
        ("eliminar_proyecto", "Puede eliminar proyecto"),
        ("pdf_proyecto", "Puede generar pdf de proyecto"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.nombrep

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
