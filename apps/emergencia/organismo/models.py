from django.db.models import CharField
from helpers.BaseModelMixin import BaseModel


class OrganismoCompetente(BaseModel):
    nombre = CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("listar_organismo_emergencia", "Puede listar tipo incidencia"),
            ("agregar_organismo_emergencia", "Puede agregar tipo incidencia"),
            ("ver_organismo_emergencia", "Puede ver tipo incidencia"),
            ("editar_organismo_emergencia", "Puede actualizar tipo incidencia"),
            ("eliminar_organismo_emergencia", "Puede eliminar tipo incidencia"),
        ]
