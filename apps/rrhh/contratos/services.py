from helpers.CrudMixin import CrudService

from .repositories import ContratoRepository


class ContratoService(CrudService):
    def __init__(self):
        self.repository = ContratoRepository()
