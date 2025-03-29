from index.mixins.BaseModelMixin import BaseModel

from django.db.models import CharField, TextField
from django.forms import model_to_dict


class EquipmentEntity(BaseModel):
    STATUS_CHOICES = [
        ("available", "Disponible"),
        ("loaned", "Prestado"),
        ("maintenance", "Mantenimiento"),
    ]

    name = CharField(max_length=100, verbose_name="Equipo")
    description = TextField(verbose_name="Descripción del equipo")
    status = CharField(max_length=50, verbose_name="Estatus del equipo", choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        db_table = "gc_equipments"
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ["status"]
