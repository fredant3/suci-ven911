from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Cedente(BaseModel):
    idc = models.CharField(max_length=100, verbose_name="Id Cedente:")
    partidac = models.CharField(max_length=64, verbose_name="Partida")
    generalc = models.CharField(max_length=64, verbose_name="General")
    espefc = models.CharField(max_length=64, verbose_name="Específicaciones")
    subespefc = models.CharField(max_length=64, verbose_name="Sub-Especialidad")
    denomc = models.CharField(max_length=64, verbose_name="Denomincación")
    presuacorc = models.CharField(max_length=64, verbose_name="Presupuesto acordado")
    caufechac = models.CharField(max_length=64, verbose_name="Causado a la fecha")
    dispc = models.CharField(max_length=64, verbose_name="Disponible a causar")
    montocc = models.CharField(max_length=64, verbose_name="Monto a ceder")
    saldofc = models.CharField(max_length=64, verbose_name="Saldo final")
    direccionc = models.CharField(max_length=64, verbose_name="Dirección cedente")
    permissions = [
        ("listar_cedente", "Puede listar cedente"),
        ("agregar_cedente", "Puede agregar cedente"),
        ("ver_cedente", "Puede ver cedente"),
        ("editar_cedente", "Puede actualizar cedente"),
        ("eliminar_cedente", "Puede eliminar cedente"),
        ("pdf_cedente", "Puede generar pdf de cedente"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.partidac, self.generalc)

    class Meta:
        verbose_name = "Cedente"
        verbose_name_plural = "Cedentes"
