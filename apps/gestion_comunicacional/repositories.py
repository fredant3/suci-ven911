from helpers.RepositoryMixin import Repository

from gestion_comunicacional.models import Gestion_comunicacional


class GestioncomunicacionalRepository(Repository):
    def __init__(self):
        self.entity = Gestion_comunicacional
