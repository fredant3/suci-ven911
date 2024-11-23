from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from rrhh.empleados.models import Empleado
from rrhh.tipos_sueldos.models import TipoSueldo

ESTATUS_CHOICES = (
    ("pendiente", "Por Pagar"),
    ("pagado", "Pago completado"),
    ("suspendido", "Suspendido"),
)


class Sueldo(BaseModel):
    estatus = models.CharField(max_length=10, choices=ESTATUS_CHOICES)
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "sueldo"
        verbose_name_plural = "sueldos"


class SueldoDetalle(BaseModel):
    tipo_sueldo = models.ForeignKey(TipoSueldo, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    sueldo = models.ForeignKey(Sueldo, on_delete=models.CASCADE)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "detalles del sueldo"
        verbose_name_plural = "destalles de los sueldos"
