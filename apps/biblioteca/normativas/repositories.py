from helpers.RepositoryMixin import Repository

from .models import Denuncia


class DenunciaRepository(Repository):
    def __init__(self):
        self.entity = Denuncia
