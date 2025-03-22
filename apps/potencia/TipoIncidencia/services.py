from potencia.TipoIncidencia.repositories import TipoIncidencaRepository
from helpers.CrudMixin import CrudService
from django.db.models import Q


class TipoIncidenciaService(CrudService):
    def __init__(self):
        self.repository = TipoIncidenciaRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= Q(nombre__icontains=search)

        return query
