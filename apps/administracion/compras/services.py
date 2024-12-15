from administracion.compras.repositories import CompraRepository
from helpers.CrudMixin import CrudService


class CompraService(CrudService):
    def __init__(self):
        self.repository = CompraRepository()
