from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import CedenteRepository


class CedenteService(CrudService):
    def __init__(self):
        self.repository = CedenteRepository()
