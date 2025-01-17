from administracion.averia.repositories import AveriaRepository
from helpers.CrudMixin import CrudService


class AveriaService(CrudService):
    def __init__(self):
        self.repository = AveriaRepository()
