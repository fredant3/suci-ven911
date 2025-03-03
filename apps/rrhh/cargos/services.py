from helpers.CrudMixin import CrudService

from rrhh.cargos.repositories import CargoRepository
from django.db.models import Q


class CargoService(CrudService):
    def __init__(self):
        self.repository = CargoRepository()

    def criteria(self, search):
        query = Q()

        if search:
            query &= Q(cargo__icontains=search)

        return query
