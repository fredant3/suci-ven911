from helpers.CrudMixin import CrudService

from .repositories import ReceptorRepository


class ReceptorService(CrudService):
    def __init__(self):
        self.repository = ReceptorRepository()
