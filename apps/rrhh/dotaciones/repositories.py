from helpers.RepositoryMixin import Repository

from .models import Dotacion


class DotacionRepository(Repository):
    def __init__(self):
        self.entity = Dotacion
