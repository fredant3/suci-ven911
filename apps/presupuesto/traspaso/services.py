from presupuesto.traspaso.repositories import TraspasoRepository
from helpers.CrudMixin import CrudService


class TraspasoService(CrudService):
    def __init__(self):
        self.repository = TraspasoRepository()
