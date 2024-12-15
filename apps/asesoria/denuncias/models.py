from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Denunciante(BaseModel):
    nombres = models.CharField("Nombre del denunciante", max_length=120)
    apellidos = models.CharField("Apellido del denunciante", max_length=120)
    cedula = models.CharField("Cédula del denunciante", max_length=12)
    telefono = models.CharField("Teléfono del denunciante", max_length=15)
    email = models.EmailField(
        "Correo electrónico del denunciante", max_length=60, blank=True, null=True
    )
    direccion = models.CharField("Dirección del denunciante", max_length=180)

    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"

    class Meta:
        verbose_name = "Denunciante"
        verbose_name_plural = "Denunciantes"


class Denunciado(BaseModel):
    nombres = models.CharField(
        "Nombre del denunciado", max_length=120, blank=True, null=True
    )
    apellidos = models.CharField(
        "Apellido del denunciado", max_length=120, blank=True, null=True
    )
    cedula = models.CharField(
        "Cédula del denunciado", max_length=12, blank=True, null=True
    )
    telefono = models.CharField(
        "Teléfono del denunciado", max_length=15, blank=True, null=True
    )
    email = models.EmailField(
        "Correo electrónico del denunciado", max_length=60, blank=True, null=True
    )
    direccion = models.CharField(
        "Dirección del denunciado", max_length=180, blank=True, null=True
    )

    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = "Denunciado"
        verbose_name_plural = "Denunciados"


class Denuncia(BaseModel):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    ente = models.CharField(max_length=50, blank=True, null=True)
    denunciante = models.ForeignKey(Denunciante, on_delete=models.CASCADE)
    denunciado = models.ForeignKey(Denunciado, on_delete=models.CASCADE)
    motivo = models.TextField(max_length=400)
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
        verbose_name = "Denuncia"
        verbose_name_plural = "Denuncias"
