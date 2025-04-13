from django.db.models import Q
from helpers.CrudMixin import CrudService
from gestion_comunicacional.frente_preventivo.repositories import (
    FrentePreventivoRepository,
)

# from emergencia.incidencias.repositories import TipoIncidenciaRepository
# from emergencia.organismo.repositories import OrganismoRepository


class FrentePreventivoService(CrudService):

    def __init__(self):
        self.repository = FrentePreventivoRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(donde_desarrollo__icontains=search)
                | Q(personas_beneficiadas__icontains=search)
                | Q(tipo_actividad__icontains=search)
            )

        return query
