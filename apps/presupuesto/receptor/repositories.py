from helpers.RepositoryMixin import Repository

from .models import Receptor


class ReceptorRepository(Repository):
    def __init__(self):
        self.entity = Receptor
