from helpers.CrudMixin import CrudService

from .repositories import TransporteRepository


class TransporteService(CrudService):
    def __init__(self):
        self.repository = TransporteRepository()
