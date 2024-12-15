from helpers.CrudMixin import CrudService

from .repositories import GestionRepository


class GestionService(CrudService):
    def __init__(self):
        self.repository = GestionRepository()
