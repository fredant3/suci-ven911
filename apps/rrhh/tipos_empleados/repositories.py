from helpers.RepositoryMixin import Repository

from .models import TipoEmpleado


class TipoEmpleadoRepository(Repository):
    def __init__(self):
        self.entity = TipoEmpleado
