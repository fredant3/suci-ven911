from django.db import models
from helpers.BaseModelMixin import BaseModel


class TipoIncidencia(BaseModel):
    tipo = models.CharField(max_length=120)

    class Meta:
        permissions = [
            ("listar_tipo_incidencia", "Puede listar tipo incidencia"),
            ("agregar_tipo_incidencia", "Puede agregar tipo incidencia"),
            ("ver_tipo_incidencia", "Puede ver tipo incidencia"),
            ("editar_tipo_incidencia", "Puede actualizar tipo incidencia"),
            ("eliminar_tipo_incidencia", "Puede eliminar tipo incidencia"),
        ]

    def __str__(self):
        return self.tipo