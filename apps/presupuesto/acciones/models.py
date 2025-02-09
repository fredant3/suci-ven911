from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Accion(BaseModel):
    proyecto = models.CharField("Nombre del Proyecto:", max_length=64)
    fecha_inicio = models.DateField("Fecha de Inicio")
    fecha_culminacion = models.DateField("Fecha de Culminación")
    situacion_presupuestaria = models.CharField(
        "Situación Presupuestaria:", max_length=64
    )
    monto = models.CharField("Monto Total del Proyecto:", max_length=64)
    responsable_gerente = models.CharField("Responsable Gerente:", max_length=64)
    responsable_tecnico = models.CharField("Responsable Técnico:", max_length=64)
    responsable_registrador = models.CharField(
        "Responsable Registrador:", max_length=64
    )
    responsable_administrativo = models.CharField(
        "Responsable Administrativo:", max_length=64
    )
    estatus = models.CharField("Estatus del Proyecto:", max_length=64)
    permissions = [
        ("listar_accion", "Puede listar acciones"),
        ("agregar_accion", "Puede agregar accion"),
        ("ver_accion", "Puede ver accion"),
        ("editar_accion", "Puede actualizar accion"),
        ("eliminar_accion", "Puede eliminar accion"),
        ("pdf_accion", "Puede generar pdf de accion"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.proyecto

    class Meta:
        verbose_name = "Accion"
        verbose_name_plural = "Acciones"
