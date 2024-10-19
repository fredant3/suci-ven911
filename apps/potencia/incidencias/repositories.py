from helpers.RepositoryMixin import Repository

from .models import Incidencia


class IncidenciaRepository(Repository):
    def __init__(self):
        self.entity = Incidencia
