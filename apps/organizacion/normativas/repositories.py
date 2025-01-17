from helpers.RepositoryMixin import Repository

from .models import Normativa

class NormativaRepository(Repository):
    def __init__(self):
        self.entity = Normativa
