from helpers.RepositoryMixin import Repository

from .models import Familiar


class FamiliarRepository(Repository):
    def __init__(self):
        self.entity = Familiar
