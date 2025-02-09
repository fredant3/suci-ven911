from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from rrhh.empleados.models import Empleado


class Educacion(BaseModel):
    colegio = models.CharField(max_length=120)
    codigo_titulo = models.CharField(max_length=120)
    titulo = models.CharField(max_length=120)
    area_conocimiento = models.CharField(max_length=120)
    fecha_inicio = models.DateField()
    fecha_culminacion = models.DateField()
    enlace_certificado = models.CharField(max_length=120, null=True, blank=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    permissions = [
        ("listar_educacion", "Puede listar educacion"),
        ("agregar_educacion", "Puede agregar educacion"),
        ("ver_educacion", "Puede ver educacion"),
        ("editar_educacion", "Puede actualizar educacion"),
        ("eliminar_educacion", "Puede eliminar educacion"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.name, self.apellido)

    class Meta:
        verbose_name = "educacion"
        verbose_name_plural = "educaciones"
