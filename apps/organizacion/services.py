from helpers.CrudMixin import CrudService
from organizacion.normativas.repositories import NormativaRepository
from organizacion.reglamentos.repositories import ReglamentoRepository


class OrganizacionService(CrudService):
    def __init__(self):
        self.normativaRepository = NormativaRepository()
        self.reglamentoRepository = ReglamentoRepository()

    def getLastThreeNormativas(self, select, orderBy, orderAsc):
        return self.normativaRepository.getAll(select, orderBy, orderAsc)[:3]

    def getLastThreeReglamentos(self, select, orderBy, orderAsc):
        return self.reglamentoRepository.getAll(select, orderBy, orderAsc)[:3]

    def getAll(
        self,
        draw,
        start,
        length,
        search=None,
        orderBy="created_at",
        orderAsc="asc",
        select=("name", "file", "date", "estado"),
    ):
        normativas = self.getLastThreeNormativas(select, orderBy, orderAsc)
        reglamentos = self.getLastThreeReglamentos(select, orderBy, orderAsc)
        return self.response(list(normativas) + list(reglamentos), start, length, draw)

    def response(self, entities, start, length, draw):
        response = {}
        records_total = len(entities)
        response["draw"] = draw
        response["entities"] = entities
        response["recordsTotal"] = records_total
        response["recordsFiltered"] = records_total
        return response
