from helpers.RepositoryMixin import Repository

from .models import Proyecto


class ProyectoRepository(Repository):
    def __init__(self):
        self.entity = Proyecto
