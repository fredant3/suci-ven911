from helpers.CrudMixin import CrudService

from rrhh.familiares.repositories import FamiliarRepository


class FamiliarService(CrudService):
    def __init__(self):
        self.repository = FamiliarRepository()
