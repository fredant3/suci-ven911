from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES


class Infraestructura(BaseModel):
    mes = models.CharField(max_length=64, verbose_name="Mes:", default="")
    estado = models.CharField(
        "Estado", name="estado", max_length=2, choices=ESTADOS_CHOICES
    )
    infraestructura = models.CharField(
        max_length=64, verbose_name="Infraestrutuctura:", default=""
    )
    cantidad = models.CharField(max_length=64, verbose_name="Cantidad:", default="")
    permissions = [
        ("listar_infraestructura", "Puede listar infraestructura"),
        ("agregar_infraestructura", "Puede agregar infraestructura"),
        ("ver_infraestructura", "Puede ver infraestructura"),
        ("editar_infraestructura", "Puede actualizar infraestructura"),
        ("eliminar_infraestructura", "Puede eliminar infraestructura"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.ente

    class Meta:
        verbose_name = "infraestructura"
        verbose_name_plural = "infraestructuras"
