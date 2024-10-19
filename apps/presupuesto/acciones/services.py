from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import AccionRepository


class AccionService(CrudService):
    def __init__(self):
        self.repository = AccionRepository()
