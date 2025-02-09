from helpers.CrudMixin import CrudService
from .repositories import EmergenciaRepository
from emergencia.incidencias.repositories import TipoIncidenciaRepository
from emergencia.organismo.repositories import OrganismoRepository


class EmergenciaService(CrudService):
    def __init__(self):
        self.repository = EmergenciaRepository()
        self.repositoryIncidence = TipoIncidenciaRepository()
        self.repositoryOrganismo = OrganismoRepository()

    def search_type_incidences(self, id):
        search = self.repositoryIncidence.getById(id)

        return search["id"] if search is not None else None

    def search_organismo(self, id):
        search = self.repositoryOrganismo.getById(id)

        return search["id"] if search is not None else None

    def relationship(self, payload, *arg, **kwargs):
        payload["incidencia"] = self.search_type_incidences(kwargs.get("incidencia"))
        payload["organismo"] = self.search_organismo(kwargs.get("organismo"))

        return payload
