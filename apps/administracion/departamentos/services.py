from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import DepartamentoRepository


class DepartamentoService(CrudService):
    def __init__(self):
        self.repository = DepartamentoRepository()