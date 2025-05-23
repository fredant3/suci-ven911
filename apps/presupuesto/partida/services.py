from helpers.CrudMixin import CrudService
from presupuesto.partida.repositories import PartidaRepository
from django.db.models import Q


class PartidaService(CrudService):
    def __init__(self):
        self.repository = PartidaRepository()

    def criteria(self, search, arg=None):
        query = Q()
        if search:
            query &= Q(codigo__icontains=search) | Q(titulo__icontains=search)
        return query
