from helpers.CrudMixin import CrudService
from rrhh.cuentas.repositories import CuentaRepository
from rrhh.empleados.models import Empleado  # Importar modelo Empleado
from rrhh.empleados.repositories import EmpleadoRepository


class CuentaService(CrudService):
    select = (
        "id",
        "banco",
        "tipo",
        "numero_cuenta",
        "pago_movil",
        "telefono",
        "empleado__nombres",
    )

    def __init__(self):
        self.repository = CuentaRepository()
        self.empleado_repository = EmpleadoRepository()

    def buscar_empleado(self, empleado_id):
        return self.empleado_repository.getById(empleado_id)

    def relationship(self, payload, *arg, **kwargs):
        payload["empleado"] = self.buscar_empleado(payload.get("empleado"))
        return payload
