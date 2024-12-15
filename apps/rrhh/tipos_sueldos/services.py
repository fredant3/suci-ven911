from helpers.CrudMixin import CrudService

from .repositories import TipoSueldoRepository


class TipoSueldoService(CrudService):
    def __init__(self):
        self.repository = TipoSueldoRepository()
