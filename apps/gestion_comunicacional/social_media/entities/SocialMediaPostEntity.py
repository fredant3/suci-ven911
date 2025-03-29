from django.db import models

from .SocialMediaAccountEntity import SocialMediaAccountEntity


class SocialMediaPostEntity(models.Model):
    POST_TYPE_CHOICES = [
        ("reel", "Reel"),
        ("post", "Post"),
        ("story", "Story"),
        ("picture", "Picture"),
    ]

    STATUS_CHOICES = [
        ("published", "Published"),  # Publicado
        ("scheduled", "Scheduled"),  # Programado
        ("draft", "Draft"),  # Borrador
    ]

    account = models.ForeignKey(SocialMediaAccountEntity, verbose_name="Cuenta", on_delete=models.CASCADE)
    post_type = models.CharField(max_length=50, verbose_name="Tipo de publicacion", choices=POST_TYPE_CHOICES)
    content = models.TextField(verbose_name="Contenido")
    publish_date = models.DateField(verbose_name="Fecha de publicacion")
    status = models.CharField(max_length=50, verbose_name="Estatus", choices=STATUS_CHOICES)
    reach = models.IntegerField(verbose_name="Alcance de la publicación")

    def __str__(self):
        return f"{self.post_type} - {self.status}"

    class Meta:
        db_table = "gc_social_media_posts"
        verbose_name = "Publicacion de red social"
        verbose_name_plural = "Publicaciones de redes sociales"
        ordering = ["account"]
