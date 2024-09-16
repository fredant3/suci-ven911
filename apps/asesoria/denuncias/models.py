from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Denuncia(BaseModel):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    ente = models.CharField(max_length=50, blank=True, null=True)
    nombres_d = models.CharField(max_length=50, verbose_name="Nombre del denunciante")
    apellidos_d = models.CharField(
        max_length=50, verbose_name="Apellido del denunciante"
    )
    cedula_d = models.CharField(max_length=50, verbose_name="Cédula del denunciante")
    telefono = models.CharField(max_length=11, verbose_name="Teléfono del denunciante")
    email = models.EmailField(blank=True, null=True, verbose_name="Correo electrónico")
    direccion_d = models.CharField(max_length=150, verbose_name="Dirección")
    nombres_denunciado = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Nombre del denunciado"
    )
    apellidos_denunciado = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Apellido del denunciado"
    )
    cedula_denunciado = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Cédula del denunciado"
    )
    motivo = models.CharField(max_length=400)
    zona = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Zona del incidente"
    )
    fecha_denuncia = models.DateField(verbose_name="Fecha de la denuncia")
    fecha_incidente = models.DateField(
        blank=True, null=True, verbose_name="Fecha del incidente"
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.ente

    class Meta:
        verbose_name = "denuncia"
        verbose_name_plural = "denuncias"
