from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import ObjetivoRepository


class ObjetivoService(CrudService):
    def __init__(self):
        self.repository = ObjetivoRepository()
