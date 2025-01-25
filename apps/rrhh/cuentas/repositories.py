from helpers.RepositoryMixin import Repository

from .models import Cuenta


class CuentaRepository(Repository):
    def __init__(self):
        self.entity = Cuenta
