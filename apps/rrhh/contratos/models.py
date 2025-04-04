from administracion.departamentos.models import Departamento
from administracion.sedes.models import Sede
from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from rrhh.cargos.models import Cargo
from rrhh.empleados.models import Empleado

TIPO_CONTRATOS_CHOICES = (
    ("pasante", "Pasante"),
    ("prueba", "Periodo de Prueba"),
    ("contrato", "Contratado"),
    ("fijo", "Personal Fijo"),
)


class Contrato(BaseModel):
    tipo = models.CharField(
        "Tipo de contrato", max_length=8, choices=TIPO_CONTRATOS_CHOICES
    )
    comision_servicio = models.BooleanField("Comision servicio", default=False)
    pnb = models.BooleanField("Funcionario PNB", default=False)
    departamento = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, verbose_name="Departamento"
    )
    cargo = models.ForeignKey(
        Cargo, on_delete=models.CASCADE, verbose_name="Cargo asignado"
    )
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="Sede")
    fecha_ingreso_911 = models.DateField("Fecha de ingreso al Ven-911")
    fecha_ingreso_apn = models.DateField("Fecha de ingreso APN")
    fasmij = models.BooleanField(default=False)
    fecha_ingreso = models.DateField("Fecha de ingreso")
    fecha_culminacion = models.DateField("Fecha de culminacion", null=True, blank=True)
    empleado = models.ForeignKey(
        Empleado, on_delete=models.CASCADE, verbose_name="Nombre del empleado"
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "contrato"
        verbose_name_plural = "contratos"
        permissions = [
            ("listar_contrato", "Puede listar contratos"),
            ("agregar_contrato", "Puede agregar contrato"),
            ("ver_contrato", "Puede ver contrato"),
            ("editar_contrato", "Puede actualizar contrato"),
            ("eliminar_contrato", "Puede eliminar contrato"),
            ("exel_contrato", "Puede exportar contrato a excel"),
        ]
