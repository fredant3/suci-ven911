from administracion.departamentos.models import Departamento
from administracion.sedes.models import Sede
from django.db.models import CharField, ForeignKey, CASCADE, DateField, BooleanField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from rrhh.cargos.models import Cargo
from rrhh.empleados.models import Empleado
from rrhh.tipos_empleados.models import TipoEmpleado
from helpers.models import BOOLEAN_CHOICES

TIPO_CONTRATOS_CHOICES = (
    ("pasante", "Pasante"),
    ("prueba", "Periodo de Prueba"),
    ("contrato", "Contratado"),
    ("fijo", "Personal Fijo"),
)


class Contrato(BaseModel):
    tipo = CharField("Tipo de contrato", max_length=8, choices=TIPO_CONTRATOS_CHOICES)
    comision_servicio = BooleanField(
        "Comision Servicio", choices=BOOLEAN_CHOICES, default=BOOLEAN_CHOICES[1]
    )
    pnb = BooleanField("PNB", choices=BOOLEAN_CHOICES, default=BOOLEAN_CHOICES[1])
    departamento = ForeignKey(
        Departamento, on_delete=CASCADE, verbose_name="Departamento"
    )
    tipo_personal = ForeignKey(
        TipoEmpleado, on_delete=CASCADE, verbose_name="Tipo de personal"
    )
    cargo = ForeignKey(Cargo, on_delete=CASCADE, verbose_name="Cargo asignado")
    sede = ForeignKey(Sede, on_delete=CASCADE, verbose_name="Sede")
    fecha_ingreso_911 = DateField("Fecha de ingreso al Ven-911")
    fecha_ingreso_apn = DateField("Fecha de ingreso APN")
    fasmij = BooleanField("Fasmij", choices=BOOLEAN_CHOICES, default=BOOLEAN_CHOICES[1])
    fecha_ingreso = DateField("Fecha de ingreso")
    fecha_culminacion = DateField("Fecha de culminacion", null=True, blank=True)
    empleado = ForeignKey(
        Empleado, on_delete=CASCADE, verbose_name="Nombre del empleado"
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
