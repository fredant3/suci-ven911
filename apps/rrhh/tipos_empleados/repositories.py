from helpers.RepositoryMixin import Repository

from rrhh.tipos_empleados.models import TipoEmpleado


class TipoEmpleadoRepository(Repository):
    def __init__(self):
        self.entity = TipoEmpleado
