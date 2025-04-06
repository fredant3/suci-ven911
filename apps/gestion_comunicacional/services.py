from django.db.models import Q
from helpers.CrudMixin import CrudService
from gestion_comunicacional.repositories import GestioncomunicacionalRepository

# from emergencia.incidencias.repositories import TipoIncidenciaRepository
# from emergencia.organismo.repositories import OrganismoRepository


class GestioncomunicacionalService(CrudService):
    def __init__(self):
        self.repository = GestioncomunicacionalRepository()
