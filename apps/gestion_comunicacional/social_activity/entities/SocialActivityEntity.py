from index.mixins.BaseModelMixin import BaseModel

from django.db.models import CharField, DateField, IntegerField, TextField
from django.forms import model_to_dict


class SocialActivityEntity(BaseModel):
    ACTIVITY_TYPE_CHOICES = [
        ("workshop", "Taller"),
        ("conference", "Conferencia"),
        ("campaign", "Campaña"),
    ]

    VIEW_SOCIAL_ACTIVITY = "gc:view_social_activity"
    ADD_SOCIAL_ACTIVITY = "gc:add_social_activity"
    CHANGE_SOCIAL_ACTIVITY = "gc:change_social_activity"
    DELETE_SOCIAL_ACTIVITY = "gc:delete_social_activity"

    activity_type = CharField(max_length=50, verbose_name="Tipo de actividad", choices=ACTIVITY_TYPE_CHOICES)
    date = DateField(verbose_name="Fecha de la actividad")
    location = CharField(max_length=255, verbose_name="Lugar de la actividad")
    description = TextField(verbose_name="Descripcion de la actividad")
    reason = TextField(verbose_name="Motivo para realizar la actividad")
    beneficiaries = IntegerField(verbose_name="Cantidad de personas beneficiadas")

    def __str__(self):
        return f"{self.activity_type} on {self.date}"

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        db_table = "gc_social_activities"
        verbose_name = "Actividad social"
        verbose_name_plural = "Actividades sociales"
        ordering = ["activity_type"]
