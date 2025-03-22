from administracion.departamentos.models import Departamento
from administracion.sedes.models import Sede
from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES
from potencia.tipo_incidencia.models import TipoIncidencia

INCIDENCIA_CHOICES = (
    ("soliint", "Solicitud Interna"),
    ("soliext", "Solicitud Externa"),
)


class Incidencia(BaseModel):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    estado = models.CharField(
        "Estado", name="estado", max_length=2, choices=ESTADOS_CHOICES
    )
    tipo_incidencia = models.ForeignKey(TipoIncidencia, on_delete=models.CASCADE)
    tipo_solicitud = models.CharField(
        "Tipo de Solicitud", max_length=10, choices=INCIDENCIA_CHOICES
    )
    observaciones = models.CharField(max_length=200)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
        permissions = [
            ("listar_incidencia", "Puede listar incidencia"),
            ("agregar_incidencia", "Puede agregar incidencia"),
            ("ver_incidencia", "Puede ver incidencia"),
            ("editar_incidencia", "Puede actualizar incidencia"),
            ("eliminar_incidencia", "Puede eliminar incidencia"),
        ]
