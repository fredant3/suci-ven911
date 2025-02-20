from helpers.CrudMixin import CrudService

from rrhh.educaciones.repositories import EducacionRepository


class EducacionService(CrudService):
    def __init__(self):
        self.repository = EducacionRepository()
