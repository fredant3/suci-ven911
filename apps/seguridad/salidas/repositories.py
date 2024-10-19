from helpers.RepositoryMixin import Repository

from .models import Salida


class SalidaRepository(Repository):
    def __init__(self):
        self.entity = Salida
