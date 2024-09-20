from helpers.CrudMixin import CrudService

from .repositories import ReglamentoRepository


class ReglamentoService(CrudService):
    def __init__(self):
        self.repository = ReglamentoRepository()
