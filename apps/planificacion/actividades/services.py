from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import ActividadRepository


class ActividadService(CrudService):
    def __init__(self):
        self.repository = ActividadRepository()
