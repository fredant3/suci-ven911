from helpers.CrudMixin import CrudService

from rrhh.tipos_empleados.repositories import TipoEmpleadoRepository


class TipoEmpleadoService(CrudService):
    def __init__(self):
        self.repository = TipoEmpleadoRepository()
