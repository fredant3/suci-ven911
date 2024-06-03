from django.db import models


class SocialMediaAccountEntity(models.Model):
    PLATFORM_CHOICES = [
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram"),
        ("Twitter", "Twitter"),
    ]

    platform = models.CharField(
        max_length=50, verbose_name="Plataforma", choices=PLATFORM_CHOICES
    )
    username = models.CharField(max_length=60, verbose_name="Nombre de usuario")
    url = models.URLField(verbose_name="Direccion web")
    followers = models.PositiveSmallIntegerField("Seguidores")
    responsible = models.CharField(
        max_length=100, verbose_name="Quien administra la red"
    )
    publications = models.PositiveSmallIntegerField("Publicaciones")

    def __str__(self):
        return f"{self.platform} - {self.username}"

    class Meta:
        db_table = "social_media_accounts"
