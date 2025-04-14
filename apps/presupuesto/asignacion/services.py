from helpers.CrudMixin import CrudService

from presupuesto.asignacion.repositories import AsignacionRepository
from django.db.models import Q


class AsignacionService(CrudService):
    def __init__(self):
        self.repository = AsignacionRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= Q(departamento__icontains=search) | Q(objetivo__icontains=search)

        return query
