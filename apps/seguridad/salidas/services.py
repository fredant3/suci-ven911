from helpers.CrudMixin import CrudService

from .repositories import SalidaRepository


class SalidaService(CrudService):
    def __init__(self):
        self.repository = SalidaRepository()
