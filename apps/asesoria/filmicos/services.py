from asesoria.filmicos.repositories import RegistroFilmicoRepository
from helpers.CrudMixin import CrudService


class RegistroFilmicoService(CrudService):
    def __init__(self):
        self.repository = RegistroFilmicoRepository()
