from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import ReglamentoRepository


class ReglamentoService(CrudService):
    def __init__(self):
        self.repository = ReglamentoRepository()

    def getAll(
        self, draw, start, length, search=None, orderBy=None, orderAsc=None, select=("")
    ):
        query = None
        if search:
            query = Q()
            for column in ["id", "name"]:
                query |= Q(**{f"{column}__icontains": search})

        return super().getAll(draw, start, length, query, orderBy, orderAsc, select)
