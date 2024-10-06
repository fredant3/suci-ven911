from helpers.RepositoryMixin import Repository

from .models import Departamento


class DepartamentoRepository(Repository):
    def __init__(self):
        self.entity = Departamento
