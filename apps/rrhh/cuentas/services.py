from helpers.CrudMixin import CrudService

from .repositories import CuentaRepository


class CuentaService(CrudService):
    def __init__(self):
        self.repository = CuentaRepository()
