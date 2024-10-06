from helpers.RepositoryMixin import Repository

from .models import Educacion


class EducacionRepository(Repository):
    def __init__(self):
        self.entity = Educacion
