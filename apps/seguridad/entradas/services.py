from helpers.CrudMixin import CrudService

from seguridad.entradas.repositories import EntradaRepository


class EntradaService(CrudService):
    def __init__(self):
        self.repository = EntradaRepository()
