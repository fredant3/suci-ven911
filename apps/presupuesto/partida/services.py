from django.forms import ValidationError
from presupuesto.partida.repositories import PartidaRepository
from presupuesto.cedente.models import Cedente
from presupuesto.receptor.models import Receptor
from django.db.models import Q
from helpers.CrudMixin import CrudService


class PartidaService(CrudService):
    def __init__(self):
        self.repository = PartidaRepository()

    def criteria(self, search, arg=None):
        query = Q()
        if search:
            query &= Q(codigo__icontains=search) | Q(titulo__icontains=search)
        return query
