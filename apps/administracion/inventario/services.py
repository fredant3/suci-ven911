from administracion.inventario.repositories import InventarioRepository
from django.db.models import Q
from helpers.CrudMixin import CrudService


class InventarioService(CrudService):
    def __init__(self):
        self.repository = InventarioRepository()
