from helpers.CrudMixin import CrudService

from rrhh.empleados.repositories import EmpleadoRepository


class EmpleadoService(CrudService):
    def __init__(self):
        self.repository = EmpleadoRepository()
