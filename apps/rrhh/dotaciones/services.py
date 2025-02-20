from helpers.CrudMixin import CrudService

from rrhh.dotaciones.repositories import DotacionRepository


class DotacionService(CrudService):
    def __init__(self):
        self.repository = DotacionRepository()
