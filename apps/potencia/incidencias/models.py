from administracion.departamentos.models import Departamento
from administracion.sedes.models import Sede
from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES


class TipoIncidencia(BaseModel):
    tipo = models.CharField(max_length=120)
    permissions = [
        ("listar_tipo_incidencia", "Puede listar tipo incidencia"),
        ("agregar_tipo_incidencia", "Puede agregar tipo incidencia"),
        ("ver_tipo_incidencia", "Puede ver tipo incidencia"),
        ("editar_tipo_incidencia", "Puede actualizar tipo incidencia"),
        ("eliminar_tipo_incidencia", "Puede eliminar tipo incidencia"),
    ]

    def __str__(self):
        return self.tipo


class Incidencia(BaseModel):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    estado = models.CharField(
        "Estado", name="estado", max_length=2, choices=ESTADOS_CHOICES
    )
    tipo_incidencia = models.ForeignKey(TipoIncidencia, on_delete=models.CASCADE)
    tipo_solicitud = models.CharField(max_length=80, verbose_name="Tipo Solicitud")
    observaciones = models.CharField(max_length=200)
    permissions = [
        ("listar_incidencia", "Puede listar incidencia"),
        ("agregar_incidencia", "Puede agregar incidencia"),
        ("ver_incidencia", "Puede ver incidencia"),
        ("editar_incidencia", "Puede actualizar incidencia"),
        ("eliminar_incidencia", "Puede eliminar incidencia"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
