from helpers.CrudMixin import CrudService

from presupuesto.acciones.repositories import AccionRepository


class AccionService(CrudService):
    def __init__(self):
        self.repository = AccionRepository()
