from django.db.models import Q
from helpers.CrudMixin import CrudService
from gestion_comunicacional.repositories import GestioncomunicacionalRepository

# from emergencia.incidencias.repositories import TipoIncidenciaRepository
# from emergencia.organismo.repositories import OrganismoRepository


class GestioncomunicacionalService(CrudService):

    select = (
        "id",
        "nombre__actividad",
        "actividad__realizada",
        "descripcion__actividad",
        "created_by",
    )

    def __init__(self):
        self.repository = GestioncomunicacionalRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(gestioncomunicacional__nombre_actividad__icontains=search)
                | Q(gestioncomunicacional__actividad_realizada__icontains=search)
                | Q(gestioncomunicacional__descripcion_actividad__icontains=search)
            )

        return query
