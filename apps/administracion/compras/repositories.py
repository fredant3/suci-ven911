from administracion.compras.model import Compra
from helpers.RepositoryMixin import Repository


class AsignacionRepository(Repository):
    def __init__(self):
        self.entity = Compra
