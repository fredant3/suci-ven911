from helpers.RepositoryMixin import Repository

from .models import TipoSueldo


class TipoSueldoRepository(Repository):
    def __init__(self):
        self.entity = TipoSueldo
