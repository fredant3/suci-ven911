from administracion.departamentos.repositories import DepartamentoRepository
from helpers.CrudMixin import CrudService


class DepartamentoService(CrudService):
    def __init__(self):
        self.repository = DepartamentoRepository()
