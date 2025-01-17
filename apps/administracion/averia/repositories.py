from administracion.averia.models import Averia, TipoAveria
from helpers.RepositoryMixin import Repository


class TipoAveriaRepository(Repository):
    def __init__(self):
        self.entity = TipoAveria


class AveriaRepository(Repository):
    def __init__(self):
        self.entity = Averia
