from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.timezone import get_current_timezone


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(deleted=True)


class BaseModel(models.Model):
    objects = BaseModelManager()

    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name="Creado por",
        on_delete=models.CASCADE,
        related_name="%(class)s_created",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name="Actualizado por",
        on_delete=models.CASCADE,
        related_name="%(class)s_updated",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Actualizado el",
    )
    deleted = models.BooleanField(default=False, verbose_name="Está eliminado")
    deleted_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name="Eliminado por",
        on_delete=models.CASCADE,
        related_name="%(class)s_delete",
        null=True,
        blank=True,
    )
    deleted_at = models.DateTimeField(
        verbose_name="Eliminado el",
        null=True,
        blank=True,
    )

    def all(self):
        return self.exclude(deleted=True)

    def delete(self):
        self.deleted = True
        self.deleted_at = datetime.now(tz=get_current_timezone())
        self.save()

    def hard_delete(self):
        return super().delete()

    class Meta:
        abstract = True
