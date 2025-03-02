from helpers.CrudMixin import CrudService

from presupuesto.acciones.repositories import AccionRepository
from django.db.models import Q


class AccionService(CrudService):
    def __init__(self):
        self.repository = AccionRepository()

    def criteria(self, search):
        query = Q()

        if search:
            query &= Q(proyecto__icontains=search)

        return query
