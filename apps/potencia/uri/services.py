from helpers.CrudMixin import CrudService
from potencia.uri.repositories import UriRepository


class UriService(CrudService):
    def __init__(self):
        self.repository = UriRepository()
