from django.db import models


class RegistroFilmico(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    camara = models.CharField(max_length=50, blank=True, null=True)
    motivo_solicitud = models.CharField(max_length=400)
    ente_solicita = models.CharField(max_length=50, blank=True, null=True)
    fecha_solicitud = models.DateField(blank=True, null=True)
    fecha_culminacion = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "registro_filmico"
        verbose_name_plural = "registro_filmicos"

    def __str__(self):
        return self.camara
