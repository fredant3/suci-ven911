from helpers.CrudMixin import CrudService

from presupuesto.cedente.repositories import CedenteRepository
from django.db.models import Q


class CedenteService(CrudService):
    def __init__(self):
        self.repository = CedenteRepository()

    def criteria(self, search):
        query = Q()

        if search:
            query &= Q(idc__icontains=search) | Q(espefc__icontains=search)

        return query
