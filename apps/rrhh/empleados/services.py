from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import EmpleadoRepository


class EmpleadoService(CrudService):
    def __init__(self):
        self.repository = EmpleadoRepository()
