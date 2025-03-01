from administracion.departamentos.models import Departamento
from administracion.inventario.models import Articulo
from administracion.sedes.models import Sede
from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Asignacion(BaseModel):
    LIST_ARTICLE = "listar_articulo"
    ADD_ARTICLE = "agregar_articulo"
    VIEW_ARTICLE = "ver_articulo"
    CHANGE_ARTICLE = "editar_articulo"
    DELETE_ARTICLE = "eliminar_articulo"

    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    descripcion = models.TextField(max_length=255)
    observaciones = models.TextField(max_length=255)

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        db_table = "administracion_asignacion"
        verbose_name = "Asignacion"
        verbose_name_plural = "Asignaciones"
        ordering = ["-id"]
        permissions = [
            ("listar_asignacion", "Puede listar asignacions"),
            ("agregar_asignacion", "Puede agregar asignacion"),
            ("ver_asignacion", "Puede ver asignacion"),
            ("editar_asignacion", "Puede actualizar asignacion"),
            ("eliminar_asignacion", "Puede eliminar asignacion"),
        ]
