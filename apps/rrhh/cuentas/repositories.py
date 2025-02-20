from helpers.RepositoryMixin import Repository

from rrhh.cuentas.models import Cuenta


class CuentaRepository(Repository):
    def __init__(self):
        self.entity = Cuenta
