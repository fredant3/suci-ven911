from administracion.inventario.models import Articulo
from helpers.RepositoryMixin import Repository


class InventarioRepository(Repository):
    def __init__(self):
        self.entity = Articulo
