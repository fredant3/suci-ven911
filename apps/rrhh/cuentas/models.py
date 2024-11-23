from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from rrhh.empleados.models import Empleado

TIPO_BANCO_CHOICES = (
    ("0001", "0001 - Banco Central de Venezuela"),
    ("0102", "0102 - Banco de Venezuela"),
    ("0104", "0104 - Banco Venezolano de Crédito"),
    ("0105", "0105 - Mercantil Banco"),
    ("0108", "0108 - BBVA Provincial"),
    ("0114", "0114 - Bancaribe"),
    ("0115", "0115 - Banco Exterior"),
    ("0116", "0116 - Banco Occidental de Descuento"),
    ("0128", "0128 - Banco Caroní"),
    ("0134", "0134 - Banesco"),
    ("0137", "0137 - Banco Sofitasa"),
    ("0138", "0138 - Banco Plaza"),
    ("0146", "0146 - Banco de la Gente Emprendedora"),
    ("0151", "0151 - Banco Fondo Común"),
    ("0156", "0156 - 100% Banco"),
    ("0157", "0157 - DelSur"),
    ("0163", "0163 - Banco del Tesoro"),
    ("0166", "0166 - Banco Agrícola de Venezuela"),
    ("0168", "0168 - Bancrecer"),
    ("0169", "0169 - Mi Banco"),
    ("0171", "0171 - Banco Activo"),
    ("0172", "0172 - Bancamiga"),
    ("0173", "0173 - Banco Internacional de Desarrollo"),
    ("0174", "0174 - Banplus"),
    ("0175", "0175 - Banco Bicentenario"),
    ("0177", "0177 - Banco de la Fuerza Armada Nacional Bolivariana"),
    ("0178", "0178 - N58 Banco Digital"),
    ("0190", "0190 - Citibank"),
    ("0191", "0191 - Banco Nacional de Crédito"),
    ("0601", "0601 - Instituto Municipal de Crédito Popular"),
)

TIPO_CUEMTA_CHOICES = (
    ("cor", "Cuenta Corriente"),
    ("aho", "Cuenta de Ahorros"),
)


class Cuenta(BaseModel):
    banco = models.CharField(max_length=4, choices=TIPO_BANCO_CHOICES)
    tipo = models.CharField(max_length=3, choices=TIPO_CUEMTA_CHOICES)
    numero_cuenta = models.CharField(max_length=30)
    cedula = models.IntegerField()
    pago_movil = models.BooleanField()
    telefono = models.CharField(max_length=12)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "cuenta"
        verbose_name_plural = "cuentas"
