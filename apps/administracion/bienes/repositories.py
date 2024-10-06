from helpers.RepositoryMixin import Repository

from .models import Bien


class BienRepository(Repository):
    def __init__(self):
        self.entity = Bien
