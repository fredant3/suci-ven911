from helpers.CrudMixin import CrudService

from rrhh.contratos.repositories import ContratoRepository
from rrhh.empleados.repositories import EmpleadoRepository
from rrhh.tipos_empleados.repositories import TipoEmpleadoRepository
from administracion.departamentos.repositories import DepartamentoRepository
from administracion.sedes.repositories import SedeRepository
from rrhh.cargos.repositories import CargoRepository


class ContratoService(CrudService):
    def __init__(self):
        self.repository = ContratoRepository()
        self.departamento_repository = DepartamentoRepository()
        self.tipo_personal_repository = TipoEmpleadoRepository()
        self.empleado_repository = EmpleadoRepository()
        self.cargo_repository = CargoRepository()
        self.sede_repository = SedeRepository()

    def search_departamento(self, id):
        return self.departamento_repository.getById(id)

    def search_tipo_empleado(self, id):
        return self.tipo_personal_repository.getById(id)

    def search_empleado(self, id):
        return self.empleado_repository.getById(id)

    def search_cargo(self, id):
        return self.cargo_repository.getById(id)

    def search_sede(self, id):
        return self.sede_repository.getById(id)

    def relationship(self, payload, *arg, **kwargs):
        payload["empleado"] = self.search_empleado(payload.get("empleado"))
        payload["tipo_personal"] = self.search_tipo_empleado(
            payload.get("tipo_personal")
        )
        payload["departamento"] = self.search_departamento(payload.get("departamento"))
        payload["cargo"] = self.search_cargo(payload.get("cargo"))
        payload["sede"] = self.search_sede(payload.get("sede"))

        return payload
