from administracion.departamentos.models import Departamento
from administracion.sedes.models import Sede
from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from rrhh.cargos.models import Cargo
from rrhh.empleados.models import Empleado
from rrhh.tipos_empleados.models import TipoEmpleado

TIPO_CONTRATOS_CHOICES = (
    ("pasante", "Pasante"),
    ("prueba", "Periodo de Prueba"),
    ("contrato", "Contratado"),
    ("fijo", "Personal Fijo"),
)


class Contrato(BaseModel):
    tipo = models.CharField(max_length=8, choices=TIPO_CONTRATOS_CHOICES)
    comision_servicio = models.BooleanField()
    pnb = models.BooleanField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    tipo_personal = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    fecha_ingreso_911 = models.DateField()
    fecha_ingreso_apn = models.DateField()
    fasmij = models.BooleanField()
    fecha_ingreso = models.DateField()
    fecha_culminacion = models.DateField(null=True, blank=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "contrato"
        verbose_name_plural = "contratos"
