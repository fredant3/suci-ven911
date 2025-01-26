from rrhh.cargos.models import Cargo
from rrhh.contratos.models import Contrato
from rrhh.cuentas.models import Cuenta
from rrhh.dotaciones.models import Dotacion
from rrhh.educaciones.models import Educacion
from rrhh.empleados.models import Empleado
from rrhh.familiares.models import Familiar
from rrhh.sueldos.models import Sueldo
from rrhh.tipos_empleados.models import TipoEmpleado
from rrhh.tipos_sueldos.models import TipoSueldo

__all__ = [
    "Cargo",
    "Empleado",
    "TipoEmpleado",
    "Contrato",
    "Educacion",
    "Dotacion",
    "Familiar",
    "Cuenta",
    "TipoSueldo",
    "Sueldo",
]
