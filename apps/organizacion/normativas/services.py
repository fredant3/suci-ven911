from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import NormativaRepository


class NormativaService(CrudService):
    def __init__(self):
        self.repository = NormativaRepository()

    def getAll(
        self, draw, start, length, search=None, orderBy=None, orderAsc=None, select=("")
    ):
        query = None
        if search:
            query = Q()
            for column in ["id", "name"]:
                query |= Q(**{f"{column}__icontains": search})

        return super().getAll(
            self, draw, start, length, search, orderBy, orderAsc, select
        )
