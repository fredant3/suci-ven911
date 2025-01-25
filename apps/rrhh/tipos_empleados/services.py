from helpers.CrudMixin import CrudService

from .repositories import TipoEmpleadoRepository


class TipoEmpleadoService(CrudService):
    def __init__(self):
        self.repository = TipoEmpleadoRepository()
