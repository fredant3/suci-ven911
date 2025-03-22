from helpers.CrudMixin import CrudService

from rrhh.tipos_empleados.repositories import TipoEmpleadoRepository
from django.db.models import Q


class TipoEmpleadoService(CrudService):
    def __init__(self):
        self.repository = TipoEmpleadoRepository()

    def criteria(self, search):
        query = Q()

        if search:
            query &= Q(tipo_personal__icontains=search)

        return query
