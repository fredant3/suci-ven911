from helpers.CrudMixin import CrudService

from .repositories import NormativaRepository


class NormativaService(CrudService):
    def __init__(self):
        self.repository = NormativaRepository()
