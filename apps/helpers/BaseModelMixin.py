from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.timezone import get_current_timezone


class BaseModelManager(models.Manager):
    def get_queryset(self):
        # return super().get_queryset().exclude(deleted=True)
        pass


class BaseModel(models.Model):
    objects = BaseModelManager()

    created_by = models.CharField(verbose_name="Creado por", max_length=6)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_by = models.CharField(verbose_name="Actualizado por", max_length=6)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")
    deleted_by = models.CharField(
        verbose_name="Eliminado por", max_length=6, null=True, blank=True
    )
    deleted_at = models.DateTimeField(
        verbose_name="Eliminado el", null=True, blank=True
    )

    def all(self):
        # return self.exclude(deleted=True)
        pass

    def delete(self):
        self.deleted_at = datetime.now(tz=get_current_timezone())
        self.save()

    def hard_delete(self):
        return super().delete()

    class Meta:
        abstract = True
