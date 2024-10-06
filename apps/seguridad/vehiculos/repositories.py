from helpers.RepositoryMixin import Repository

from .models import Vehiculo


class VehiculoRepository(Repository):
    def __init__(self):
        self.entity = Vehiculo
