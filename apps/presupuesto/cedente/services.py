from helpers.CrudMixin import CrudService

from presupuesto.cedente.repositories import CedenteRepository


class CedenteService(CrudService):
    def __init__(self):
        self.repository = CedenteRepository()
