from helpers.CrudMixin import CrudService

from .repositories import RegistroFilmicoRepository


class RegistroFilmicoService(CrudService):
    def __init__(self):
        self.repository = RegistroFilmicoRepository()
