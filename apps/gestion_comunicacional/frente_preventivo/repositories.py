from helpers.RepositoryMixin import Repository

from gestion_comunicacional.frente_preventivo.models import FrentePreventivo


class FrentePreventivoRepository(Repository):
    def __init__(self):
        self.entity = FrentePreventivo
