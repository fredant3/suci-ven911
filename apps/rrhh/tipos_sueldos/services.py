from helpers.CrudMixin import CrudService

from rrhh.tipos_sueldos.repositories import TipoSueldoRepository


class TipoSueldoService(CrudService):
    def __init__(self):
        self.repository = TipoSueldoRepository()
