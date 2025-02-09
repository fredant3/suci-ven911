from helpers.CrudMixin import CrudService

from .repositories import LlamadaRepository


class LlamadaService(CrudService):
    def __init__(self):
        self.repository = LlamadaRepository()
