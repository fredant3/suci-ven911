from administracion.compras.repositories import CompraRepository
from django.db.models import Q
from helpers.CrudMixin import CrudService


class CompraService(CrudService):
    def __init__(self):
        self.repository = CompraRepository()
