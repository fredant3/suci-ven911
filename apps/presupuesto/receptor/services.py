from helpers.CrudMixin import CrudService

from presupuesto.receptor.repositories import ReceptorRepository


class ReceptorService(CrudService):
    def __init__(self):
        self.repository = ReceptorRepository()
