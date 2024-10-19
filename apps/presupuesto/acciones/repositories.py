from helpers.RepositoryMixin import Repository

from .models import Accion


class AccionRepository(Repository):
    def __init__(self):
        self.entity = Accion
