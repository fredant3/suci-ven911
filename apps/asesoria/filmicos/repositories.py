from helpers.RepositoryMixin import Repository

from .models import RegistroFilmico


class RegistroFilmicoRepository(Repository):
    def __init__(self):
        self.entity = RegistroFilmico
