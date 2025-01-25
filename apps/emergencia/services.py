from helpers.CrudMixin import CrudService

from .repositories import EmergenciaRepository


class EmergenciaService(CrudService):
    def __init__(self):
        self.repository = EmergenciaRepository()
