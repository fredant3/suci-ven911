from django.db.models import Q
from helpers.CrudMixin import CrudService

from gestion_comunicacional.repositories import Gestion_comunicacionalRepository


class EmergenciaService(CrudService):
    def __init__(self):
        self.repository = Gestion_comunicacionalRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= Q(nombre__actividad__icontains=search)

        return query
