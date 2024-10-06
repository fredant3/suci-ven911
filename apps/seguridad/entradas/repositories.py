from helpers.RepositoryMixin import Repository

from .models import Entrada


class EntradaRepository(Repository):
    def __init__(self):
        self.entity = Entrada
