from helpers.RepositoryMixin import Repository

from .models import Asignacion


class AsignacionRepository(Repository):
    def __init__(self):
        self.entity = Asignacion
