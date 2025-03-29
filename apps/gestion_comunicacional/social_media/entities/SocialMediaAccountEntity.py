from index.mixins.BaseModelMixin import BaseModel

from django.db.models import CharField, PositiveSmallIntegerField, URLField
from django.forms import model_to_dict


class SocialMediaAccountEntity(BaseModel):
    PLATFORM_CHOICES = [
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram"),
        ("Twitter", "Twitter"),
    ]

    platform = CharField(max_length=50, verbose_name="Red social", choices=PLATFORM_CHOICES)
    username_sm = CharField(max_length=60, verbose_name="Nombre de usuario de la red social", unique=True)
    url = URLField(verbose_name="Direccion web", unique=True)
    followers = PositiveSmallIntegerField("Seguidores")
    responsible = CharField(max_length=100, verbose_name="Responsable de la red social")
    publications = PositiveSmallIntegerField("Publicaciones")

    def __str__(self):
        return f"red social: {self.platform}@{self.username_sm}"

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        db_table = "gc_social_media_accounts"
        verbose_name = "Red social"
        verbose_name_plural = "Redes sociales"
        ordering = ["platform"]
